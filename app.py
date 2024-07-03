from flask import Flask, render_template, request, jsonify
import boto3
import os

app = Flask(__name__)

# Load AWS credentials from environment variables, these are for demonstration.
AWS_ACCESS_KEY = "AKIA2SAMPLE" #changethis
AWS_SECRET_KEY = "0nu-SAMPLEKEY-rJpP" #changethis
AWS_REGION = 'us-east-1'  # Change to your region

# Disclaimer: Author or employer is not responsible for any damage due to this code.

# Initialize the Amazon Bedrock client
bedrock_client = boto3.client('bedrock-runtime',
                              aws_access_key_id=AWS_ACCESS_KEY,
                              aws_secret_access_key=AWS_SECRET_KEY,
                              region_name=AWS_REGION)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# API route to get cloud security tip
@app.route('/get_tip', methods=['GET'])
def get_tip():
    model_id = 'amazon.titan-text-premier-v1:0'
    prompt = "Provide a cloud security tip of the day"
    response = bedrock_client.converse(
        modelId=model_id,
        messages=[{"role": "user", "content": [{"text": prompt}]}]
    )
    tip = response['output']['message']['content'][0]['text']
    return jsonify({'tip': tip})

if __name__ == '__main__':
    app.run(debug=True)
