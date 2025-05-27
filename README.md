# Gemini Function Calling with Python 🤖

This project demonstrates how to integrate **Google's Gemini 2.0 Flash** model with **function calling** capability in Python. The model dynamically interprets natural language prompts and routes them to appropriate functions such as weather lookup, joke generation, currency conversion, task management, blog post creation, and more.

---

## 📁 Project Structure

```
├── main.py # Main script to run the application
├── function_schema.py # JSON schemas defining function interfaces
├── .gitignore
├── README.md
└── functions/ # Folder containing all function implementations
├── init.py
├── weather.py
├── jokes.py
├── calculator.py
├── currency_converter.py
├── todo.py
├── post_creator.py
├── get_post_by_title.py
└── random_user.py
```


---

## 🚀 Features

- 🔌 Gemini 2.0 Flash API Integration
- 📚 Function Calling via natural language
- ⚡ Dynamic function mapping (no `if-elif` statements)
- 📦 Modular function design
- 🧠 Intelligent API assistant using Gemini
- 🔄 Easily extendable with more tools

---

## 🛠️ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/gemini-function-calling.git
cd gemini-function-calling

```
pip install -r requirements.txt
```

```
python main.py
```