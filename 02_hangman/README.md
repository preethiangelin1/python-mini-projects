# 🕹️ Hangman Game (Python)

A simple **command-line Hangman game** built using Python.  
This project is beginner-friendly and focuses on core Python concepts like loops, conditionals, functions, lists, and modules.

---

## 📌 Project Description

Hangman is a word-guessing game where the player tries to guess a hidden word one letter at a time.  
For every wrong guess, the player loses a life. The game ends when:

- ✅ The player guesses all letters correctly (Win)
- ❌ The player runs out of lives (Lose)

---

## 🛠️ Features

- Random word selection
- ASCII art for Hangman stages
- Life tracking system (6 lives)
- Repeated letter detection
- Clear win/lose messages

---

## 📂 Project Structure

```text
hangman/
│
├── main.py            # Main game logic
├── hangman_art.py     # Hangman ASCII art & logo
├── hangman_words.py   # List of words
└── README.md          # Project documentation
