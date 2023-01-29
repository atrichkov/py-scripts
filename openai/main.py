import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
model = "text-davinci-003" # "code-davinci-002"

prompt = str(input('Ask me anything: '))

if prompt:
    print('Waiting for response...')

    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response.choices[0].text)
