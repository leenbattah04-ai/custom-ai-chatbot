# Import the Groq SDK to communicate with the AI model
from groq import Groq

# Import dotenv to load environment variables from the .env file
from dotenv import load_dotenv

# Import os to access environment variables
import os

# Load variables from the .env file
load_dotenv()

# Create the Groq client using the API key from the .env file
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Conversation memory
# The system message defines the chatbot's behavior
history = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]


def chat_with_ai(user_message):
    """
    Sends the user's message to the AI model,
    stores the conversation history,
    and returns the assistant's reply.
    """

    # Add the user's message to the conversation history
    history.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    # Send the full conversation history to the model
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=history
    )

    # Extract the assistant's reply
    bot_reply = response.choices[0].message.content

    # Save the assistant's reply in memory
    history.append(
        {
            "role": "assistant",
            "content": bot_reply
        }
    )

    # Keep the system message and the latest 10 conversation messages
    if len(history) > 11:
        history[:] = [history[0]] + history[-10:]

    # Return the assistant's reply
    return bot_reply