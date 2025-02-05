import random
import art


def check_guess(player_guess, actual_number):
    if player_guess == actual_number:
        print(f"You got it! The answer was {player_guess}")
        return True
    elif player_guess < actual_number:
        print("Too low.")
        return False
    else:
        print("Too high.")
        return False


print(art.logo_gtn)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
correct_number = random.randint(1, 100)
attempts = 10
is_game_over = False
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
else:
    print("Invalid input.")
    attempts = 0
while attempts > 0:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if check_guess(guess, correct_number):
        attempts = -1
    else:
        attempts -= 1
        print('Guess again.')
if attempts == 0:
    print("You've run out of guesses. Refresh the page to run again.")

