# Import the chatbot function
from chatbot import chat_with_ai, history

print("🤖 AI Chatbot is running...")
print("Type 'exit' to quit.")
print("Type 'memory' to view conversation history.")
print("Type 'clear' to reset the conversation.\n")

while True:
    # Get user input
    user_message = input(" You: ")

    # Exit the chatbot
    if user_message.lower() == "exit":
        print("👋 Goodbye!")
        break

    # Display conversation memory
    elif user_message.lower() == "memory":
        print("\n========== Conversation Memory ==========")

        for message in history:
            if message["role"] == "system":
                continue
            elif message["role"] == "user":
                print(f" You: {message['content']}")
            elif message["role"] == "assistant":
                print(f"🤖 Bot: {message['content']}")

        print("**\n")
        continue

    # Clear conversation history
    elif user_message.lower() == "clear":
        history[:] = [history[0]]
        print(" Conversation memory cleared.\n")
        continue

    # Get AI response
    response = chat_with_ai(user_message)

    # Display AI response
    print(f"🤖 Bot: {response}\n")