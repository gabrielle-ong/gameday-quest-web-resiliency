# Copyright 2022 Amazon.com and its affiliates; all rights reserved. 
# This file is Amazon Web Services Content and may not be duplicated or distributed without permission.
import os
from datetime import datetime
import boto3
import json
import dynamodb_utils
import quest_const
import output_const
import input_const
import hint_const
import scoring_const
import http.client
import time
from aws_gameday_quests.gdQuestsApi import GameDayQuestsApiClient

# Standard AWS GameDay Quests Environment Variables
QUEST_ID = os.environ['QUEST_ID']
QUEST_API_BASE = os.environ['QUEST_API_BASE']
QUEST_API_TOKEN = os.environ['QUEST_API_TOKEN']
GAMEDAY_REGION = os.environ['GAMEDAY_REGION']

# Quest Environment Variables
QUEST_TEAM_STATUS_TABLE = os.environ['QUEST_TEAM_STATUS_TABLE']
CHAOS_TIMER_MINUTES = os.environ['CHAOS_TIMER_MINUTES']

# Dynamo DB setup
dynamodb = boto3.resource('dynamodb')
quest_team_status_table = dynamodb.Table(QUEST_TEAM_STATUS_TABLE)

# This function is triggered by cron_lambda.py. It performs validation of team actions, such as assuming a role in their
# AWS account to check resources or trigger chaos events, as well as updating progress, or posting a message to the team’s event UI.
# Expected event payload is the QuestsAPI entry for this team
def lambda_handler(event, context):
    print(f"check_team_lambda invocation, event:{json.dumps(event, default=str)}, context: {str(context)}")

    # Instantiate the Quest API Client.
    quests_api_client = GameDayQuestsApiClient(QUEST_API_BASE, QUEST_API_TOKEN)

    # Check if event is running
    event_status = quests_api_client.get_event_status()
    if event_status['status'] != quest_const.EVENT_IN_PROGRESS:
        print(f"Event Status: {event_status}, aborting CHECK_TEAM_LAMBDA")
        return

    dynamodb_response = quest_team_status_table.get_item(Key={'team-id': event['team-id']})
    print(f"Retrieved quest team state for team {event['team-id']}: {json.dumps(dynamodb_response, default=str)}")

    # Make a copy of the original array to be able later on to do a comparison and validate whether a DynamoDB update is needed    
    team_data = dynamodb_response['Item'].copy() # Check init_lambda for the format

    # Task 0 to start continuous scoring
    team_data = continuous_scoring(quests_api_client, team_data)

    # Task 1 is check cloudfront origin

    # Task 2 evaluation
    team_data = attach_cloudfront_origin(quests_api_client, team_data)
    
    # Task 3 evaluation
    team_data = evaluate_cloudfront_logging(quests_api_client, team_data)

    # Task 4 is Find needle in ocean

    # Task 5 evaluation
    team_data = evaluate_cloudfront_waf(quests_api_client, team_data)

    # # Task 5 evaluation
    # team_data = evaluate_access_key(quests_api_client, team_data)

    # Task 6 evaluation
    team_data = evaluate_cloudwatch_alarm(quests_api_client, team_data)

    # Complete quest if everything is done
    check_and_complete_quest(quests_api_client, QUEST_ID, team_data)

    # Compare initial DynamoDB item with its copy to check whether changes were made. 
    if dynamodb_response['Item']==team_data:
        print("No changes throughout this run - no need to update the DynamoDB item")
    else:
        dynamodb_utils.save_team_data(team_data, quest_team_status_table)

# Task 0 - Welcome (Continuous scoring)
def continuous_scoring(quests_api_client, team_data):
    print(f"Continuous scoring started for team {team_data['team-id']}")

    # Check whether quest is completed
    if not check_and_complete_quest(quests_api_client, QUEST_ID, team_data):
        quests_api_client.post_score_event(
            team_id=team_data["team-id"],
            quest_id=QUEST_ID,
            description=scoring_const.CONTINUOUS_DESC,
            points=scoring_const.CONTINUOUS_POINTS
        )

    return team_data

# Task 2 evaluation - CloudFront Distribution Origin
def attach_cloudfront_origin(quests_api_client, team_data):
    print(f"Evaluating CloudFront Distribution Origin for team {team_data['team-id']}")

    # Check whether task was completed already
    if not team_data['is-attach-cloudfront-origin-done']:

        # Establish cross-account session
        print(f"Assuming Ops role for team {team_data['team-id']}")
        xa_session = quests_api_client.assume_team_ops_role(team_data['team-id'])

        # Lookup events in CloudFront
        cloudfront_client = xa_session.client('cloudfront')
        quest_start = datetime.fromtimestamp(team_data['quest-start-time'])
        # cloudfront_response = cloudfront_client.list_distributions()
        # origin_domain_name = cloudfront_response['DistributionList']['Items'][0]['Origins']['Items'][0]['DomainName']
        cloudfront_response = cloudfront_client.get_distribution(Id=team_data['cloudfront-distribution-id'])
        origin_domain_name = cloudfront_response['Distribution']['DistributionConfig']['Origins']['Items'][0]['DomainName']
        print(f"CloudFront result for team {team_data['team-id']}: {cloudfront_response}")

        # Complete task if CloudFront Origin was attached
        if origin_domain_name == team_data['elb-dns-name'].lower():

            # Switch flag
            team_data['is-attach-cloudfront-origin-done'] = True

            # Delete hint
            quests_api_client.delete_hint(
                team_id=team_data['team-id'],
                quest_id=QUEST_ID,
                hint_key=hint_const.TASK2_HINT1_KEY,
                detail=True
            )
            # Handling a response status code other than 200. In this case, we are just logging
            # if response['statusCode'] != 200:
            #     print(response)

            # Post task final message
            quests_api_client.post_output(
                team_id=team_data['team-id'],
                quest_id=QUEST_ID,
                key=output_const.TASK2_COMPLETE_KEY,
                label=output_const.TASK2_COMPLETE_LABEL,
                value=output_const.TASK2_COMPLETE_VALUE,
                dashboard_index=output_const.TASK2_COMPLETE_INDEX,
                markdown=output_const.TASK2_COMPLETE_MARKDOWN,
            )

            # Award final points
            quests_api_client.post_score_event(
                team_id=team_data["team-id"],
                quest_id=QUEST_ID,
                description=scoring_const.TASK2_COMPLETE_DESC,
                points=scoring_const.TASK2_COMPLETE_POINTS
            )

        else:
            print(f"No matching CloudFront events found for team {team_data['team-id']}")

    return team_data

# # Checks whether the monitoring web app is up or done and returns True or False respectively
# def check_webapp(team_data):
#     try:
#         print(f"Testing web app status")
#         conn = http.client.HTTPConnection(team_data['ip-address'], timeout=5)
#         conn.request("GET", "/index.html")
#         res = conn.getresponse()
#         data = res.read().decode("utf-8") 
#         print(res.status)
#         if res.status != 200:
#             raise Exception(f"Web app down: {res.status} - {res.reason}")
#         return True
#     except Exception as e:
#         print(f"Web app not available: {e}")
#         return False


# Task 3 evaluation - CloudFront logs
def evaluate_cloudfront_logging(quests_api_client, team_data):
    print(f"Evaluating CloudFront Logs task for team {team_data['team-id']}")

    # Check whether task was completed already
    if not team_data['is-cloudfront-logs-enabled']:

        # Establish cross-account session
        print(f"Assuming Ops role for team {team_data['team-id']}")
        xa_session = quests_api_client.assume_team_ops_role(team_data['team-id'])

        # Lookup events in CloudFront
        cloudfront_client = xa_session.client('cloudfront')
        quest_start = datetime.fromtimestamp(team_data['quest-start-time'])
        # cloudfront_response = cloudfront_client.list_distributions()
        # distribution_id = cloudfront_response['DistributionList']['Items'][0]['Id']
        # cloudfront_distribution_response = cloudfront_client.get_distribution(Id=distribution_id)
        cloudfront_response = cloudfront_client.get_distribution(Id=team_data['cloudfront-distribution-id'])
        logging_flag = cloudfront_response['Distribution']['DistributionConfig']['Logging']['Enabled']

        print(f"CloudFront result for team {team_data['team-id']}: {logging_flag}")

        # Complete task if CloudShell was launched
        if logging_flag:

            # Switch flag
            team_data['is-cloudfront-logs-enabled'] = True

            # Delete hint
            quests_api_client.delete_hint(
                team_id=team_data['team-id'],
                quest_id=QUEST_ID,
                hint_key=hint_const.TASK3_HINT1_KEY,
                detail=True
            )
            # Handling a response status code other than 200. In this case, we are just logging
            # if response['statusCode'] != 200:
            #     print(response)

            # Post task final message
            quests_api_client.post_output(
                team_id=team_data['team-id'],
                quest_id=QUEST_ID,
                key=output_const.TASK3_COMPLETE_KEY,
                label=output_const.TASK3_COMPLETE_LABEL,
                value=output_const.TASK3_COMPLETE_VALUE,
                dashboard_index=output_const.TASK3_COMPLETE_INDEX,
                markdown=output_const.TASK3_COMPLETE_MARKDOWN,
            )

            # Award final points
            quests_api_client.post_score_event(
                team_id=team_data["team-id"],
                quest_id=QUEST_ID,
                description=scoring_const.TASK3_COMPLETE_DESC,
                points=scoring_const.TASK3_COMPLETE_POINTS
            )

        else:
            print(f"No matching CloudTrail events found for team {team_data['team-id']}")

    return team_data


# Task 5 - WAF Rule
# 'is-cloudfront-ip-set-created'
# 'is-cloudfront-waf-attached'
def evaluate_cloudfront_waf(quests_api_client, team_data):
    print(f"Evaluating CloudFront WAF task for team {team_data['team-id']}")

    # Check whether task was completed already
    if not team_data['is-cloudfront-ip-set-created'] or not team_data['is-cloudfront-waf-attached']:
        print("TASK 5 START")

        ip_address_from_task2b = "10.0.0.0" + "/32"
        created_web_acl_name = "waf-web-acl"
        web_acl_id = ""
        web_acl_arn = ""
        ip_set_id = ""
        ip_set_arn = ""
        waf_web_acl_flag = False
        

        # Establish cross-account session
        print(f"Assuming Ops role for team {team_data['team-id']}")
        xa_session = quests_api_client.assume_team_ops_role(team_data['team-id'])

        # Lookup events in WAF IP Sets
        waf_client = xa_session.client('wafv2')
        quest_start = datetime.fromtimestamp(team_data['quest-start-time'])
        waf_ip_set_response = waf_client.list_ip_sets(Scope="CLOUDFRONT")
        ip_sets = waf_ip_set_response['IPSets']
        for ip_set in ip_sets:
            waf_ip_set_response = waf_client.get_ip_set(Id=ip_set['Id'], Scope="CLOUDFRONT", Name=ip_set['Name'])
            ip_set_addresses = waf_ip_set_response['IPSet']['Addresses']
            for ip_set_address in ip_set_addresses:
                if ip_set_address == ip_address_from_task2b:
                    ip_set_id = ip_set['Id']
                    ip_set_arn = ip_set['ARN']
                    break
        
        # Lookup events in WAF WebACL
        quest_start = datetime.fromtimestamp(team_data['quest-start-time'])
        waf_web_acls_response = waf_client.list_web_acls(Scope="CLOUDFRONT")
        web_acls = waf_web_acls_response['WebACLs']
        for web_acl in web_acls:
            if web_acl['Name'] == created_web_acl_name:
                web_acl_id = web_acl['Id']
                web_acl_arn = web_acl['ARN']
                break

        waf_web_acl_response = waf_client.get_web_acl(Name=created_web_acl_name, Scope="CLOUDFRONT", Id=web_acl_id)
        web_acl_rules = waf_web_acl_response['WebACL']['Rules']
        for rule in web_acl_rules:
            rule_ip_set = rule['Statement']['IPSetReferenceStatement']
            if rule_ip_set['ARN'] == ip_set_arn:
                waf_web_acl_flag = True
                break

            # rule_response = waf_client.get_rule_group(Name=rule['Name'], Scope="CLOUDFRONT")
            # rule_predicates = rule_response['Rule']['Predicates']
            # for predicate in rule_predicates:
            #     if predicate['DataId'] == ip_set_id:
            #         waf_web_acl_flag = True
            #         break
        
        if ip_set_id != "" and waf_web_acl_flag:
            team_data['is-cloudfront-ip-set-created'] = True
            # Lookup events in CloudFront
            cloudfront_client = xa_session.client('cloudfront')
            quest_start = datetime.fromtimestamp(team_data['quest-start-time'])
            # cloudfront_response = cloudfront_client.list_distributions()
            # distribution_id = cloudfront_response['DistributionList']['Items'][0]['Id']
            # cloudfront_distribution_response = cloudfront_client.get_distribution(Id=distribution_id)
            cloudfront_response = cloudfront_client.get_distribution(Id=team_data['cloudfront-distribution-id'])
            cloudfront_web_acl_id = cloudfront_response['Distribution']['DistributionConfig']['WebACLId']

            print(f"TASK 5 result for team {team_data['team-id']}: {cloudfront_web_acl_id}")

            # Complete task if WebACL was attached
            if cloudfront_web_acl_id == web_acl_arn:

                # Switch flag
                team_data['is-cloudfront-waf-attached'] = True

                # Delete hint
                quests_api_client.delete_hint(
                    team_id=team_data['team-id'],
                    quest_id=QUEST_ID,
                    hint_key=hint_const.TASK5_HINT1_KEY,
                    detail=True
                )
                # Handling a response status code other than 200. In this case, we are just logging
                # if response['statusCode'] != 200:
                #     print(response)

                # Post task final message
                quests_api_client.post_output(
                    team_id=team_data['team-id'],
                    quest_id=QUEST_ID,
                    key=output_const.TASK5_COMPLETE_KEY,
                    label=output_const.TASK5_COMPLETE_LABEL,
                    value=output_const.TASK5_COMPLETE_VALUE,
                    dashboard_index=output_const.TASK5_COMPLETE_INDEX,
                    markdown=output_const.TASK5_COMPLETE_MARKDOWN,
                )

                # Award final points
                quests_api_client.post_score_event(
                    team_id=team_data["team-id"],
                    quest_id=QUEST_ID,
                    description=scoring_const.TASK5_COMPLETE_DESC,
                    points=scoring_const.TASK5_COMPLETE_POINTS
                )

            else:
                print(f"No matching CloudTrail events found for team {team_data['team-id']}")

    return team_data

# Task 6 - CloudWatch Metrics
def evaluate_cloudwatch_alarm(quests_api_client, team_data):

    if not team_data['is-cloudwatch-alarm-created']:
        print("TASK 6 START")

        alarm_flag = False
        
        # Complete task if WebACL was attached
        if alarm_flag:

            # Switch flag
            team_data['is-cloudwatch-alarm-created'] = True

            # Delete hint
            quests_api_client.delete_hint(
                team_id=team_data['team-id'],
                quest_id=QUEST_ID,
                hint_key=hint_const.TASK6_HINT1_KEY,
                detail=True
            )
            # Handling a response status code other than 200. In this case, we are just logging
            # if response['statusCode'] != 200:
            #     print(response)

            # Post task final message
            quests_api_client.post_output(
                team_id=team_data['team-id'],
                quest_id=QUEST_ID,
                key=output_const.TASK6_COMPLETE_KEY,
                label=output_const.TASK6_COMPLETE_LABEL,
                value=output_const.TASK6_COMPLETE_VALUE,
                dashboard_index=output_const.TASK6_COMPLETE_INDEX,
                markdown=output_const.TASK6_COMPLETE_MARKDOWN,
            )

            # Award final points
            quests_api_client.post_score_event(
                team_id=team_data["team-id"],
                quest_id=QUEST_ID,
                description=scoring_const.TASK6_COMPLETE_DESC,
                points=scoring_const.TASK6_COMPLETE_POINTS
            )

        else:
            print(f"No matching CloudTrail events found for team {team_data['team-id']}")

    return team_data


# Verify that all tasks have been successfully done and complete the quest if so
def check_and_complete_quest(quests_api_client, quest_id, team_data):

    # Check if everything is done
    if (team_data['is-identified-origin']                   # Task 1
        and team_data['is-attach-cloudfront-origin-done']   # Task 2
        and team_data['is-cloudfront-logs-enabled']         # Task 3
        and team_data['is-answer-to-ip-address-correct']    # Task 4
        and team_data['is-cloudfront-ip-set-created']       # Task 5
        and team_data['is-cloudfront-waf-attached']         # Task 5
        and team_data['is-cloudwatch-alarm-created']):      # Task 6

        # Award quest complete points
        print(f"Team {team_data['team-id']} has completed this quest, posting output and awarding points")
        quests_api_client.post_score_event(
            team_id=team_data["team-id"],
            quest_id=quest_id,
            description=scoring_const.QUEST_COMPLETE_DESC,
            points=scoring_const.QUEST_COMPLETE_POINTS
        )

        # Award quest complete bonus points
        bonus_points = calculate_bonus_points(quests_api_client, quest_id, team_data)
        quests_api_client.post_score_event(
            team_id=team_data["team-id"],
            quest_id=quest_id,
            description=scoring_const.QUEST_COMPLETE_BONUS_DESC,
            points=bonus_points
        )

        # Post quest complete message
        quests_api_client.post_output(
            team_id=team_data['team-id'],
            quest_id=quest_id,
            key=output_const.QUEST_COMPLETE_KEY,
            label=output_const.QUEST_COMPLETE_LABEL,
            value=output_const.QUEST_COMPLETE_VALUE,
            dashboard_index=output_const.QUEST_COMPLETE_INDEX,
            markdown=output_const.QUEST_COMPLETE_MARKDOWN,
        )

        # Complete quest
        quests_api_client.post_quest_complete(team_id=team_data['team-id'], quest_id=quest_id)

        return True

    return False


# Checks whether the chaos event timer is up by calculating the difference between the current time and 
# the timer's start time plus the minutes to trigger the chaos event
def is_chaos_timer_up(timer_start_time, timer_minutes):

    # Timer start time
    start_time = datetime.fromtimestamp(timer_start_time)

    # Current time
    current_time = datetime.now()

    # Time difference
    time_diff = current_time - start_time
    
    # Time difference in minutes
    minutes = int(time_diff.total_seconds() / 60)

    if minutes >= timer_minutes:
        print(f"Chaos event timer is up: {minutes} minutes have elapsed")
        return True
    else:
        print(f"No time for chaos event yet: {timer_minutes - minutes} minutes left")

    return False


# Calculate quest completion bonus points
# This is to reward teams that complete the quest faster
def calculate_bonus_points(quests_api_client, quest_id, team_data):
    quest = quests_api_client.get_quest_for_team(team_data['team-id'], quest_id)

    # Get quest start time
    start_time = datetime.fromtimestamp(quest['quest-start-time'])

    # Get quest end time, that is, current time
    end_time = datetime.now()

    # Calculate elapsed time
    time_diff = end_time - start_time
    minutes = int(time_diff.total_seconds() / 60)

    # Calculate bonus points based on elapsed time
    bonus_points = int(scoring_const.QUEST_COMPLETE_POINTS / minutes * scoring_const.QUEST_COMPLETE_MULTIPLIER)
    print(f"Bonus points on {scoring_const.QUEST_COMPLETE_POINTS} done in {minutes} minutes: {bonus_points}")

    return bonus_points