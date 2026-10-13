from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Tell me about Michael Jordan.",
        }
    ],
)

print(response.choices[0].message.content)
