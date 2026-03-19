from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Explain ADAS perception in autonomous driving in a concise and structured way, suitable for a technical interview"}
    ]
)

print(response.choices[0].message.content)