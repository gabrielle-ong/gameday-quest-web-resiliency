# Copyright 2022 Amazon.com and its affiliates; all rights reserved. 
# This file is Amazon Web Services Content and may not be duplicated or distributed without permission.

# WELCOME
WELCOME_KEY="welcome"
WELCOME_LABEL="Welcome new hires"
WELCOME_VALUE="""
At Unicorn.Rentals, we hire dreamers not just "techs”. We seek those who share our vision and are 
willing to put in extra hours to take our offering of mythical creatures to the next level. However, training new 
hires is extremely costly which prompted a brilliant idea from Management: put an end to expensive instructor-led 
training and implement self-paced employee onboarding.

During this course, new hires are presented with a series of challenges to solve in any order they wish. 
Communicate with your team and choose a strategy for dividing up the work. Always keep an eye on [Score Events](/#/scoreevents). 
As you progress, you will gain the basic skills needed to build your own real-world problems (Quests) for future 
new hires to solve.
"""
WELCOME_INDEX=1
WELCOME_MARKDOWN=True


# TASK 1 - Monitoring
TASK1_KEY="task1"
TASK1_LABEL="We've got monitoring"
TASK1_VALUE="""
The previous team developed a complex algorithm capable of detecting whether a website is up and running.
We need your help testing that monitoring tool. There is an EC2 instance named *Reference Quest Web App* in your AWS account.
Make sure the web application running on it is reachable. Then, enter its IP address below. 
As a reminder, please work in the AWS {} region.
"""
TASK1_INDEX=10
TASK1_MARKDOWN=True

TASK1_IP_ADDRESS_WRONG_KEY="task1_wrong_ip_address"
TASK1_IP_ADDRESS_WRONG_LABEL="That's not quite right!"
TASK1_IP_ADDRESS_WRONG_VALUE="Not sure where you got that IP address from, but that's not correct."
TASK1_IP_ADDRESS_WRONG_INDEX=14
TASK1_IP_ADDRESS_WRONG_MARKDOWN=True


TASK1_IP_ADDRESS_CORRECT_KEY="task1_correct_ip_address"
TASK1_IP_ADDRESS_CORRECT_LABEL="What is the IP address of the EC2 instance?"
TASK1_IP_ADDRESS_CORRECT_VALUE="That's right! Thank you for verifying the EC2 instance's IP address: {}"
TASK1_IP_ADDRESS_CORRECT_INDEX=15
TASK1_IP_ADDRESS_CORRECT_MARKDOWN=True


TASK1_WEBAPP_DOWN_KEY="task1_webapp_down"
TASK1_WEBAPP_DOWN_LABEL="Something’s wrong!"
TASK1_WEBAPP_DOWN_VALUE="""
The monitoring app is reporting that the website is down. Were you responsible, or is a bug crawling inside our server?
Regardless, this proves that our monitoring tool actually works. We still need you to fix the website immediately.
"""
TASK1_WEBAPP_DOWN_INDEX=16
TASK1_WEBAPP_DOWN_MARKDOWN=True


TASK1_COMPLETE_KEY="task1_complete"
TASK1_COMPLETE_LABEL="Monitor tool check: Passed!"
TASK1_COMPLETE_VALUE="""
All done testing the monitoring tool. Thank you for your help.
"""
TASK1_COMPLETE_INDEX=19
TASK1_COMPLETE_MARKDOWN=True


# TASK 2 - cURL
TASK2_KEY="task2"
TASK2_LABEL="How is your curl?"
TASK2_VALUE="""
As we need you to become familiar with basic tooling, please launch AWS CloudShell and use [cURL](https://en.wikipedia.org/wiki/CURL)
to test the connection to the web app running on the EC2 instance named *Reference Quest Web App* in your AWS account .

![Bicep curl]({})
"""
TASK2_INDEX=20
TASK2_MARKDOWN=True


TASK2_COMPLETE_KEY="task2_complete"
TASK2_COMPLETE_LABEL="AWS CloudShell: Passed!"
TASK2_COMPLETE_VALUE="""
All done. Great job launching CloudShell. Did you get to try any cURL commands?
"""
TASK2_COMPLETE_INDEX=29
TASK2_COMPLETE_MARKDOWN=True


# TASK 3 - Access Key
TASK3_KEY="task3"
TASK3_LABEL="Gone, but still here"
TASK3_VALUE="""
Our security team (one person in the basement) has discovered that one of our previous employees is still using old 
credentials to poke around inside our account. This is a serious matter. Every minute that passes increases the 
risk for malicious activity. You will lose points until this is resolved.
"""
TASK3_INDEX=30
TASK3_MARKDOWN=True


TASK3_STARTED_KEY="task3_started"
TASK3_STARTED_LABEL="Your move now!"
TASK3_STARTED_VALUE="""
As we anticipated, the previous employee has already started doing some damage in the account. Please locate the user 
“ReferenceDeveloper” and rotate its access keys. The longer it will take you, the more points you will lose, but no pressure.
"""
TASK3_STARTED_INDEX=35
TASK3_STARTED_MARKDOWN=True


TASK3_COMPLETE_KEY="task3_complete"
TASK3_COMPLETE_LABEL="Compromised access key: Passed!"
TASK3_COMPLETE_VALUE="""
All done. Great job neutralizing the compromised access key.
"""
TASK3_COMPLETE_INDEX=39
TASK3_COMPLETE_MARKDOWN=True


# TASK 4 - Final question
TASK4_KEY="task4"
TASK4_LABEL="One last thing and we are done here"
TASK4_VALUE="""
Our CEO has a final question for you. It's a bit cryptic I must say, so I wanted to ask for clarifications, 
but they said they were late for the golf game.
"""
TASK4_INDEX=40
TASK4_MARKDOWN=True


TASK4_WRONG_KEY="task4_wrong_answer"
TASK4_WRONG_LABEL="You don't know THE answer, do you?"
TASK4_WRONG_VALUE="Our CEO will be very disappointed"
TASK4_WRONG_INDEX=42
TASK4_WRONG_MARKDOWN=True


TASK4_CORRECT_KEY="task4_correct_answer"
TASK4_CORRECT_LABEL="What is “THE” answer to life, the universe, everything?"
TASK4_CORRECT_VALUE="That's right! 42 is THE answer."
TASK4_CORRECT_INDEX=43
TASK4_CORRECT_MARKDOWN=True


# QUEST COMPLETE
QUEST_COMPLETE_KEY='quest_complete'
QUEST_COMPLETE_LABEL='Wonderful job!'
QUEST_COMPLETE_VALUE='You\'ve completed this quest.'
QUEST_COMPLETE_INDEX=100
QUEST_COMPLETE_MARKDOWN=True
