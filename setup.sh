#!/bin/bash
# Clone your application from Git
git clone https://github.com/YonathanRon/cloud_computing_hw1.git

sudo apt-get update -y
sudo apt-get upgrade -y

# Update system packages
sudo apt install python3-pip -y
pip3 install --upgrade pip

# Install necessary packages
pip3 install fastapi
pip3 install db
pip3 install db-sqlite3
pip3 install uvicorn


#aws configure
#
## Change to your application directory
cd cloud_computing_hw1
#
## Start the FastAPI server
python3 main.py
#
## Save the PID of the last command executed
#echo $! > server.pid
#
## Wait for the server to start
#sleep 3
#
## Print the logs
#tail -f nohup.out






