from groq import Groq

client = Groq(
    api_key="YOUR_GROQ_API_KEY"
)

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Program Ended.")
        break

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ],
        model="llama-3.1-8b-instant"
    )

    print("\nBot:", response.choices[0].message.content)