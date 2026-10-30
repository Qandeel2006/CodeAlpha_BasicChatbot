# Task 4: Basic Chatbot
import random
from datetime import datetime

# fun facts the bot can tell
facts = [
    "Honey never spoils. Edible honey has been found in ancient Egyptian tombs!",
    "Octopuses have three hearts.",
    "A day on Venus is longer than a year on Venus.",
    "Bananas are berries, but strawberries are not.",
    "A group of flamingos is called a flamboyance.",
    "Sharks have been around longer than trees.",
]

# riddles: [question, answer]
riddles = [
    ["What has a face and two hands but no arms or legs?", "clock"],
    ["What gets wetter the more it dries?", "towel"],
    ["What has to be broken before you can use it?", "egg"],
    ["What can you catch but never throw?", "cold"],
    ["I have cities but no houses, and rivers but no water. What am I?", "map"],
]

def get_reply(message, name):
    message = message.lower().strip()
    words = message.split()   # split the message into single words

    if "how are you" in message:
        return "I'm fine, thanks! How about you, " + name + "?"
    elif "hello" in words or "hi" in words or "hey" in words:
        return "Hi " + name + "!"
    elif "your name" in message:
        return "I'm PyBot, a simple Python chatbot."
    elif "fact" in words:
        return "Fun fact: " + random.choice(facts)
    elif "riddle" in words:
        riddle = random.choice(riddles)
        print("PyBot:", riddle[0])
        answer = input(name + " (your answer): ").lower()
        if riddle[1] in answer:
            return "Correct! Well done, " + name + "!"
        else:
            return "Not quite. The answer is: " + riddle[1]
    elif "joke" in words:
        return "I'm not good at jokes, but I know riddles and fun facts! Try 'riddle' or 'fact'."
    elif "time" in words:
        return "The time is " + datetime.now().strftime("%I:%M %p")
    elif "date" in words or "today" in words:
        return "Today is " + datetime.now().strftime("%A, %d %B %Y")
    elif "coin" in words:
        return "I flipped a coin and got " + random.choice(["Heads", "Tails"]) + "!"
    elif "thanks" in words or "thank" in words:
        return "You're welcome, " + name + "!"
    elif "help" in words:
        return "Try: hello, how are you, fact, riddle, what is the time, what is the date, flip a coin, or bye."
    elif "bye" in words:
        return "Goodbye, " + name + "! See you soon!"
    else:
        return "Sorry, I don't understand. Type 'help' to see what I can do."
print("=== PyBot ===")
print("Hi! I'm PyBot.")
name = input("What is your name? ")
print("Nice to meet you, " + name + "! Type 'help' to see what I can do.\n")
while True:
    user = input(name + ": ")
    reply = get_reply(user, name)
    print("PyBot:", reply)
    if "bye" in user.lower().split():
        break