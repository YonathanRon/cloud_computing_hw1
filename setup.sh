#!/bin/bash
# Clone your application from Git
git clone https://github.com/YonathanRon/cloud_computing_hw1.git

mkdir temp
mv main.py temp/
sudo apt-get update -y
sudo apt-get upgrade -y

# Update system packages
sudo apt install python3-pip -y
sudo pip3 install --upgrade pip

# Install necessary packages
sudo pip3 install sqlite
sudo pip3 install fastapi
sudo pip3 install db
sudo pip3 install db-sqlite3
sudo pip3 install uvicorn


aws configure

# Change to your application directory
cd cloud_computing_hw1

# Start the FastAPI server
nohup uvicorn parking_lot:app --host 127.0.0.1 --port 8000 &
