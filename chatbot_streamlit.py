import streamlit as st

def get_response(user_input):
    user_input = user_input.lower()
    responses = {
        "hi": "Hello! How can I help you?",
        "hello": "Hi there!",
        "how are you": "I'm just a Python bot, but I'm doing great!",
        "what is your name": "I'm a simple Python chatbot!",
        "who created you": "I was created as a Python project example.",
        "bye": "Goodbye! Have a nice day!",
        "thanks": "You're welcome!",
        "help": "Try typing 'hello', 'what is your name', or 'bye'."
    }
    for key in responses:
        if key in user_input:
            return responses[key]
    return "Sorry, I didn't understand that."

st.title("💬 Simple Chatbot using Streamlit")

user_input = st.text_input("You:", "")

if user_input:
    bot_response = get_response(user_input)
    st.write("🤖 Bot:", bot_response)
