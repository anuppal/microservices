from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)

# AWS credentials and region
aws_access_key_id = 'your_access_key_id'
aws_secret_access_key = 'your_secret_access_key'
aws_region = 'your_aws_region'

# SNS Topic ARN
sns_topic_arn = 'your_sns_topic_arn'

# Create an SNS client
sns_client = boto3.client('sns', region_name=aws_region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

@app.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.get_json()
    message = data.get('message')
    subject = data.get('subject', 'Notification Subject')

    response = sns_client.publish(
        TopicArn=sns_topic_arn,
        Message=message,
        Subject=subject
    )

    return jsonify({"MessageId": response['MessageId']})

if __name__ == '__main__':
    app.run(debug=True)
