import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.environ['OPENAI_API_KEY']

def askAQuestion():
    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "Write a haiku about recursion in programming."
            }
        ]
    )

    print(completion.choices[0].message)

if __name__ == "__main__":
    askAQuestion()
