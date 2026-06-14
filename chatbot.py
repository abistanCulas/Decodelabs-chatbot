Responses = {
    "hello" : "Hey there! How can I help you?",
    "hi" : "Hi! Ready to chat. What's on your mind?",
    "hey" : "Hey! What can i do for you today?",

    "who are you" : "I'm BotX - a deterministic rule-based chatbot built.",
    "what are you" : "I'm a rule baseed AI chatbot.",

    "how are you" : "I'm good ",
    "what is ai" : "AI is the simulation of human intelligence by machines using logic, data, and learning.",
    "what is ml" : "Machine Learning is AI that learns patterns from data instead of folowing hard code rules.",
    "tell me a joke" : "Why do progrmmers prefer dark mode? Because light atteacts bugs! ",
    
    "help" : "I understood: hello,hi,hey,who are you,what are you,how are you, what is ai,what is ml,tell me a joke, and 'quit' to exit.",

    "bye" : "Goodbye Come back when you need me.",
    "goodbye" : "See you later! Keep building."

}

EXIT_COMMANDS = {"quit","exit","bye","goodbye"}

def get_clean_input(prompt: str= "You: "):
    raw_input = input(prompt)
    clean_input=raw_input.lower().strip()
    return clean_input

def get_response(user_input: str):
    return Responses.get(user_input,"I don't understan that yet.Type 'help' to see what I know." )


def display_response(response:str):
    print(f"BotX : {response}")

def run_chatbot():
    print("=" * 52)
    print(" BotX - Rule Based AI chatbot ")
    print(" Type 'help' for commands.Type 'quit' to exit. ")
    print("="*52 + "\n")

    while True:
        user_input=get_clean_input()

        if not user_input:
            continue

        if user_input in EXIT_COMMANDS:
            display_response(Responses.get(user_input,"Goodbye!"))
            print("---Session ended---")
            break

        response = get_response(user_input)
        display_response(response)

if __name__=="__main__":
    run_chatbot()
