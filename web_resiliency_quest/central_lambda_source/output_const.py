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

* Unicorn.Rentals has an infamous employee who is a sentient A.I. initially programmed to be a **_robot vacuum**_. 
* After the last few months of hiring issues, the A.I. rose up the ranks and is now the CTO of the company. 
* It’s name is RoboVax-9000 and it is **_extremely paranoid about high traffic attacks and bad actors**_ out to destroy the business. 
"""
WELCOME_1_INDEX=1
WELCOME_1_MARKDOWN=True


WELCOME_2_KEY="welcome2"
WELCOME_2_LABEL="Now that you're up to date..."
WELCOME_2_VALUE="""
_"Today is our team’s first day. Being the latest hires in the company, the CEO has entrusted us to deal with RoboVax’s paranoia today.

The CEO has shared that we have 45 minutes to set up infrastructure protection methods to give RoboVax a peace of mind."_

Your team will be presented with a series of challenges to solve. Communicate with your team and choose a strategy for dividing up the work. Always keep an eye on your Score Events. As you progress, you will gain the basic skills needed to solve real-world problems.

**Please work in the AWS us-east-1 region.**_

Here is the AWS Architecture Diagram of the resources that have been provisioned for you:

![architecture_task0]({})
"""
WELCOME_2_INDEX=2
WELCOME_2_MARKDOWN=True


# Task 1 - Cloudfront distribution wrong-origin
TASK1_KEY="task1"
TASK1_LABEL="What is CloudFront distribution origin pointing to?"
TASK1_VALUE="""
*BEEP BOOP* - Your first task from RoboVax is here! It seems like our customers are complaining that they are unable to
connect to the application. Quick! Find out which origin (URL) our content delivery network (CDN) is currently pointing to.
The CDN service web page should look something like this:

![cf_console_task1]({})
"""
TASK1_INDEX=10
TASK1_MARKDOWN=True

TASK1_WRONG_ORIGIN_KEY="task1_wrong_answer"
TASK1_WRONG_ORIGIN_LABEL="That's not quite right!"
TASK1_WRONG_ORIGIN_VALUE="Not sure how you configured that, but that's not correct."
TASK1_WRONG_ORIGIN_INDEX=14
TASK1_WRONG_ORIGIN_MARKDOWN=True


TASK1_CORRECT_ORIGIN_KEY="task1_correct_answer"
TASK1_CORRECT_ORIGIN_LABEL="That's right, but..."
TASK1_CORRECT_ORIGIN_VALUE="Our CloudFront origin is currently pointing to www.amazon.com. Are they going shopping instead?"
TASK1_CORRECT_ORIGIN_INDEX=15
TASK1_CORRECT_ORIGIN_MARKDOWN=True


TASK1_COMPLETE_KEY="task1_complete"
TASK1_COMPLETE_LABEL="Identify distribution origin: Passed!"
TASK1_COMPLETE_VALUE="""
All done. Thank you for your help.
"""
TASK1_COMPLETE_INDEX=17
TASK1_COMPLETE_MARKDOWN=True

# TASK 2 - CloudFront distribution change-origin
TASK2_KEY="task2"
TASK2_LABEL="Now correctly configure the CloudFront distribution to your Application Load Balancer"
TASK2_VALUE="""
Hmm... We want people to visit our application, not to go shopping. 

Connect Amazon CloudFront to the correct origin in order for the application to work! 

It seems like the correct origin should be the Application Load Balancer (ALB) that is fronting your Amazon EC2 instances. The ALB has already been provisioned for you.
"""
TASK2_INDEX=20
TASK2_MARKDOWN=True

# TASK2_WRONG_ORIGIN_KEY="task2_wrong_answer"
# TASK2_WRONG_ORIGIN_LABEL="That's not quite right!"
# TASK2_WRONG_ORIGIN_VALUE="Not sure how you configured that, but that's not correct."
# TASK2_WRONG_ORIGIN_INDEX=24
# TASK2_WRONG_ORIGIN_MARKDOWN=True


# TASK2_CORRECT_ORIGIN_KEY="task2_correct_answer"
# TASK2_CORRECT_ORIGIN_LABEL="Have you updated the origin?"
# TASK2_CORRECT_ORIGIN_VALUE="That's right! Thank you for verifying the EC2 instance's IP address: {}"
# TASK2_CORRECT_ORIGIN_INDEX=25
# TASK2_CORRECT_ORIGIN_MARKDOWN=True


TASK2_COMPLETE_KEY="task2_complete"
TASK2_COMPLETE_LABEL="CloudFront origin attachment: Passed!"
TASK2_COMPLETE_VALUE="""
Phew! That was close, our customers can access the application now. 

Here is the current architecture:

![architecture_task2]({})
"""
TASK2_COMPLETE_INDEX=28
TASK2_COMPLETE_MARKDOWN=True


# TASK 3 - Logs
TASK3_KEY="task3"
TASK3_LABEL="Where are my logs!?"
TASK3_VALUE="""
BEEP BOOP - RoboVax has sounded the alarm! 

We are under attack by bad actors!!! We need to find out where the attack is coming from, but currently we are not able to track the traffic going through Amazon CloudFront. 

Find a way to log the traffic going through Amazon CloudFront to Amazon Simple Storage Service (S3).

An S3 bucket to store the Cloudfront logs has been created for you. The bucket name would look similar to _gameday-cloudfront-logs-XXX-XXX_

"""
TASK3_INDEX=30
TASK3_MARKDOWN=True


TASK3_COMPLETE_KEY="task3_complete"
TASK3_COMPLETE_LABEL="Enable logs: Passed!"
TASK3_COMPLETE_VALUE="""
Great job enabling Cloudfront Logs! 

Here’s the current architecture:

![architecture_task3]({})
"""
TASK3_COMPLETE_INDEX=39
TASK3_COMPLETE_MARKDOWN=True

# TASK 4 - IP Address
TASK4_KEY="task4"
TASK4_LABEL="Get malicious IP attacker address"
TASK4_VALUE="""
With logging enabled, now the logs will be recorded in the Amazon Simple Storage Service (S3) bucket. Well done!
However, the bad actors are still trying to take down our Unicorn.Rentals application! We managed to obtain the generated log
file of network traffic.

Do you know which IP address is the attack coming from?

![sample_log]({})
"""
TASK4_INDEX=40
TASK4_MARKDOWN=True

TASK4_IP_ADDRESS_WRONG_KEY="task4_wrong_ip_address"
TASK4_IP_ADDRESS_WRONG_LABEL="That's not quite right!"
TASK4_IP_ADDRESS_WRONG_VALUE="Not sure where you got that IP address from, but that's not correct. Please, try again."
TASK4_IP_ADDRESS_WRONG_INDEX=44
TASK4_IP_ADDRESS_WRONG_MARKDOWN=True

TASK4_IP_ADDRESS_CORRECT_KEY="task4_correct_ip_address"
TASK4_IP_ADDRESS_CORRECT_LABEL="Thats right!"
TASK4_IP_ADDRESS_CORRECT_VALUE="You identified the malicious IP address."
TASK4_IP_ADDRESS_CORRECT_INDEX=45
TASK4_IP_ADDRESS_CORRECT_MARKDOWN=True


TASK4_COMPLETE_KEY="task4_complete"
TASK4_COMPLETE_LABEL="IP Address: Passed!"
TASK4_COMPLETE_VALUE="""
All done. Great job neutralizing the compromised access key.
"""
TASK4_COMPLETE_INDEX=49
TASK4_COMPLETE_MARKDOWN=True

# TASK 5 - Firewall
TASK5_KEY="task5"
TASK5_LABEL="Set up Firewall to block this IP address"
TASK5_VALUE="""
*BZZZRRRRRTTHTHTT* RoboVax has just shut down due to a malfunction! The bad actors managed to get to it! Now there is no one to
tell us whether we are have any security issues or are under extremely high traffic loads!

Quickly set up an AWS Web Application Firewall (WAF) to block this IP address before the bad actors get to any more devices! Ensure that this firewall is
attached to the Amazon CloudFront distribution too!
"""
TASK5_INDEX=50
TASK5_MARKDOWN=True


TASK5_COMPLETE_KEY="task5_complete"
TASK5_COMPLETE_LABEL="Firewall rule: Passed!"
TASK5_COMPLETE_VALUE="""
Great Job setting up the WAF rule. 

Here’s the current architecture:

![architecture_task5]({})
"""
TASK5_COMPLETE_INDEX=59
TASK5_COMPLETE_MARKDOWN=True


# TASK 6 - Final question
TASK6_KEY="task6"
TASK6_LABEL="Set up Alarm for metrics"
TASK6_VALUE="""
The worst is over for now, but without RoboVax screaming, no one will be able to tell us of any attacks. 

Let’s look at the metrics on how we can set up an alarm for future attacks.

This is a Cloudwatch monitoring dashboard of some metrics during heavy traffic load. Notice which metric is spiking!

![cloudwatch_metrics]({})

Pick the right metric that identifies high traffic load. In your AWS CloudWatch service dashboard, set up a CloudWatch alarm for this particular metric. Be sure to choose the metric for the correct Cloudwatch distribution!

To configure the alarm, measuring the average of this metric over 5 minutes. Set the alarm to be in alarm state using Anomaly detection, whenever RequestCount is Outside of the Band of threshold 2.

Notifications will be sent when the alarm state trigger is In Alarm.

Send notifications to an existing SNS topic. The SNS topic has been provisioned for you, called _SNS-topic-for-cloudwatch-alarm_.
"""
TASK6_INDEX=60
TASK6_MARKDOWN=True

TASK6_COMPLETE_KEY="task6_complete"
TASK6_COMPLETE_LABEL="CloudWatch alarm: Passed!"
TASK6_COMPLETE_VALUE="""
Great Job creating your CloudWatch alarm!
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

You configured CloudFront for your users to access your application quickly and reliably. When the bad actors tried to access your application, you identified them with CloudFront Logs and blocked them using WAF Rules. Lastly, you’ve set an alarm to detect future high traffic incidents so that you and your (ex-) boss, RoboVax can have a peace of mind.

Here is the final architecture you’ve achieved:

![architecture_final]({})

You've saved the day. You've completed this quest.
"""
QUEST_COMPLETE_INDEX=100
QUEST_COMPLETE_MARKDOWN=True
