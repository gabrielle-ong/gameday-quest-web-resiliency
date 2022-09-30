# Copyright 2022 Amazon.com and its affiliates; all rights reserved. 
# This file is Amazon Web Services Content and may not be duplicated or distributed without permission.

#!/bin/bash

QUEST_ROOT_DIR=${PWD}
BUILD_QUEST_NAME=web_resiliency_quest
BUILD_QUEST_ID=4a841f49-25c9-43c2-bf9d-da2b97142027
BUILD_QUEST_BUCKET_NAME=${QDK_ASSETS_BUCKET}                              # when deploying locally
#BUILD_QUEST_BUCKET_NAME=ee-assets-prod-us-east-1                         # when deploying to production
# Include trailing / if a value is defined!
BUILD_QUEST_BUCKET_PREFIX=web_resiliency_quest/                           # when deploying locally
#BUILD_QUEST_BUCKET_PREFIX=modules/9c0e89820b864addaed45ec2f5440379/v5/   # when deploying to production

QUEST_ARTIFACTS_ZIP=gdQuests-${BUILD_QUEST_ID}-quest-artifacts.zip        # don't change

if [[ -z "${AWS_GAMEDAY_PROFILE}" ]]; then
  PROFILE_ARGUMENT=""
  echo Not using AWS_GAMEDAY_PROFILE
else
  PROFILE_ARGUMENT="--profile $AWS_GAMEDAY_PROFILE"
fi


echo -e "BUILD_QUEST_BUCKET_NAME=" ${BUILD_QUEST_BUCKET_NAME}
echo -e "BUILD_QUEST_BUCKET_PREFIX=" ${BUILD_QUEST_BUCKET_PREFIX}
echo -e "\n Working from " ${QUEST_ROOT_DIR}

# Create the build directory if it doesn't exist
mkdir -p build

########################################################
## Pipeline Assets                                    ##
## Zip up all quest assets (with no dependencies)     ##
## and upload to S3. The quest artifacts zip will     ##
## be used to seed CodeCommit upon it creation        ##
## Note: the zip cannot exceed 6MB!                   ##
########################################################
echo -e "\nZipping up the quest artifacts......"
cd ${QUEST_ROOT_DIR}
zip -q9r - . > ${QUEST_ROOT_DIR}/build/${QUEST_ARTIFACTS_ZIP} . -x \*artifacts\* \*build\* central_lambda_source/.venv/**\* team_lambda_source/.venv/**\*


############################
## Upload to S3           ##
############################
echo -e "\nUploading Quest artifacts to S3 for seeding CodeCommit"
cd ${QUEST_ROOT_DIR}/build
aws s3 cp ${QUEST_ARTIFACTS_ZIP} s3://${BUILD_QUEST_BUCKET_NAME}/${BUILD_QUEST_BUCKET_PREFIX}${BUILD_QUEST_ID}/${QUEST_ARTIFACTS_ZIP} ${PROFILE_ARGUMENT}


echo -e "\nUploading additional Quest artifacts to S3"
cd ${QUEST_ROOT_DIR}
aws s3 cp artifacts/images/sample_log.png s3://${BUILD_QUEST_BUCKET_NAME}/${BUILD_QUEST_BUCKET_PREFIX}${BUILD_QUEST_ID}/sample_log.png ${PROFILE_ARGUMENT}
aws s3 cp artifacts/images/architecture_task0.png s3://${BUILD_QUEST_BUCKET_NAME}/${BUILD_QUEST_BUCKET_PREFIX}${BUILD_QUEST_ID}/architecture_task0.png ${PROFILE_ARGUMENT}
aws s3 cp artifacts/images/architecture_task2.png s3://${BUILD_QUEST_BUCKET_NAME}/${BUILD_QUEST_BUCKET_PREFIX}${BUILD_QUEST_ID}/architecture_task2.png ${PROFILE_ARGUMENT}
aws s3 cp artifacts/images/architecture_task3.png s3://${BUILD_QUEST_BUCKET_NAME}/${BUILD_QUEST_BUCKET_PREFIX}${BUILD_QUEST_ID}/architecture_task3.png ${PROFILE_ARGUMENT}
aws s3 cp artifacts/images/architecture_task5.png s3://${BUILD_QUEST_BUCKET_NAME}/${BUILD_QUEST_BUCKET_PREFIX}${BUILD_QUEST_ID}/architecture_task5.png ${PROFILE_ARGUMENT}
aws s3 cp artifacts/images/cf_console_task1.png s3://${BUILD_QUEST_BUCKET_NAME}/${BUILD_QUEST_BUCKET_PREFIX}${BUILD_QUEST_ID}/cf_console_task1.png ${PROFILE_ARGUMENT}
aws s3 cp artifacts/images/cloudwatch_metrics.png s3://${BUILD_QUEST_BUCKET_NAME}/${BUILD_QUEST_BUCKET_PREFIX}${BUILD_QUEST_ID}/cloudwatch_metrics.png ${PROFILE_ARGUMENT}
aws s3 cp artifacts/images/robot_queue_image.png s3://${BUILD_QUEST_BUCKET_NAME}/${BUILD_QUEST_BUCKET_PREFIX}${BUILD_QUEST_ID}/robot_queue_image.png ${PROFILE_ARGUMENT}
aws s3 cp artifacts/images/architecture_final.png s3://${BUILD_QUEST_BUCKET_NAME}/${BUILD_QUEST_BUCKET_PREFIX}${BUILD_QUEST_ID}/architecture_final.png ${PROFILE_ARGUMENT}  


echo Complete: $(date)