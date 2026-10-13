OpenAI = ("")
from openai import OpenAI

client = OpenAI(
    api_key="sk-proj-WLbHt50XDCPqwmbvNGS8usYHxqHZpMLnMichael-Jordan55555555555555555555555555555555"
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Ciao, chi sei?"
        }
    ]
)

print(response.choices[0].message.content)