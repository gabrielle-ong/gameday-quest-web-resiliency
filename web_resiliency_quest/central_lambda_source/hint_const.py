# Copyright 2022 Amazon.com and its affiliates; all rights reserved. 
# This file is Amazon Web Services Content and may not be duplicated or distributed without permission.

# HINT STATUS
STATUS_OFFERED="OFFERED"
STATUS_DISPLAYED="DISPLAYED"

# TASK 1 HINTS
TASK1_HINT1_KEY="task1_hint1"
TASK1_HINT1_LABEL="Need help identifying origin?"
TASK1_HINT1_DESCRIPTION="If you're stuck, click on the Reveal Hint button to get some guidance"
TASK1_HINT1_VALUE="Hmm taking the easy way eh? Visiting the link should bring you to www.amazon.com"
TASK1_HINT1_INDEX=16
TASK1_HINT1_COST=200

# TASK 2 HINTS
TASK2_HINT1_KEY="task2_hint1"
TASK2_HINT1_LABEL="Need help?"
TASK2_HINT1_DESCRIPTION="If you're stuck, click on the Reveal Hint button to get some guidance"
TASK2_HINT1_VALUE="""
1. Click into your Amazon CloudFront distribution and select the “Origins” tab.

2. Edit the defaultOrigin and change origin domain to point to your Elastic Load Balancer (ELB).

"""
TASK2_HINT1_INDEX=26
TASK2_HINT1_COST=500

# TASK 3 HINTS
TASK3_HINT1_KEY="task3_hint1"
TASK3_HINT1_LABEL="Need help?"
TASK3_HINT1_DESCRIPTION="If you're stuck, click on the Reveal Hint button to get some guidance"
TASK3_HINT1_VALUE="""
1. Go to your Amazon CloudFront Distribution and edit its settings.

2. Check the “Standard logging” checkbox which you will then link it to your Amazon S3 bucket.

"""
TASK3_HINT1_INDEX=37
TASK3_HINT1_COST=500

# TASK 4 HINTS
TASK4_HINT1_KEY="task4_hint1"
TASK4_HINT1_LABEL="Need help?"
TASK4_HINT1_DESCRIPTION="If you're stuck, click on the Reveal Hint button to get some guidance"
TASK4_HINT1_VALUE="Look at what the x-forwarded-for IP address is."
TASK4_HINT1_INDEX=46
TASK4_HINT1_COST=500

# TASK 5 HINTS
TASK5_HINT1_KEY="task5_hint1"
TASK5_HINT1_LABEL="Need help?"
TASK5_HINT1_DESCRIPTION="If you're stuck, click on the Reveal Hint button to get some guidance"
TASK5_HINT1_VALUE="""
1. Using the IP address identified in Task 4, create an IP Set on AWS WAF. To include the malicious IP address, input '52.23.186.156/32'.

2. Once created, go to the Web ACL that has already been pre-created for you. 

3. Go to the Rules tab, click "Add rules" and select “Add my own rules and rule groups”. 

4. Select rule type of "IP Set" and choose the IP Set that was created earlier.

5. Ensure that the Action is "Block".

"""
TASK5_HINT1_INDEX=57
TASK5_HINT1_COST=500


# TASK 6 HINTS
TASK6_HINT1_KEY="task6_hint1"
TASK6_HINT1_LABEL="Need help?"
TASK6_HINT1_DESCRIPTION="If you're stuck, click on the Reveal Hint button to get some guidance"
TASK6_HINT1_VALUE="""
1. On the graph, there seems to be a spike in the metric called “CloudFront - Request”.

2. Head to Amazon CloudWatch, expand "Alarms" in the menu on the left. Select "All alarms" and choose "Create alarm".

3. Click "Select Metric". Select or search for "CloudFront", then "Per-Distribution Metrics".

4. There may be many metrics listed under "Browse". Search for your CloudFront distribution ID, and the "Requests" metric. If you do not know your CloudFront distribution ID, visit the CloudFront dashboard to check the distribution ID.

5. Select this metric. Under Specify metric and conditions, select "Anomaly detection" whever requests is "Outside of the band" of "2"

6. Under Configure actions, select the alarm state trigger to be "In alarm". Send a notification to an "existing SNS topic", and select "SNS-topic-for-cloudwatch-alarm". You can leave the endpoints empty.

7. Name your alarm, press Next. Lastly, preview your settings and select "Create alarm".
"""
TASK6_HINT1_INDEX=67
TASK6_HINT1_COST=500
