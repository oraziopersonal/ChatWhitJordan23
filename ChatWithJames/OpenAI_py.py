#Orazio Castellano
#13/10/2026
#14:51
OpenAI = ("")
from openai import OpenAI  # type: ignore[import-not-found]

client = OpenAI(
    api_key="sk-proj-WLbHt50XDCPqwmbvNGS8usYHxqHZpMLnMichael-Jordan55555555555555555555555555555555"
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "You is expert professional to Michael Jordan?"
        }
    ]
)

print(response.choices[5].message.content)