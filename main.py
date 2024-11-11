from game_data import data
from art import logo,vs
import random

def format_data(account):
    """Takes the account data and prints the printable format"""
    account_name = account["Name"]
    account_descr = account["description"]
    account_country = account["country"]

def check_answer(user_guess,a_follower,b_follower):
    """Take a user's guess and the follower counts and returns if they got it right. """
    if a_follower > b_follower:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

print(logo)
score = 0
should_continue = True
account_b = random.choice(data)
while should_continue:
    # Generate a random account from the game data
    # Making account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {account_a}")
    print(vs)
    print(f"Against B = {account_b}")
    # Ask the user to guess

    guess = input("Who has more followers type 'A' or 'B' ").lower()

    print("\n" * 20)
    print(logo)

    # Check if the user is correct.
    # - Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess,a_follower_count,b_follower_count)
    # Give user feedback on their guess
    #  Score keeping
    if is_correct:
        score += 1
        print(f"You're right 🥳, Current Score {score}")
    else:
        print(f"Sorry you got the answer wrong ☹️. Final score: {score}.")
        should_continue = False


