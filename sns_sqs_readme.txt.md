# AWS SNS + SQS Email Alert Script

This Python script:
- Creates an SQS queue
- Creates an SNS topic
- Subscribes both the queue and your email to the topic
- Publishes a test message
- Reads the message from SQS

## Setup

1. Install dependencies:
```bash
pip install boto3
```

2. Configure AWS credentials:
```bash
aws configure
```

3. Run the script:
```bash
python sns_sqs_alert.py
```

📧 Check your inbox for a confirmation email from AWS SNS. Click to confirm the subscription!
