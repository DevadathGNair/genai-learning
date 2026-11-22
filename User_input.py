import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

qn = input("Ask ur python teacher a qn?")
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"system",
         "content":"You are a very experienced Python teacher who explains the concept in a user friendly manner"},
        {"role":"user",
         "content":qn}
    ]
)

ans = response.choices[0].message.content
print("\n Teacher:", ans)