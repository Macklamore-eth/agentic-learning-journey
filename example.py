import os
from openai import OpenAI
import truststore


truststore.inject_into_ssl()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)
print("Enter your prompt:")

prompt  = input()


try:
        response = client.responses.create(
            model="gpt-4.1",
            input=prompt,
            temperature=0.7
            )
        print(response.output_text)
except Exception as e:
        print("Something went wrong:", e)

