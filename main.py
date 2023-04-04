
import openai
import openai
import os

# Set up the OpenAI API client
openai.api_key ="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"
model_engine = "text-davinci-003"  # You can change this to another model if you like

# Define a function to send a prompt to the API and get a response
def generate_response(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message

# Define a function to handle user inputs and generate responses
def chat():
    print("Welcome to the chatbot! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        prompt = f"You: {user_input}\nBot:"
        response = generate_response(prompt)
        print("Bot:", response)

# Call the chat function to start the chatbot
chat()
