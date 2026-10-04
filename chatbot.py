# Simple AI Chatbot Project
# Author: Laltlanhlua65

import random

# Chatbot knowledge base
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm good! How about you?", "Doing great! Thanks for asking!"],
    "your name": ["I'm AI Chatbot, created by Laltlanhlua65!", "You can call me AI Bot!"],
    "bye": ["Goodbye! Have a great day!", "Bye! See you soon!"],
    "help": ["I can chat with you! Try saying hello, how are you, etc."],
    "default": ["Sorry, I didn't understand that.", "Can you say that again?", "I'm still learning!"]
}

def get_response(user_input):
    user_input = user_input.lower()

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return random.choice(responses["default"])

# Main Chat Loop
print("🤖 AI Chatbot - Type 'bye' to exit")
print("Bot: Hello! I'm your AI assistant!")

while True:
    user = input("You: ")
    if "bye" in user.lower():
        print("Bot:", random.choice(responses["bye"]))
        break

    bot_reply = get_response(user)
    print("Bot:", bot_reply)
