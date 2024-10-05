# openai_helper.py
import openai
import os
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()

# Retrieve API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(question):
    openai.api_key = openai_api_key
    
    try:
        # Call OpenAI API using the new ChatCompletion method
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or use gpt-4 if you have access
            messages=[
                {"role": "system", "content": "You are a helpful tutor."},
                {"role": "user", "content": question}
            ]
        )
        # Extract and return the response text
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"
