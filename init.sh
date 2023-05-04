#!/bin/bash
### This script shouls run on the dev station, it will install the prerequisites for creating a ec2 machine
### assuming that you have keyID, access key  on your environment vars
pip3 install boto3
sudo apt install awscli
export AWS_DEFAULT_REGION=eu-west-1
aws configure

# Clone your application from Git
echo "Cloning cloud_computing_hw1.git"
git clone https://github.com/YonathanRon/cloud_computing_hw1.git
cd cloud_computing_hw1
echo "Create ec2 Machine and run server inside..."
python3 create_ec2_instance.py