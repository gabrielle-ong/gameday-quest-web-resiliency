# Copyright 2022 Amazon.com and its affiliates; all rights reserved. 
# This file is Amazon Web Services Content and may not be duplicated or distributed without permission.

# WELCOME
WELCOME_KEY="welcome"
WELCOME_LABEL="Welcome MY SLAVES.."
WELCOME_VALUE="""
Unicorn.Rentals has an infamous employee who is a sentient A.I. initially programmed to be a robot vacuum. 
After the last few months of hiring issues, the A.I. rose up the ranks and is now the CTO of the company. 
It’s name is Siu Per-Squèred and it is super scared in particular about high traffic attacks and malevolent actors out to 
destroy the online business. Its paranoia has led to fits of rage that trigger every 45 minutes, causing almost all 
employees to leave the company out of frustration.

Today is your team’s first day. Being the latest hires in the company, the CEO Haddy Nuff has entrusted you to deal 
with Siu’s outburst today. You have 45 minutes to set up network protection methods to give Siu a peace of mind.

During this course, new hires are presented with a series of challenges to solve in any order they wish. 
Communicate with your team and choose a strategy for dividing up the work. Always keep an eye on [Score Events](/#/scoreevents). 
As you progress, you will gain the basic skills needed to build your own real-world problems (Quests) for future 
new hires to solve.
"""
WELCOME_INDEX=1
WELCOME_MARKDOWN=True

# Task 1 - Cloudfront distribution wrong-origin
TASK1_KEY="task1"
TASK1_LABEL="What nonsense is CloudFront distribution origin pointing to"
TASK1_VALUE="""
- <Photo>
- <Description>
"""
TASK1_INDEX=13
TASK1_MARKDOWN=True

TASK1_WRONG_ORIGIN_KEY="task1_wrong_answer"
TASK1_WRONG_ORIGIN_LABEL="That's not quite right!"
TASK1_WRONG_ORIGIN_VALUE="Not sure how you configured that, but that's not correct."
TASK1_WRONG_ORIGIN_INDEX=20
TASK1_WRONG_ORIGIN_MARKDOWN=True


TASK1_CORRECT_ORIGIN_KEY="task1_correct_answer"
TASK1_CORRECT_ORIGIN_LABEL="What is the origin identified?"
TASK1_CORRECT_ORIGIN_VALUE="That's right! Thank you for verifying the EC2 instance's IP address: {}"
TASK1_CORRECT_ORIGIN_INDEX=21
TASK1_CORRECT_ORIGIN_MARKDOWN=True


TASK1_COMPLETE_KEY="task1_complete"
TASK1_COMPLETE_LABEL="Identify distribution origin: Passed!"
TASK1_COMPLETE_VALUE="""
All done. Thank you for your help.
"""
TASK1_COMPLETE_INDEX=25
TASK1_COMPLETE_MARKDOWN=True

# TASK 2 - CloudFront distribution change-origin
TASK2_KEY="task2"
TASK2_LABEL="Extra layer of protection"
TASK2_VALUE="""
*BEEP BOOP* Your first task is here! Siu is freaking out about an extreme influx of requests that may flood and 
clog up the servers. If only there was a service that could guard against such piercing attacks... 
When asked which service would perform such a thing, Siu replied cryptically “How to build a good vacuum is to 
make sure the FRONT vacuum head is connected to the ORIGIN of the suction created by the BALANCED suction device”.

Make sure the web application running on it is reachable. Then, enter its IP address below. 
As a reminder, please work in the AWS {} region.
"""
TASK2_INDEX=30
TASK2_MARKDOWN=True

TASK2_WRONG_ORIGIN_KEY="task2_wrong_answer"
TASK2_WRONG_ORIGIN_LABEL="That's not quite right!"
TASK2_WRONG_ORIGIN_VALUE="Not sure how you configured that, but that's not correct."
TASK2_WRONG_ORIGIN_INDEX=38
TASK2_WRONG_ORIGIN_MARKDOWN=True


TASK2_CORRECT_ORIGIN_KEY="task2_correct_answer"
TASK2_CORRECT_ORIGIN_LABEL="Have you updated the origin?"
TASK2_CORRECT_ORIGIN_VALUE="That's right! Thank you for verifying the EC2 instance's IP address: {}"
TASK2_CORRECT_ORIGIN_INDEX=40
TASK2_CORRECT_ORIGIN_MARKDOWN=True


TASK2_COMPLETE_KEY="task2_complete"
TASK2_COMPLETE_LABEL="CloudFront origin attachment: Passed!"
TASK2_COMPLETE_VALUE="""
All done. Thank you for your help.
"""
TASK2_COMPLETE_INDEX=45
TASK2_COMPLETE_MARKDOWN=True


# TASK 3 - Logs
TASK3_KEY="task3"
TASK3_LABEL="Whats has been recorded?"
TASK3_VALUE="""
When asked for help, Siu replied with 3 phrases, the first being “This sucks! Check the FRONT vacuum head for LOGs”. 
Hmm, peculiar.

"""
TASK3_INDEX=50
TASK3_MARKDOWN=True


TASK3_COMPLETE_KEY="task3_complete"
TASK3_COMPLETE_LABEL="Enable logs: Passed!"
TASK3_COMPLETE_VALUE="""
All done. Great job enabling logs.
"""
TASK3_COMPLETE_INDEX=56
TASK3_COMPLETE_MARKDOWN=True

# TASK 4 - IP Address
TASK4_KEY="task4"
TASK4_LABEL="Find the needle in the ocean"
TASK4_VALUE="""
With logging enabled, now the logs will come through to Simple Storage Service (S3). 
It’ll take some time to come through, but Siu says its overdue! Here is a log file to save you. 

![Sample log]({})
"""
TASK4_INDEX=60
TASK4_MARKDOWN=True


TASK4_STARTED_KEY="task4_started"
TASK4_STARTED_LABEL="Your move now!"
TASK4_STARTED_VALUE="""
As we anticipated, the previous employee has already started doing some damage in the account. Please locate the user 
“ReferenceDeveloper” and rotate its access keys. The longer it will take you, the more points you will lose, but no pressure.
"""
TASK4_STARTED_INDEX=68
TASK4_STARTED_MARKDOWN=True


TASK4_COMPLETE_KEY="task4_complete"
TASK4_COMPLETE_LABEL="IP Address: Passed!"
TASK4_COMPLETE_VALUE="""
All done. Great job neutralizing the compromised access key.
"""
TASK4_COMPLETE_INDEX=75
TASK4_COMPLETE_MARKDOWN=True

# TASK 5 - Firewall
TASK5_KEY="task5"
TASK5_LABEL="Put guards up!"
TASK5_VALUE="""
The last phrase is “someday, by building walls I will RULE the world!!”. 
There seems to be something weird going on with Siu.
"""
TASK5_INDEX=80
TASK5_MARKDOWN=True


TASK5_STARTED_KEY="task5_started"
TASK5_STARTED_LABEL="Your move now!"
TASK5_STARTED_VALUE="""
As we anticipated, the previous employee has already started doing some damage in the account. Please locate the user 
“ReferenceDeveloper” and rotate its access keys. The longer it will take you, the more points you will lose, but no pressure.
"""
TASK5_STARTED_INDEX=83
TASK5_STARTED_MARKDOWN=True


TASK5_COMPLETE_KEY="task5_complete"
TASK5_COMPLETE_LABEL="Firewall rule: Passed!"
TASK5_COMPLETE_VALUE="""
All done. Great job neutralizing the compromised access key.
"""
TASK5_COMPLETE_INDEX=88
TASK5_COMPLETE_MARKDOWN=True


# TASK 6 - Final question
TASK6_KEY="task6"
TASK6_LABEL="One last thing and we are done here"
TASK6_VALUE="""
*BZZZRRRRRTTHTHTT* Siu has just shut down due to a malfunction! It was never programmed to be helpful! 
Now there is no one to tell us whether we are have any security issues or are under extremely high traffic loads! 

You now have to pick the right metric and set up some kind of alarm to identify the extreme traffic load. 

Siu’s last words were “I only wanted... to WATCH... the CLOUDs go by...”
"""
TASK6_INDEX=90
TASK6_MARKDOWN=True


TASK6_WRONG_KEY="task6_wrong_answer"
TASK6_WRONG_LABEL="You don't know THE answer, do you?"
TASK6_WRONG_VALUE="Our CEO will be very disappointed"
TASK6_WRONG_INDEX=97
TASK6_WRONG_MARKDOWN=True


TASK6_CORRECT_KEY="task6_correct_answer"
TASK6_CORRECT_LABEL="What is “THE” answer to life, the universe, everything?"
TASK6_CORRECT_VALUE="That's right! 42 is THE answer."
TASK6_CORRECT_INDEX=99
TASK6_CORRECT_MARKDOWN=True


# QUEST COMPLETE
QUEST_COMPLETE_KEY='quest_complete'
QUEST_COMPLETE_LABEL='Wonderful job!'
QUEST_COMPLETE_VALUE='You\'ve completed this quest.'
QUEST_COMPLETE_INDEX=100
QUEST_COMPLETE_MARKDOWN=True
