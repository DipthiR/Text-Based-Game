import requests
import random
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

def get_random_question():
    # API URL for fetching a random trivia question
    url = "https://opentdb.com/api.php?amount=1&type=multiple"
    
    # Send GET request to fetch the data
    response = requests.get(url)
    
    # Parse the response as JSON
    data = response.json()
    
    # Extract the question, correct answer, and options
    question = data['results'][0]['question']
    correct_answer = data['results'][0]['correct_answer']
    options = data['results'][0]['incorrect_answers'] + [correct_answer]
    
    # Shuffle the options to randomize their order
    random.shuffle(options)
    
    return question, options, correct_answer

def display_header():
    print(Fore.CYAN + Style.BRIGHT + "------------------------------------")
    print(Fore.GREEN + Style.BRIGHT + "   WELCOME TO THE TRIVIA GAME!")
    print(Fore.CYAN + Style.BRIGHT + "------------------------------------")

def ask_question():
    question, options, correct_answer = get_random_question()
    
    # Display the question and options with some formatting
    display_header()
    print(Fore.YELLOW + Style.BRIGHT + "\nQuestion: " + Fore.WHITE + question)
    print(Fore.MAGENTA + Style.BRIGHT + "Options:")
    
    for idx, option in enumerate(options, 1):
        print(Fore.LIGHTYELLOW_EX + f"{idx}. {option}")
    
    # Ask the user to choose an option
    user_answer = input(Fore.GREEN + "\nChoose the correct option (1-4): ")
    
    try:
        # Validate the user's choice and check if it's correct
        user_choice = int(user_answer)
        if options[user_choice - 1] == correct_answer:
            print(Fore.GREEN + Style.BRIGHT + "\nCorrect! Well done. 😊")
        else:
            print(Fore.RED + f"\nIncorrect! The correct answer was: {correct_answer}")
    
    except ValueError:
        print(Fore.RED + "Please enter a valid number between 1 and 4.")
    except IndexError:
        print(Fore.RED + "Please choose a valid option (1-4).")

def play_again():
    # Ask the user if they want to play again
    play = input(Fore.CYAN + "\nDo you want to play again? (yes/no): ").lower()
    if play == "yes":
        ask_question()
        play_again()
    else:
        print(Fore.MAGENTA + "\nThanks for playing! Goodbye! 👋")

# Start the game by asking the first question
ask_question()

# Ask if they want to play again
play_again()
