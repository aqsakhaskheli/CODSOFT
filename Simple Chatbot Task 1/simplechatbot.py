import nltk 
from nltk.chat.util import Chat
from nltk.chat.util import reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!! How can i assist you today?"]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!","I'm good, thanks for asking.", "I'm fine, how about you?"]
    ],
    [
        r"nice to meet you",
        ["Mee tooo!", "thank you"]
    ],
    [
        r"Thank you",
        ["Thank you for reaching out! Is there anything else i can assist you with?"]
    ],
    [
        r"(.*) your name?", 
        ["My name is ChatBot.", "You can call me ChatBot.", "I go by the name ChatBot."]
    ],
    [
        r"bye",
        ["Bye! Take care", "Goodbye! Have a great day!", "See you later!", "If you have any questions, feel free to ask. Otherwise, have a great day."]
    ],
]

# create a chat instance
chatbot = Chat(pairs, reflections)

# Start the conversation
print("Welcome to the ChatBot. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("MyChatBot:", response)
    if user_input.lower() == 'quit':
        break

