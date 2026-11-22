import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

personas =["You are a strict financial analyst. Respond ONLY with bullet points and numbers.", "You are a friendly teacher. Use simple analogies and examples.","You are a risk manager. Always highlight what could go wrong."]
question = "Should I invest in tech stocks right now?"

"""for i, persona in enumerate(personas, 1):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"system", "content":persona}, {"role":"user", "content":question}]
    )
    print(f"----Persona {i}----\n{response.choices[0].message.content}")"""


persona = personas[0]

for i in range(3):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": persona},
            {"role": "user", "content": question}
        ], temperature=1.0,
        max_tokens=100
    )

    print(f"\n--- Run {i+1} ---")
    print(response.choices[0].message.content)
    print(response.choices[0].finish_reason)