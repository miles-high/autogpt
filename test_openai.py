import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

# Check if the API key is loaded
if not openai.api_key:
    raise ValueError("OpenAI API key not found. Please set it in the .env file.")

try:
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',  # You can also use 'gpt-4' if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "A fantasy landscape with mountains and rivers."}
        ],
        max_tokens=150,
        temperature=0.7  # Optional: Controls the creativity of the response
    )

    # Extract and print the response content
    assistant_message = response.choices[0].message['content'].strip()
    print("Assistant:", assistant_message)

except openai.error.OpenAIError as e:
    print(f"An error occurred: {e}")

