# Copyright 2022 Amazon.com and its affiliates; all rights reserved. 
# This file is Amazon Web Services Content and may not be duplicated or distributed without permission.

# WELCOME
WELCOME_KEY="welcome"
WELCOME_LABEL="Welcome minions.."
WELCOME_VALUE="""
When you’re ready, line up and brace yourselves.....

Here’s the gist of it:

<IMAGE OF ROBOTS WHISPERING PSST>

“Psst hey! You’re new here right? I’m sure you’re wondering whats going on, here’s a quick note of what’s been going on, take this!”

**The note reads:**

* Unicorn.Rentals has an infamous employee who is a sentient A.I. initially programmed to be a robot vacuum. 
* After the last few months of hiring issues, the A.I. rose up the ranks and is now the CTO of the company. 
* It’s name is RoboVax-9000 and it is extremely paranoid about high traffic attacks and bad actors out to destroy the business. 


“Today is your team’s first day. Being the latest hires in the company, the CEO has entrusted you to deal with
RoboVax’s paranoia today. You have 45 minutes to set up network protection methods to give it a peace of mind.”


*During this course, new hires are presented with a series of challenges to solve in any order they wish.
Communicate with your team and choose a strategy for dividing up the work. Always keep an eye on Score Events (https://d7f46jhe0vm23.cloudfront.net/#/scoreevents).
As you progress, you will gain the basic skills needed to build your own real-world problems (Quests) for future new hires to solve.
**Please work in the AWS us-east-1 region.** *

<ARCHITECTURE DIAGRAM>
"""
WELCOME_INDEX=1
WELCOME_MARKDOWN=True

# Task 1 - Cloudfront distribution wrong-origin
TASK1_KEY="task1"
TASK1_LABEL="What nonsense is CloudFront distribution origin pointing to?"
TASK1_VALUE="""
*BEEP BOOP* - Your first task from RoboVax is here! It seems like our customers are complaining that they are unable to
connect to the application. Quick! Find out which origin (URL) our content delivery network (CDN) is currently pointing to.
The CDN service web page should look something like this:

<CLOUDFRONT CONSOLE>
"""
TASK1_INDEX=10
TASK1_MARKDOWN=True

TASK1_WRONG_ORIGIN_KEY="task1_wrong_answer"
TASK1_WRONG_ORIGIN_LABEL="That's not quite right!"
TASK1_WRONG_ORIGIN_VALUE="Not sure how you configured that, but that's not correct."
TASK1_WRONG_ORIGIN_INDEX=14
TASK1_WRONG_ORIGIN_MARKDOWN=True


TASK1_CORRECT_ORIGIN_KEY="task1_correct_answer"
TASK1_CORRECT_ORIGIN_LABEL="What is the origin identified?"
TASK1_CORRECT_ORIGIN_VALUE="That's right! Thank you for verifying the EC2 instance's IP address: {}"
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
TASK2_LABEL="Now correctly configure the CloudFront distribution to your ALB (dropdown)"
TASK2_VALUE="""
The job is not done yet! Connect Amazon CloudFront to the correct origin in order for the application to work!
It seems like the correct origin is the application load balancer that is fronting your Amazon EC2 instances. 
"""
TASK2_INDEX=20
TASK2_MARKDOWN=True

TASK2_WRONG_ORIGIN_KEY="task2_wrong_answer"
TASK2_WRONG_ORIGIN_LABEL="That's not quite right!"
TASK2_WRONG_ORIGIN_VALUE="Not sure how you configured that, but that's not correct."
TASK2_WRONG_ORIGIN_INDEX=24
TASK2_WRONG_ORIGIN_MARKDOWN=True


TASK2_CORRECT_ORIGIN_KEY="task2_correct_answer"
TASK2_CORRECT_ORIGIN_LABEL="Have you updated the origin?"
TASK2_CORRECT_ORIGIN_VALUE="That's right! Thank you for verifying the EC2 instance's IP address: {}"
TASK2_CORRECT_ORIGIN_INDEX=25
TASK2_CORRECT_ORIGIN_MARKDOWN=True


TASK2_COMPLETE_KEY="task2_complete"
TASK2_COMPLETE_LABEL="CloudFront origin attachment: Passed!"
TASK2_COMPLETE_VALUE="""
All done. Thank you for your help.
"""
TASK2_COMPLETE_INDEX=28
TASK2_COMPLETE_MARKDOWN=True


# TASK 3 - Logs
TASK3_KEY="task3"
TASK3_LABEL="What has been recorded? (Enable Amazon CloudFront logging to Amazon S3)"
TASK3_VALUE="""
Phew! That was close, our customers can access the application now.

*BEEP BOOP* - RoboVax has sounded the alarm! We are under attack by hackers!!! We need to find out where the attack is coming from,
but currently we are not able to track the traffic going through Amazon CloudFront. Find a way to start logging the traffic
going through Amazon CloudFront! 
"""
TASK3_INDEX=30
TASK3_MARKDOWN=True


TASK3_COMPLETE_KEY="task3_complete"
TASK3_COMPLETE_LABEL="Enable logs: Passed!"
TASK3_COMPLETE_VALUE="""
All done. Great job enabling logs.
"""
TASK3_COMPLETE_INDEX=39
TASK3_COMPLETE_MARKDOWN=True

# TASK 4 - IP Address
TASK4_KEY="task4"
TASK4_LABEL="Get malicious IP attacker address"
TASK4_VALUE="""
With logging enabled, now the logs will be recorded in the Amazon Simple Storage Service (S3) bucket. Well done!
However, the hackers are still trying to take down our Unicorn.Rentals application! We managed to obtain the generated log
file of network traffic.

![Sample log]({})
"""
TASK4_INDEX=40
TASK4_MARKDOWN=True

TASK4_IP_ADDRESS_WRONG_KEY="task4_wrong_ip_address"
TASK4_IP_ADDRESS_WRONG_LABEL="That's not quite right!"
TASK4_IP_ADDRESS_WRONG_VALUE="Not sure where you got that IP address from, but that's not correct."
TASK4_IP_ADDRESS_WRONG_INDEX=44
TASK4_IP_ADDRESS_WRONG_MARKDOWN=True

TASK4_IP_ADDRESS_CORRECT_KEY="task4_correct_ip_address"
TASK4_IP_ADDRESS_CORRECT_LABEL="What is the IP address?"
TASK4_IP_ADDRESS_CORRECT_VALUE="That's right! Thank you for verifying the IP address."
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
*BZZZRRRRRTTHTHTT* RoboVax has just shut down due to a malfunction! The hackers managed to get to it! Now there is no one to
tell us whether we are have any security issues or are under extremely high traffic loads!

Quickly set up a firewall to block this IP address before the hackers get to any more devices! Ensure that this firewall is
attached to the Amazon CloudFront distribution too!
"""
TASK5_INDEX=50
TASK5_MARKDOWN=True


TASK5_COMPLETE_KEY="task5_complete"
TASK5_COMPLETE_LABEL="Firewall rule: Passed!"
TASK5_COMPLETE_VALUE="""
All done. Great job neutralizing the compromised access key.
"""
TASK5_COMPLETE_INDEX=59
TASK5_COMPLETE_MARKDOWN=True


# TASK 6 - Final question
TASK6_KEY="task6"
TASK6_LABEL="Set up Alarm for metrics"
TASK6_VALUE="""
The worst is over for now, but without RoboVax, no one will be able to tell us of any attacks. 

Let’s look at the metrics on how we can set up an alarm for that.

<IMAGE OF METRICS CHART>

You now have to pick the right metric and set up an alarm to identify the extreme traffic load.
"""
TASK6_INDEX=60
TASK6_MARKDOWN=True

TASK6_COMPLETE_KEY="task6_complete"
TASK6_COMPLETE_LABEL="CloudWatch alarm: Passed!"
TASK6_COMPLETE_VALUE="""
All done. Great job neutralizing the compromised access key.
"""
TASK6_COMPLETE_INDEX=69
TASK6_COMPLETE_MARKDOWN=True


# TASK6_WRONG_KEY="task6_wrong_answer"
# TASK6_WRONG_LABEL="You don't know THE answer, do you?"
# TASK6_WRONG_VALUE="Our CEO will be very disappointed"
# TASK6_WRONG_INDEX=97
# TASK6_WRONG_MARKDOWN=True


# TASK6_CORRECT_KEY="task6_correct_answer"
# TASK6_CORRECT_LABEL="What is “THE” answer to life, the universe, everything?"
# TASK6_CORRECT_VALUE="That's right! 42 is THE answer."
# TASK6_CORRECT_INDEX=99
# TASK6_CORRECT_MARKDOWN=True


# QUEST COMPLETE
QUEST_COMPLETE_KEY='quest_complete'
QUEST_COMPLETE_LABEL='Wonderful job!'
QUEST_COMPLETE_VALUE='You\'ve completed this quest.'
QUEST_COMPLETE_INDEX=100
QUEST_COMPLETE_MARKDOWN=True
