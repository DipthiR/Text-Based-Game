# Text-Based-Game
## Trivia Game
A simple trivia game where users are prompted with a random question and multiple-choice answers. The game checks if the user's answer is correct and provides feedback. The user is then asked if they would like to play again.

## Features:
Fetches a random trivia question from the Open Trivia Database API.

Displays the question and randomized answer options.

Lets the user choose an answer and checks if it's correct.

Provides feedback on whether the answer was correct or incorrect.

Asks the user if they want to play again after each question.

## Prerequisites:
Python 3.x

requests library

colorama library for colored terminal output.

## Installation:
Install Python 3.x if you haven't already: Download Python.

Install the required libraries:

pip install requests colorama
## Usage:
Clone or download this repository.

Navigate to the directory containing the script.

Run the game by executing the Python script:

python trivia_game.py
The game will display a trivia question and options in your terminal.

Choose an answer by typing the number corresponding to your option.

After each question, you'll be asked if you want to play again.

## Example of Running the Game:

------------------------------------
   WELCOME TO THE TRIVIA GAME!
------------------------------------
Question: What is the capital of France?
Options:
1. Berlin
2. Paris
3. Rome
4. Madrid

Choose the correct option (1-4): 2

Correct! Well done. 😊

Do you want to play again? (yes/no): yes

------------------------------------
   WELCOME TO THE TRIVIA GAME!
------------------------------------
Question: What is the smallest prime number?
Options:
1. 0
2. 1
3. 2
4. 3

Choose the correct option (1-4): 3

Incorrect! The correct answer was: 2

Do you want to play again? (yes/no): no

Thanks for playing! Goodbye! 👋
## Game Flow:
When you start the game, you are presented with a random trivia question and multiple-choice answers.

You can select the answer by typing the corresponding number (1-4).

The game will tell you if your answer is correct or incorrect and will display the correct answer if you were wrong.

After each question, you'll be asked if you want to play again. If you enter "yes", the game will ask another question. If you enter "no", the game will exit with a friendly farewell message.
