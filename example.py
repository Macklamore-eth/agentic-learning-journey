import os
from openai import OpenAI
import truststore


truststore.inject_into_ssl()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

response = client.responses.create(
    model="gpt-4.1",
    input="Write a one-sentence bedtime story about a unicorn.",
   
)

print(response.output_text)