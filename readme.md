# Creating an EC2 Instance and Deploying a Server
This program uses the AWS SDK for Python (Boto3) to create and deploy a parking lot management server on an Amazon EC2 instance. 
### Prerequisites
Before running the program, you need to install the following:
* Python 3.x
* pip3
* AWS CLI

#### To install the required Python packages, run the following command:
```bash
pip3 install boto3
```

#### To install the AWS CLI, run the following command:

```bash
sudo apt install awscli
```
### Configuration
#### To configure the AWS CLI, run the following command and enter your AWS Access Key ID, Secret Access Key, default region name, and default output format (if you dont have AWS credentials set up in your environment variables.):
region should be eu-west-1

```bash
aws configure
```

### Usage
#### To create an EC2 instance and deploy the server, follow these steps:

Clone the application from Git:

```bash
git clone https://github.com/YonathanRon/cloud_computing_hw1.git
cd cloud_computing_hw1
python3 create_ec2_instance.py
```
Run the Python script that creates the EC2 instance and deploys the server:
The script will create a dedicated security group and key pair for the new instance if they don't already exist, and will then launch the instance and deploy the server on port 8000. Once the instance is launched, you can access the server by navigating to its public IP address in a web browser.

Note: make sure to terminate the instance when you are done using it to avoid incurring charges.