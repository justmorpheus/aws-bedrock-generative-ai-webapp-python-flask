# AWS Bedrock Generative AI Web App using Python Flask and Amazon Bedrock


## Introduction

In this project, we create a generative AI-enabled web application from scratch using Python Flask. The application fetches cloud security tips using the `amazon.titan-text-premier-v1:0` model from Amazon Bedrock.

> This blog is an introduction to building a generative AI web application using Python Flask and Amazon Bedrock. The application provides a daily cloud security tip, but please note that detailed security aspects related to Amazon Bedrock will be covered in future posts. Stay tuned for more updates!

> This is part of workshop, hence Amazon Q was integrated with Vscode to develop this python app as per guidelines.

## Prerequisites

- An AWS account with access to Amazon Bedrock.
- Python installed on your system.
- Basic knowledge of Flask.

## Setup Instructions

1. **Clone the repository:**
    ```sh
    git clone https://github.com/s3curitydojolab/aws-bedrock-generative-ai-webapp-python-flask
    cd aws-bedrock-generative-ai-webapp-python-flask
    ```

2. **Set up a virtual environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```sh
    python3 -m pip install flask boto3 python-dotenv
    ```

4. **Set up environment variables:**
    - Create a `.env` file in the project root with the following content:
        ```
        AWS_ACCESS_KEY=your_access_key
        AWS_SECRET_KEY=your_secret_key
        ```

5. **Run the Flask application:**
    ```sh
    python app.py
    ```

6. **Open your browser and navigate to:**
    ```
    http://127.0.0.1:5000
    ```

## File Structure

```
aws-bedrock-generative-ai-webapp-python-flask/
├── app.py
├── templates/
│ └── index.html
├── .env
├── README.md
└── requirements.txt
```


## Usage

- The application provides a daily cloud security tip.
- Click the "Get Tip" button to fetch a new cloud security tip.

## Future Work

- Detailed security aspects related to Amazon Bedrock will be covered in future posts. Stay tuned for more updates!

## Credits

- [Amazon Q](https://aws.amazon.com/q/)
- [Amazon Bedrock](https://aws.amazon.com/bedrock)
- [AWS building-gen-ai-apps](https://catalog.workshops.aws/building-gen-ai-apps)
- [AWS GenAI Bootcamp | Day 3: AWS Bedrock & Foundational Models | Hosted by AWS UG Dehradun](https://www.youtube.com/watch?v=DjhcU4uZ2VQ)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
