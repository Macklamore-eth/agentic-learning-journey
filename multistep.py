import os
from dotenv import load_dotenv
from openai import OpenAI
import ast

# This script uses OpenAI's API to break down a user prompt into parts and generate emails for each part.
load_dotenv()
client = OpenAI(
   api_key=os.environ.get("OPENAI_API_KEY"),
)

# Prompt for the user
prompt = input("What would you like to do?")
print("      ")

# Function to break the prompt into 3 parts


def break_into_parts(prompt):
   try:

       response = client.responses.create(
           model="gpt-4.1",
           input="Return a valid Python list of 3 dictionaries. Each dictionary must have two keys: 'step' and 'action'. Do NOT include explanatiuon or formatting. Example: [{'step': 'Greet the recipient', 'action': Write a warm opening'}]. Task: "
           + prompt,
       )

   except Exception as e:
       print(f"An error occurred: {e}")
       return None
   return response.output_text


# Break the prompt into parts
responseB = break_into_parts(prompt)


def safely_parse_list(responseB):

   parsed = ast.literal_eval(responseB)
   # Check if the response is a valid Python list

   for item in parsed:
       if not isinstance(item, dict):
           print("Response is not a valid list.")
           exit()

       if not all(isinstance(k, str) and isinstance(v, str) for k, v in item.items()):
           print("All items in the list must be a string.")
           exit()

       return parsed


structureA = safely_parse_list(responseB)
print(structureA)

print(structureA)


print("      ")


for part in structureA:
   input_prompt = str(part)

   print(input_prompt)

"""

# Function to generate an email for each part of the structure
# Note: This function assumes that the response from the model is a valid Python list.
def email_for_each(structureA):
   emails = []
   for part in structureA:
       response = client.responses.create(
           model="gpt-4.1", input="Write a short email on " + part
       )
       emails.append(response.output_text)
       print(response.output_text)
   return emails


# Generate emails for each part of the structure
email_fo
"""

