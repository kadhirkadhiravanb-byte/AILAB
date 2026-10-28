"""Simple rule-based AI chatbot."""


def chatbot(user_input: str) -> str:
    text = user_input.lower()
    words = text.split()

    if "hello" in words or "hi" in words:
        return "Hello! How can I help you?"
    elif "how are you" in text:
        return "I am fine! Thank you."
    elif "name" in text:
        return "I am an AI chatbot."
    elif "college" in text:
        return "College is a place for learning and development."
    elif "ai" in words:
        return "AI stands for Artificial Intelligence."
    elif "thank" in text:
        return "You're welcome!"
    elif "bye" in text:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I don't understand your question."


def main() -> None:
    print("===== AI CHATBOT =====")
    print("Type 'bye' to exit.")

    while True:
        user = input("You: ")
        print("Bot:", chatbot(user))

        if "bye" in user.lower():
            break


