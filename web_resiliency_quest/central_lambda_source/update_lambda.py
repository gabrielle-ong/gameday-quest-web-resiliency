# Copyright 2022 Amazon.com and its affiliates; all rights reserved. 
# This file is Amazon Web Services Content and may not be duplicated or distributed without permission.
import json
import os
import boto3
from datetime import datetime
import dynamodb_utils
import quest_const
import input_const
import output_const
import scoring_const
import hint_const
from aws_gameday_quests.gdQuestsApi import GameDayQuestsApiClient

# Standard AWS GameDay Quests Environment Variables
QUEST_ID = os.environ['QUEST_ID']
QUEST_API_BASE = os.environ['QUEST_API_BASE']
QUEST_API_TOKEN = os.environ['QUEST_API_TOKEN']
GAMEDAY_REGION = os.environ['GAMEDAY_REGION']

# Quest Environment Variables
QUEST_TEAM_STATUS_TABLE = os.environ['QUEST_TEAM_STATUS_TABLE']

# Dynamo DB resource
dynamodb = boto3.resource('dynamodb')
quest_team_status_table = dynamodb.Table(QUEST_TEAM_STATUS_TABLE)

# This function is triggered by sns_lambda.py whenever the team has provided input via the event UI. It validates
# the input and performs related operations, such as updating the team's DynamoDB table record or posting a feedback message.
# Expected event parameters: {'team_id': team_id,'key': key, 'value': value}
def lambda_handler(event, context):
    print(f"update_lambda invocation, event:{json.dumps(event, default=str)}, context: {str(context)}")

    # Instantiate the Quest API Client.
    quests_api_client = GameDayQuestsApiClient(QUEST_API_BASE, QUEST_API_TOKEN)

    # Check if event is running
    event_status = quests_api_client.get_event_status()
    if event_status['status'] != quest_const.EVENT_IN_PROGRESS:
        print(f"Event Status: {event_status['status']}, aborting UPDATE_LAMBDA")
        return

    # Check if quest is active for the team
    quest_status = quests_api_client.get_quest_for_team(team_id=event['team_id'], quest_id=QUEST_ID)
    if quest_status['quest-state'] != quest_const.TEAM_QUEST_IN_PROGRESS:
        print(f"Quest Status: {quest_status['quest-state']}, aborting UPDATE_LAMBDA")

    dynamodb_response = quest_team_status_table.get_item(Key={'team-id': event['team_id']})
    print(f"Retrieved team state for team {event['team_id']}: {json.dumps(dynamodb_response, default=str)}")
    team_data = dynamodb_response['Item']

    task1_origin = "www.amazon.com"
    task4_ip_address = "192.0.2.200"

    # Task 1 - Wrong origin domain
    if (event['key'] == input_const.TASK1_ORIGIN_KEY
        and not team_data['is-identified-origin']): # This second check is needed to avoid multiple submissions since points are being given here

        # Check team's input value
        value = event['value'].strip().strip("http://") # Being forgiven if leading spaces, trailing spaces, or protocol were added
        if value == task1_origin:

            # Correct answer - switch flag to true
            team_data['is-identified-origin'] = True

            try:
                # First update DynamoDB to avoid race conditions, then do the rest on success
                dynamodb_utils.save_team_data(team_data, quest_team_status_table)

                # Delete previous error if present
                quests_api_client.delete_output(
                    team_id=team_data["team-id"],
                    quest_id=QUEST_ID, 
                    key=output_const.TASK1_WRONG_ORIGIN_KEY
                )
                
                # Delete input since cannot be updated as task can be started only once
                quests_api_client.delete_input(
                    team_id=team_data["team-id"],
                    quest_id=QUEST_ID, 
                    key=input_const.TASK1_ORIGIN_KEY
                )

                # Delete hint
                quests_api_client.delete_hint(
                    team_id=team_data['team-id'],
                    quest_id=QUEST_ID,
                    hint_key=hint_const.TASK1_HINT1_KEY,
                    detail=True
                )

                # Replace input with an output to leave a trace of what has been done
                quests_api_client.post_output(
                    team_id=team_data['team-id'],
                    quest_id=QUEST_ID,
                    key=output_const.TASK1_CORRECT_ORIGIN_KEY,
                    label=output_const.TASK1_CORRECT_ORIGIN_LABEL,
                    value=output_const.TASK1_CORRECT_ORIGIN_VALUE.format(task1_origin),
                    dashboard_index=output_const.TASK1_CORRECT_ORIGIN_INDEX,
                    markdown=output_const.TASK1_CORRECT_ORIGIN_MARKDOWN,
                )
                # Award points
                quests_api_client.post_score_event(
                    team_id=team_data["team-id"],
                    quest_id=QUEST_ID,
                    description=scoring_const.TASK1_CORRECT_ORIGIN_DESC,
                    points=scoring_const.TASK1_CORRECT_ORIGIN_POINTS
                )
            
            except Exception as err:
                print(f"Error while handling team update request: {err}")
        else:
            # Post output
            quests_api_client.post_output(
                team_id=team_data['team-id'],
                quest_id=QUEST_ID,
                key=output_const.TASK1_WRONG_ORIGIN_KEY,
                label=output_const.TASK1_WRONG_ORIGIN_LABEL,
                value=output_const.TASK1_WRONG_ORIGIN_VALUE,
                dashboard_index=output_const.TASK1_WRONG_ORIGIN_INDEX,
                markdown=output_const.TASK1_WRONG_ORIGIN_MARKDOWN,
            )
            # Detract points
            quests_api_client.post_score_event(
                team_id=team_data["team-id"],
                quest_id=QUEST_ID,
                description=scoring_const.TASK1_WRONG_ORIGIN_DESC,
                points=scoring_const.TASK1_WRONG_ORIGIN_POINTS
            )

    # Task 4 - Needle in the ocean       
    elif (event['key'] == input_const.TASK4_ENDPOINT_KEY
        and not team_data['is-ip-address']): # This second check is needed to avoid multiple submissions since points are being given here

        # Check team's input value
        value = event['value'].strip().strip("http://") # Being forgiven if leading spaces, trailing spaces, or protocol were added
        if value == task4_ip_address:

            # Correct answer - switch flag to true
            team_data['is-ip-address'] = True

            try:
                # First update DynamoDB to avoid race conditions, then do the rest on success
                dynamodb_utils.save_team_data(team_data, quest_team_status_table)

                # Delete previous error if present
                quests_api_client.delete_output(
                    team_id=team_data["team-id"],
                    quest_id=QUEST_ID, 
                    key=output_const.TASK4_IP_ADDRESS_WRONG_KEY
                )
                
                # Delete input since cannot be updated as task can be started only once
                quests_api_client.delete_input(
                    team_id=team_data["team-id"],
                    quest_id=QUEST_ID, 
                    key=input_const.TASK4_ENDPOINT_KEY
                )

                # Delete hint
                quests_api_client.delete_hint(
                    team_id=team_data['team-id'],
                    quest_id=QUEST_ID,
                    hint_key=hint_const.TASK4_HINT1_KEY,
                    detail=True
                )

                # Replace input with an output to leave a trace of what has been done
                quests_api_client.post_output(
                    team_id=team_data['team-id'],
                    quest_id=QUEST_ID,
                    key=output_const.TASK4_IP_ADDRESS_CORRECT_KEY,
                    label=output_const.TASK4_IP_ADDRESS_CORRECT_LABEL,
                    value=output_const.TASK4_IP_ADDRESS_CORRECT_VALUE.format(task4_ip_address),
                    dashboard_index=output_const.TASK4_IP_ADDRESS_CORRECT_INDEX,
                    markdown=output_const.TASK4_IP_ADDRESS_CORRECT_MARKDOWN,
                )
                # Award points
                quests_api_client.post_score_event(
                    team_id=team_data["team-id"],
                    quest_id=QUEST_ID,
                    description=scoring_const.TASK4_CORRECT_IP_ADDRESS_DESC,
                    points=scoring_const.TASK4_CORRECT_IP_ADDRESS_POINTS
                )
            
            except Exception as err:
                print(f"Error while handling team update request: {err}")
        else:
            # Post output
            quests_api_client.post_output(
                team_id=team_data['team-id'],
                quest_id=QUEST_ID,
                key=output_const.TASK4_IP_ADDRESS_WRONG_KEY,
                label=output_const.TASK4_IP_ADDRESS_WRONG_LABEL,
                value=output_const.TASK4_IP_ADDRESS_WRONG_VALUE,
                dashboard_index=output_const.TASK4_IP_ADDRESS_WRONG_INDEX,
                markdown=output_const.TASK4_IP_ADDRESS_WRONG_MARKDOWN,
            )
            # Detract points
            quests_api_client.post_score_event(
                team_id=team_data["team-id"],
                quest_id=QUEST_ID,
                description=scoring_const.TASK4_WRONG_IP_ADDRESS_DESC,
                points=scoring_const.TASK4_WRONG_IP_ADDRESS_POINTS
            )

    else:
        print(f"Unknown input key {event['key']} encountered, ignoring.")
