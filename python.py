import nltk
from nltk.chat.util import Chat, reflections


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["You can call me Chatbot."]
    ],
    [
        r"how are you ?",
        ["I'm good. How about you?"]
    ],
    [
        r"sorry (.*)",
        ["No problem", "Don't worry"]
    ],
    [
        r"I (.*)(good|well|fine)",
        ["That's great to hear"]
    ],
    [
        r"quit",
        ["Bye-bye, take care!"]
    ],
]

def chatbot():
    print("Hello! I'm a chatbot. You can start chatting with me.")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print("Bye-bye, take care!")
            break
        print(chat.respond(user_input))


if __name__ == "__main__":
    nltk.download("punkt")  #pip install nltk
    chatbot()
