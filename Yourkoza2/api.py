import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()


def gemini(prompt):
    genai.configure(api_key=os.environ["API_KEY"])
    model = genai.GenerativeModel('gemini-pro')

    responses = model.generate_content(prompt)
    return responses.text


while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye", "goodbye"]:
        break
    response = gemini(user_input)
    print("Chatbot: ", response)
