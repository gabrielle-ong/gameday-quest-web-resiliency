# Copyright 2022 Amazon.com and its affiliates; all rights reserved. 
# This file is Amazon Web Services Content and may not be duplicated or distributed without permission.

# WELCOME
WELCOME_1_KEY="welcome1"
WELCOME_1_LABEL="Today at Unicorn.Rentals"
WELCOME_1_VALUE="""
When you’re ready, line up and brace yourselves.....

![robot_queue_image]({})

Your teammate whispers:

_“Psst hey! You’re new here right? I’m sure you’re wondering whats going on, here’s a quick note of what’s been going on, take this!”_

**The note reads:**

* Unicorn.Rentals has an infamous employee who is a sentient A.I. initially programmed to be a **robot vacuum**. 
* After the last few months of hiring issues, the A.I robot vacuum rose up the ranks and is now the **CTO of the company**. 
* Its name is RoboVax-9000 and it is **extremely paranoid about high traffic attacks and bad actors** out to destroy the business. 
"""
WELCOME_1_INDEX=1
WELCOME_1_MARKDOWN=True

WELCOME_2_KEY="welcome2"
WELCOME_2_LABEL="Now that you're up to date..."
WELCOME_2_VALUE="""
_"Today is our team’s first day. Being the latest hires in the company, the CEO has entrusted us to deal with RoboVax’s paranoia today._

_The CEO has shared that we have 45 minutes to set up infrastructure protection methods to give RoboVax a peace of mind."_

Your team will be presented with a series of tasks to solve. Always keep an eye on your Score Events to check the points you've earned. 

As you progress, you will gain the basic skills needed to solve real-world problems.

Here is the AWS Architecture Diagram of the resources that have been provisioned for you:

![architecture_task0]({})
"""
WELCOME_2_INDEX=5
WELCOME_2_MARKDOWN=True


# Task 1 - Cloudfront distribution wrong-origin
TASK1_KEY="task1"
TASK1_LABEL="Task 1: What is CloudFront distribution origin pointing to?"
TASK1_VALUE="""
*BEEP BOOP* - Your first task from RoboVax is here! It seems like our customers are complaining that they are unable to
connect to the application. Quick! Find out which origin (URL) our content delivery network, Amazon CloudFront is currently pointing to.

Click your CloudFront Distribution Domain Name, {}, to see where it brings you to. 

Check your answer by visiting the Amazon Cloudfront service console, which looks something like this:

![cf_console_task1]({})
"""
TASK1_INDEX=10
TASK1_MARKDOWN=True

TASK1_WRONG_ORIGIN_KEY="task1_wrong_answer"
TASK1_WRONG_ORIGIN_LABEL="Task 1: That's not quite right!"
TASK1_WRONG_ORIGIN_VALUE="Not sure how you got that, but that's not correct."
TASK1_WRONG_ORIGIN_INDEX=14
TASK1_WRONG_ORIGIN_MARKDOWN=True


TASK1_CORRECT_ORIGIN_KEY="task1_correct_answer"
TASK1_CORRECT_ORIGIN_LABEL="Task 1: Correct! However, that looks strange..."
TASK1_CORRECT_ORIGIN_VALUE="Our CloudFront origin is currently pointing to www.amazon.com. Are they going shopping instead?"
TASK1_CORRECT_ORIGIN_INDEX=15
TASK1_CORRECT_ORIGIN_MARKDOWN=True

# TASK 2 - CloudFront distribution change-origin
TASK2_KEY="task2"
TASK2_LABEL="## Task 2: Configure the CloudFront distribution origin to your application"
TASK2_VALUE="""
Hmm... We want people to visit our application, not to go shopping. 

Connect Amazon CloudFront to the correct origin in order for your application to work! 

It seems like the correct origin should be the Application Load Balancer (ALB) that is fronting your Amazon EC2 instances. The ALB has already been provisioned for you.
"""
TASK2_INDEX=20
TASK2_MARKDOWN=True

TASK2_COMPLETE_KEY="task2_complete"
TASK2_COMPLETE_LABEL="Task 2: CloudFront origin attachment - Passed!"
TASK2_COMPLETE_VALUE="""
Phew! That was close! Now visit your Cloudfront Distribution Domain Name again, {}, and see where it brings you.

This time, it should open our custom application site instead of www.amazon.com. 

Here is the current architecture:

![architecture_task2]({})
"""
TASK2_COMPLETE_INDEX=28
TASK2_COMPLETE_MARKDOWN=True


# TASK 3 - Logs
TASK3_KEY="task3"
TASK3_LABEL="Task 3: Where are my logs!?"
TASK3_VALUE="""
BEEP BOOP - RoboVax has sounded the alarm! 

We are under attack by bad actors!!! We need to find out where the attack is coming from, but currently we are not able to track the traffic going through Amazon CloudFront. 

Find a way to log the traffic going through Amazon CloudFront to Amazon Simple Storage Service (S3).

An S3 bucket to store the Cloudfront logs has been created for you. The bucket name would look similar to _gameday-cloudfront-logs-XXX-XXX_

"""
TASK3_INDEX=30
TASK3_MARKDOWN=True


TASK3_COMPLETE_KEY="task3_complete"
TASK3_COMPLETE_LABEL="Task 3: Enable logs - Passed!"
TASK3_COMPLETE_VALUE="""
Great job enabling Cloudfront Logs! 

Here’s the current architecture:

![architecture_task3]({})
"""
TASK3_COMPLETE_INDEX=39
TASK3_COMPLETE_MARKDOWN=True

# TASK 4 - IP Address
TASK4_KEY="task4"
TASK4_LABEL="Task 4: Get malicious IP attacker address"
TASK4_VALUE="""
With logging enabled, now the logs will be recorded in the Amazon Simple Storage Service (S3) bucket. Well done!
However, the bad actors are still trying to take down our Unicorn.Rentals application! We managed to obtain the generated log
file of network traffic.

Do you know which IP address is the attack coming from?
```
#Fields: date time ... cs-method cs(Host) cs-uri-stem sc-status ... x-forwarded-for
2022-11-04 21:02:31  ... GET {} /index.html 200 ... 52.23.186.156
2022-11-04 21:02:31  ... GET {} /index.html 200 ... 52.23.186.156
2022-11-04 21:02:31  ... GET {} /index.html 200 ... 52.23.186.156
2022-11-13 22:36:27  ... GET {} /favicon.ico 502 ... 52.23.186.156
2022-11-13 22:36:26  ... GET {} / 502 ... 52.23.186.156
2022-11-13 22:37:02  ... GET {} / 502 ... 52.23.186.156
```
"""
TASK4_INDEX=40
TASK4_MARKDOWN=True

TASK4_IP_ADDRESS_WRONG_KEY="task4_wrong_ip_address"
TASK4_IP_ADDRESS_WRONG_LABEL="Task 4: That's not quite right!"
TASK4_IP_ADDRESS_WRONG_VALUE="Not sure where you got that IP address from, but that's not correct. Please, try again."
TASK4_IP_ADDRESS_WRONG_INDEX=44
TASK4_IP_ADDRESS_WRONG_MARKDOWN=True

TASK4_IP_ADDRESS_CORRECT_KEY="task4_correct_ip_address"
TASK4_IP_ADDRESS_CORRECT_LABEL="Task 4: Thats right!"
TASK4_IP_ADDRESS_CORRECT_VALUE="You identified the malicious IP address!"
TASK4_IP_ADDRESS_CORRECT_INDEX=45
TASK4_IP_ADDRESS_CORRECT_MARKDOWN=True

# TASK 5 - Firewall
TASK5_KEY="task5"
TASK5_LABEL="Task 5: Set up Firewall to block this IP address"
TASK5_VALUE="""
*BZZZRRRRRTTHTHTT* RoboVax has just shut down due to a malfunction! The bad actors managed to get to it! Now there is no one to
tell us whether we are have any security issues or are under extremely high traffic loads!

Quickly set up an AWS Web Application Firewall (WAF) to block this IP address before the bad actors get to any more devices! 

This task is your biggest task (yet). Here are some tips:
* The WAF Web ACL for CloudFront has already been created for you, named _waf-web-acl_. In the Web ACL dashboard, change the dropdown region to Global (CloudFront) to see it.
* In this Web ACL, you will create an IP Set and your own WAF Rule to block this IP address.

![waf_console]({})
"""
TASK5_INDEX=50
TASK5_MARKDOWN=True


TASK5_COMPLETE_KEY="task5_complete"
TASK5_COMPLETE_LABEL="Task 5: Firewall rule - Passed!"
TASK5_COMPLETE_VALUE="""
Great Job setting up the WAF rule. 

Here’s the current architecture:

![architecture_task5]({})
"""
TASK5_COMPLETE_INDEX=59
TASK5_COMPLETE_MARKDOWN=True


# TASK 6 - Final question
TASK6_KEY="task6"
TASK6_LABEL="Task 6: Set up Alarm for metrics"
TASK6_VALUE="""
The worst is over for now, but without RoboVax screaming, no one will be able to tell us of any attacks. 

Let’s look at the metrics on how we can set up an alarm for future attacks.

This is a Cloudwatch monitoring dashboard of some metrics during heavy traffic load. 

![cloudwatch_metrics]({})

Notice which metric is spiking? Pick the right metric that identifies high traffic load.

In your Amazon CloudWatch service dashboard, set up a CloudWatch alarm for this particular metric. Be sure to choose the metric for the correct Cloudwatch distribution!

_Note: If you're unable to find CloudWatch metrics for your distribution, please visit your CloudFront Domain Name URL, {}. You might have already done this in Task 1 and Task 2. The metrics should show up after 1-2 minutes of your visit._

To configure the alarm, measure the average of this metric over 5 minutes. Set the alarm to be in alarm state using Anomaly detection, whenever RequestCount is Outside of the Band of threshold 2.

Notifications will be sent when the alarm state trigger is In Alarm.

Send notifications to an existing SNS topic. The SNS topic has been provisioned for you, called _SNS-topic-for-cloudwatch-alarm_.
"""
TASK6_INDEX=60
TASK6_MARKDOWN=True

TASK6_COMPLETE_KEY="task6_complete"
TASK6_COMPLETE_LABEL="Task 6: CloudWatch alarm - Passed!"
TASK6_COMPLETE_VALUE="""
Great Job creating your CloudWatch alarm! Now we will know of possible future attacks calmly, without RoboVax screaming.
"""
TASK6_COMPLETE_INDEX=69
TASK6_COMPLETE_MARKDOWN=True


# TASK6_WRONG_KEY="task6_wrong_answer"
# TASK6_WRONG_LABEL="You don't know THE answer, do you?"
# TASK6_WRONG_VALUE="Our CEO will be very disappointed"
# TASK6_WRONG_INDEX=97
# TASK6_WRONG_MARKDOWN=True


# QUEST COMPLETE
QUEST_COMPLETE_KEY='quest_complete'
QUEST_COMPLETE_LABEL='CONGRATULATIONS!'
QUEST_COMPLETE_VALUE="""
You have successfully protected your application and increased web resiliency for RoboVax and Unicorn Rentals.

You configured CloudFront for your users to access your application quickly and reliably. When the bad actors tried to attack your application, you identified them with CloudFront Logs and blocked them using WAF Rules. 

Lastly, you’ve set an alarm to detect future high traffic incidents so that you and your (ex-) boss, RoboVax can have a peace of mind.

Not bad, rookie. Maybe you'll be CTO soon?

Here is the final architecture you’ve achieved:

![architecture_final]({})

You've saved the day. You've completed this quest. Go conquer the world.
"""
QUEST_COMPLETE_INDEX=100
QUEST_COMPLETE_MARKDOWN=True
