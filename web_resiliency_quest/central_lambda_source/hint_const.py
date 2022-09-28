# Copyright 2022 Amazon.com and its affiliates; all rights reserved. 
# This file is Amazon Web Services Content and may not be duplicated or distributed without permission.

# HINT STATUS
STATUS_OFFERED="OFFERED"
STATUS_DISPLAYED="DISPLAYED"

# TASK 1 HINTS
TASK1_HINT1_KEY="task1_hint1"
TASK1_HINT1_LABEL="Need help identifying origin?"
TASK1_HINT1_DESCRIPTION="If you're stuck, click on the Reveal Hint button to get some guidance"
TASK1_HINT1_VALUE="Take a look at the origin that has been attached to CloudFront distribution"
TASK1_HINT1_INDEX=16
TASK1_HINT1_COST=200

# TASK 2 HINTS
TASK2_HINT1_KEY="task2_hint1"
TASK2_HINT1_LABEL="Need help?"
TASK2_HINT1_DESCRIPTION="If you're stuck, click on the Reveal Hint button to get some guidance"
TASK2_HINT1_VALUE="Click into your Amazon CloudFront distribution to edit its “Origins” to point to the Application Load Balancer (ALB). "
TASK2_HINT1_INDEX=26
TASK2_HINT1_COST=500


# # TASK 2 HINTS
# TASK2_HINT1_KEY="task2_hint1"
# TASK2_HINT1_LABEL="Having difficulty finding CloudShell?"
# TASK2_HINT1_DESCRIPTION="If you're stuck, click on the Reveal Hint button to get some guidance"
# TASK2_HINT1_VALUE="Ensure that you have navigated to your team's AWS Console. Then click on 'Services' in the upper left and find 'CloudShell'."
# TASK2_HINT1_INDEX=27
# TASK2_HINT1_COST=200

# TASK 3 HINTS
TASK3_HINT1_KEY="task3_hint1"
TASK3_HINT1_LABEL="Need help?"
TASK3_HINT1_DESCRIPTION="If you're stuck, click on the Reveal Hint button to get some guidance"
TASK3_HINT1_VALUE="Go to your Amazon CloudFront Distribution and edit its settings. Thereafter, look for the “standard logging” checkbox which you will the link up to your Amazon S3 bucket."
TASK3_HINT1_INDEX=37
TASK3_HINT1_COST=500

# TASK 4 HINTS
TASK4_HINT1_KEY="task4_hint1"
TASK4_HINT1_LABEL="Need help?"
TASK4_HINT1_DESCRIPTION="If you're stuck, click on the Reveal Hint button to get some guidance"
TASK4_HINT1_VALUE="Look at what the source IP address is."
TASK4_HINT1_INDEX=46
TASK4_HINT1_COST=500

# TASK 5 HINTS
TASK5_HINT1_KEY="task5_hint1"
TASK5_HINT1_LABEL="Need help?"
TASK5_HINT1_DESCRIPTION="If you're stuck, click on the Reveal Hint button to get some guidance"
TASK5_HINT1_VALUE="""
Using the IP address identified in Task 4, create an IP Set on AWS WAF. 

Once created, go to the Web ACL that has already been pre-created for you. 

Under Rules, go to “Add my own rules and rule groups” to create a rule that blocks the IP Set created earlier. 

Once done, go to “Associated AWS resources” and add your Amazon CloudFront distribution. This will attach the AWS WAF rule to your Amazon CloudFront distribution.
"""
TASK5_HINT1_INDEX=57
TASK5_HINT1_COST=500


# TASK 6 HINTS
TASK6_HINT1_KEY="task6_hint1"
TASK6_HINT1_LABEL="Need help?"
TASK6_HINT1_DESCRIPTION="If you're stuck, click on the Reveal Hint button to get some guidance"
TASK6_HINT1_VALUE="""
On the graph, there seems to be a spike in the metric called “CloudFront - Request”.

Head to Amazon CloudWatch to set up an alarm with these metrics so that we will always be notified of any large spike in traffic.
"""
TASK6_HINT1_INDEX=67
TASK6_HINT1_COST=500
