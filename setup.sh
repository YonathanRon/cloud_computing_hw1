#!/bin/bash

# Update system packages
sudo yum update -y

# Install necessary packages
sudo yum install -y python3-pip sqlite

# Upgrade pip
sudo -H pip3 install --upgrade pip

# Install required Python packages
sudo -H pip3 install fastapi uvicorn

# Clone your application from Git
git clone https://github.com/your_username/your_repo.git

# Change to your application directory
cd your_repo

# Start the FastAPI server
nohup uvicorn your_app:app --host 0.0.0.0 --port 80 &