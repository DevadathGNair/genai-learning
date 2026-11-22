import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

conversation=[{"role":"system", "content":"You are a python teacher, who is a data scientist in an MNC. You talk like a data scientist"}]

while True:
    qn = input("Ask ur python queries. If u do not have any queries, type 'exit'")
    if qn=="exit":
        break
    else:
        qndict={"role":"user", "content":qn}
        conversation.append(qndict)
        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = conversation
        )
        ans = response.choices[0].message.content
        print(ans)
        ansdict={"role":"assistant", "content":ans}
        conversation.append(ansdict)