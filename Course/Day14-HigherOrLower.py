import art
from instagram_data import data
import random


def get_celeb():
    return random.choice(data)


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def higher_or_lower(celeb_1, celeb_2):
    print(f"Compare A: {format_data(celeb_1)}.")
    print(art.vs)
    print(f"Against B: {format_data(celeb_2)}.")
    choice = input("Who has more followers? Type 'A' or 'B' ").upper()
    print('\n' * 20)
    print(art.logo_hol)
    if choice == 'A' and celeb_1["follower_count"] > celeb_2["follower_count"]:
        return True
    elif choice == 'B' and celeb_2["follower_count"] > celeb_1["follower_count"]:
        return True
    else:
        return False


score = 0
celeb_A = get_celeb()
celeb_B = get_celeb()
while celeb_A == celeb_B:
    celeb_B = get_celeb()
print(art.logo_hol)
while higher_or_lower(celeb_A, celeb_B):
    score += 1
    print(f"You are right! Current score: {score}")
    celeb_A = celeb_B
    celeb_B = get_celeb()
print(f"Sorry, that's wrong. Final score: {score}")