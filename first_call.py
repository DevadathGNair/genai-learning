import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Read the API key and create the client
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Send a prompt to the language model
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful finance assistant."
        },
        {
            "role": "user",
            "content": "What are 3 key metrics to evaluate a company's financial health?"
        }
    ]
)

# Print the model's response
"""print("*********Printing response*********")
print(response)
print("*********Printing response.choices*********")
print(response.choices)
print("*********Printing response.choices[0]*********")
print(response.choices[0])
print("*********Printing response.choices[0].message*********")
print(response.choices[0].message)
print("*********Printing response.choices[0].message.content*********")"""
print(response.choices[0].message.content)
