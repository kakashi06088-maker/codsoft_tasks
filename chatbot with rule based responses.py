# Rule-Based Chatbot

def chatbot(user_input):
    # Convert input to lowercase for easier matching
    user_input = user_input.lower().strip()

    # Greeting rules
    if user_input in ["hi", "hello", "hey"]:
        return "Hello! How can I help you?"

    # Name rule
    elif "your name" in user_input or "who are you" in user_input:
        return "I am a simple rule-based chatbot."

    # How are you rule
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."

    # Help rule
    elif "help" in user_input:
        return "Sure! You can ask me about my name, the weather, or say hello."

    # Weather rule
    elif "weather" in user_input:
        return "I'm not connected to live weather data, but I hope it's nice outside!"

    # Thank you rule
    elif "thank" in user_input or "thanks" in user_input:
        return "You're welcome!"

    # Goodbye rule
    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day."

    # Default response
    else:
        return "Sorry, I don't understand that. Please try asking something else."


# Main chatbot loop
print("Chatbot: Hello! I'm a rule-based chatbot.")
print("Chatbot: Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    response = chatbot(user_input)
    print("Chatbot:", response)

    if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
        break
