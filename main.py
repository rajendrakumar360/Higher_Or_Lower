## Learn how to breakdown the bigger problem into smaller parts for coding convinience


#Display art
from art import logo,vs
from game_data import data
import random


def format_data(account):
    """Take the account data and return printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr} from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take the user's guess and the follower count and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess =="b"

print(logo)
score = 0
game_should_continue = True

account_b = random.choice(data)

while game_should_continue:
    #Generate a random account from data  from the game data
    account_a = account_b
    account_b = random.choice(data)

    # account_a = random.choice(data)   initially we have done this here
    # account_b = random.choice(data)
    if account_a == account_b:
        random.choice(data)


    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Print the account data into accountable format. WE have defined a function for this above

    # Ask user for a guess.
    guess = input("Who has more follower? Type 'A' or 'B': ").lower()

    #clear the screen
    print("\n" *20)
    print(logo)


    # Check is user is correct
    ## Get the follower count of each account.
    ## Use if statement to check if user is correct.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    #Give user feedback on their guess
    #Score keeping
    if is_correct:
        score += 1
        print(f"You are right! Current score {score}")
    else:
        print(f"Sorry, You are Wrong. Final Score: {score}")
        game_should_continue = False


# Make the game repeatable.( while loop lagakar humne game ko repeatabe bana diya)

# Making account at position B become the next account at position A.


