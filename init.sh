#!/bin/bash
### This script shouls run on the dev station, it will install the prerequisites for creating a ec2 machine
### assuming that you have keyID, access key  on your environment vars
pip3 install boto3
sudo apt install awscli

aws configure