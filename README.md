<h1 align="center">💬 Basic Chatbot</h1>

<p align="center">
  <b>A simple rule-based chatbot written in Python.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/CodeAlpha-Task%204-6C47FF" alt="CodeAlpha">
  <img src="https://img.shields.io/badge/Level-Beginner-orange" alt="Level">
</p>

---

## 💡 About

This is **Task 4** of my [CodeAlpha](https://www.codealpha.tech) Python Programming Internship.
The chatbot follows simple rules: when you type a message it knows, it gives a ready-made reply.

## ✨ Features

- 👋 Asks for your **name** and uses it in its replies
- 🧠 Shares **fun facts** and asks **riddles** you can try to answer
- 🕒 Tells you the **time** and today's **date**
- 🪙 Can **flip a coin** for you
- 🔠 Not case-sensitive (`Hello` and `hello` both work)
- 🤷 Politely says when it does not understand
- 👋 Type `bye` to end the chat

## 🤖 What the Bot Understands

| You say | Bot replies |
|---------|-------------|
| `hello` / `hi` / `hey` | Hi, *your name*! |
| `how are you` | I'm fine, thanks! How about you? |
| `what is your name` | I'm PyBot, a simple Python chatbot. |
| `fact` | A random fun fact |
| `riddle` | Asks a riddle and checks your answer |
| `what is the time` | The current time |
| `what is the date` | Today's date |
| `flip a coin` | Heads or Tails |
| `thanks` | You're welcome! |
| `help` | A list of things to try |
| `bye` | Goodbye! (and the chat ends) |
| anything else | Sorry, I don't understand. |

## 🖥️ Example

```text
=== PyBot ===
Hi! I'm PyBot.
What is your name? Sara
Nice to meet you, Sara! Type 'help' to see what I can do.

Sara: hello
PyBot: Hi Sara!
Sara: fact
PyBot: Fun fact: Octopuses have three hearts.
Sara: riddle
PyBot: What has to be broken before you can use it?
Sara (your answer): egg
PyBot: Correct! Well done, Sara!
Sara: bye
PyBot: Goodbye, Sara! See you soon!
```

## ⚙️ Getting Started

**Requirements:** Python 3 (nothing else to install)

```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_BasicChatbot.git
cd CodeAlpha_BasicChatbot
python chatbot.py
```

> On some computers the command is `python3` instead of `python`.

## 🧠 Concepts Used

| Concept | Where it is used |
|---------|------------------|
| `if-elif` | Choosing the right reply |
| `random` | Picking a random fact, riddle or coin flip |
| `datetime` | Getting the current time and date |
| Functions | `get_reply()` returns the answer |
| Loops | Keeping the chat going until `bye` |
| Lists | Storing the facts and riddles |
| Input / output | Reading messages and printing replies |

## 📁 Project Structure

```text
CodeAlpha_BasicChatbot/
├── chatbot.py
└── README.md
```

---

## 👤 Author

**Your Name**
Python Programming Intern at [CodeAlpha](https://www.codealpha.tech)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/YOUR_PROFILE)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?logo=github&logoColor=white)](https://github.com/YOUR_USERNAME)

<p align="center">
  ⭐ If you liked this project, give it a star! ⭐<br>
  Made with ❤️ during the <b>CodeAlpha</b> internship
</p>
