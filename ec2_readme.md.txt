# AWS EC2 Instance Launcher

This Python script launches a new EC2 instance using the `boto3` AWS SDK.

## Features
- Launches a `t2.micro` EC2 instance
- Uses a custom AMI and key pair
- Adds a name tag to the instance

## Prerequisites
- Python 3
- `boto3` library installed
- AWS credentials configured (`aws configure`)
- An existing EC2 Key Pair and Security Group in your AWS account

## Usage

```bash
python launch_ec2_instance.py
