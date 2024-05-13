import openai

from config import *

openai.api_key = API_KEY

while True:
    user_message = input()
    if user_message.lower() == "quit":
        break
    else:
        chat
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role"}
    ]
)
