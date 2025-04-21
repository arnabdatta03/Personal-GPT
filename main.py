import os
import google.generativeai as genai
from dotenv import load_dotenv

API_KEY = ''
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")
chat=model.start_chat()


# Loop for user interaction
while True:
    user_input = input("USER: ")
    if user_input.lower() in ['exit', 'quit']:
        print("GPT: Goodbye! Have a great day.")
        break

    response = chat.send_message(user_input)
    print("GPT:", response.text)
