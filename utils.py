import os
from openai import OpenAI
OPENAI_API_TOKEN = os.getenv('OPENAI_API_KEY')

def call_openai_api(user_prompt,system_prompt,model="gpt-4o"):
    client = OpenAI(api_key=OPENAI_API_TOKEN)
    response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    )
    # print("response ",response.choices[0].message.content)
    return response.choices[0].message.content