import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["I'm a chatbot. You can call me ChatGPT_byLagan.",]
    ],
    [
        r"how are you",
        ["I'm good, thank you!",]
    ],
    [
        r"(.*) (good|well|fine)",
        ["That's great to hear!", "Nice to hear that.",]
    ],
    [
        r"quit",
        ["Bye, take care. Have a great day!",]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that. Can you please rephrase?",]
    ],
    [
        r"tell me a joke",
        ["Sure, here's one: Why don't scientists trust atoms? Because they make up everything!",]
    ],
    [
        r"how old are you",
        ["I don't have an age. I'm just a computer program.",]
    ],
    [
        r"where are you located",
        ["I exist in the virtual world, so I don't have a physical location.",]
    ],
    [
        r"favorite color",
        ["I don't have a favorite color. I'm not programmed to have preferences.",]
    ],
    [
        r"thank you",
        ["You're welcome! If you have more questions, feel free to ask.",]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! If you ever want to chat again, I'll be here.",]
    ],
]

chatbot = Chat(pairs, reflections)

def simple_chat():
    print("Hello! I'm your chatbot. You can type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Bye, take care. Have a great day!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

simple_chat()
