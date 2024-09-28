# frontend/chatbot.py

import requests

def chat():
    print("Welcome to the Hint Chatbot! Ask me a question about learning.")
    while True:
        question = input("You: ")
        if question.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        
        response = requests.post("http://localhost:8000/get_hint", json={"question": question})
        if response.status_code == 200:
            print("Chatbot:", response.json()["hint"])
        else:
            print("Chatbot: Sorry, I couldn't generate a hint.")

if __name__ == "__main__":
    chat()
