import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

conversation =[{"role":"system", "content":"You are a very experienced Python teacher who explains the concept in a user friendly manner"}]

for i in range(5):
    qn = input("Ask ur python teacher a question")
    qndict = {"role":"user", "content":qn}
    conversation.append(qndict)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation
    )
    ans = response.choices[0].message.content
    ansdict = {"role":"assistant", "content":ans}
    conversation.append(ansdict)
    print('\n Teacher:', ans)
    