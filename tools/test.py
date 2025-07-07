from dotenv import load_dotenv
import os
import openai

# ✅ Load your custom-named env file
load_dotenv(dotenv_path="API_Key.env")

api_key = os.getenv("OPENAI_API_KEY")
print("Loaded API Key:", "✅" if api_key else "❌ NOT FOUND")

client = openai.OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, what can you do?"}
    ]
)

print(response.choices[0].message.content)
