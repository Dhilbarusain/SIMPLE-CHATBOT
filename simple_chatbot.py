def get_response(user_input):
    user_input = user_input.lower()

    # Dictionary of possible responses
    responses = {
        "hi": "Hello! How can I help you?",
        "hello": "Hi there!",
        "how are you": "I'm just a Python bot, but I'm doing great!",
        "what is your name": "I'm a simple Python chatbot!",
        "who created you": "I was created as a Python project example.",
        "bye": "Goodbye! Have a nice day!",
        "thanks": "You're welcome!",
        "help": "I can respond to basic greetings and questions. Try 'hello' or 'what is your name'."
    }

    # Match response
    for key in responses:
        if key in user_input:
            return responses[key]
    
    return "Sorry, I didn't understand that."

def chatbot():
    print("Bot: Hello! I’m a simple chatbot. Type 'bye' to exit.")
    while True:
        user = input("User: ")
        if user.lower() == "bye":
            print("Bot: Goodbye!")
            break
        response = get_response(user)
        print("Bot:", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
