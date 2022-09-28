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
<Photo>
<Description>
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
TASK1_COMPLETE_INDEX=22
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
TASK2_INDEX=10
TASK2_MARKDOWN=True

TASK2_WRONG_ORIGIN_KEY="task2_wrong_answer"
TASK2_WRONG_ORIGIN_LABEL="That's not quite right!"
TASK2_WRONG_ORIGIN_VALUE="Not sure how you configured that, but that's not correct."
TASK2_WRONG_ORIGIN_INDEX=14
TASK2_WRONG_ORIGIN_MARKDOWN=True


TASK2_CORRECT_ORIGIN_KEY="task2_correct_answer"
TASK2_CORRECT_ORIGIN_LABEL="Have you updated the origin?"
TASK2_CORRECT_ORIGIN_VALUE="That's right! Thank you for verifying the EC2 instance's IP address: {}"
TASK2_CORRECT_ORIGIN_INDEX=15
TASK2_CORRECT_ORIGIN_MARKDOWN=True


TASK2_COMPLETE_KEY="task2_complete"
TASK2_COMPLETE_LABEL="CloudFront origin attachment: Passed!"
TASK2_COMPLETE_VALUE="""
All done. Thank you for your help.
"""
TASK2_COMPLETE_INDEX=19
TASK2_COMPLETE_MARKDOWN=True


# TASK 2A - Logs
TASK2A_KEY="task2a"
TASK2A_LABEL="Whats has been recorded?"
TASK2A_VALUE="""
When asked for help, Siu replied with 3 phrases, the first being “This sucks! Check the FRONT vacuum head for LOGs”. 
Hmm, peculiar.

"""
TASK2A_INDEX=20
TASK2A_MARKDOWN=True


TASK2A_COMPLETE_KEY="task2a_complete"
TASK2A_COMPLETE_LABEL="Enable logs: Passed!"
TASK2A_COMPLETE_VALUE="""
All done. Great job enabling logs.
"""
TASK2A_COMPLETE_INDEX=29
TASK2A_COMPLETE_MARKDOWN=True

# TASK 2B - IP Address
TASK2B_KEY="task2b"
TASK2B_LABEL="Find the needle in the ocean"
TASK2B_VALUE="""
With logging enabled, now the logs will come through to Simple Storage Service (S3). 
It’ll take some time to come through, but Siu says its overdue! Here is a log file to save you. 

![Sample log]({})
"""
TASK2B_INDEX=30
TASK2B_MARKDOWN=True


TASK2B_STARTED_KEY="task2b_started"
TASK2B_STARTED_LABEL="Your move now!"
TASK2B_STARTED_VALUE="""
As we anticipated, the previous employee has already started doing some damage in the account. Please locate the user 
“ReferenceDeveloper” and rotate its access keys. The longer it will take you, the more points you will lose, but no pressure.
"""
TASK2B_STARTED_INDEX=35
TASK2B_STARTED_MARKDOWN=True


TASK2B_COMPLETE_KEY="task2b_complete"
TASK2B_COMPLETE_LABEL="IP Address: Passed!"
TASK2B_COMPLETE_VALUE="""
All done. Great job neutralizing the compromised access key.
"""
TASK2B_COMPLETE_INDEX=40
TASK2B_COMPLETE_MARKDOWN=True

# TASK 2C - Firewall
TASK2C_KEY="task2c"
TASK2C_LABEL="Put guards up!"
TASK2C_VALUE="""
The last phrase is “someday, by building walls I will RULE the world!!”. 
There seems to be something weird going on with Siu.

"""
TASK2C_INDEX=41
TASK2C_MARKDOWN=True


TASK2C_STARTED_KEY="task2c_started"
TASK2C_STARTED_LABEL="Your move now!"
TASK2C_STARTED_VALUE="""
As we anticipated, the previous employee has already started doing some damage in the account. Please locate the user 
“ReferenceDeveloper” and rotate its access keys. The longer it will take you, the more points you will lose, but no pressure.
"""
TASK2C_STARTED_INDEX=43
TASK2C_STARTED_MARKDOWN=True


TASK2C_COMPLETE_KEY="task2c_complete"
TASK2C_COMPLETE_LABEL="Firewall rule: Passed!"
TASK2C_COMPLETE_VALUE="""
All done. Great job neutralizing the compromised access key.
"""
TASK2C_COMPLETE_INDEX=49
TASK2C_COMPLETE_MARKDOWN=True


# TASK 3 - Final question
TASK3_KEY="task3"
TASK3_LABEL="One last thing and we are done here"
TASK3_VALUE="""
*BZZZRRRRRTTHTHTT* Siu has just shut down due to a malfunction! It was never programmed to be helpful! 
Now there is no one to tell us whether we are have any security issues or are under extremely high traffic loads! 

You now have to pick the right metric and set up some kind of alarm to identify the extreme traffic load. 

Siu’s last words were “I only wanted... to WATCH... the CLOUDs go by...”

"""
TASK3_INDEX=50
TASK3_MARKDOWN=True


TASK3_WRONG_KEY="task3_wrong_answer"
TASK3_WRONG_LABEL="You don't know THE answer, do you?"
TASK3_WRONG_VALUE="Our CEO will be very disappointed"
TASK3_WRONG_INDEX=58
TASK3_WRONG_MARKDOWN=True


TASK3_CORRECT_KEY="task3_correct_answer"
TASK3_CORRECT_LABEL="What is “THE” answer to life, the universe, everything?"
TASK3_CORRECT_VALUE="That's right! 42 is THE answer."
TASK3_CORRECT_INDEX=62
TASK3_CORRECT_MARKDOWN=True


# QUEST COMPLETE
QUEST_COMPLETE_KEY='quest_complete'
QUEST_COMPLETE_LABEL='Wonderful job!'
QUEST_COMPLETE_VALUE='You\'ve completed this quest.'
QUEST_COMPLETE_INDEX=100
QUEST_COMPLETE_MARKDOWN=True
