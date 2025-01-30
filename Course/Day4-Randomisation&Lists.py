import random

# random_integer = random.randint(1, 10)
# print(random_integer)
#
# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(1,10)
# print(random_float)
#
# if random.randint(0, 1) == 0:
#     print("Heads")
# else:
#     print("Tails")

# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# print(friends[random.randint(0, 4)])


# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game = [rock, paper, scissors]
try:
    player_choice = game[int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))]
    print(player_choice)
    computer_choice = random.choice(game)
    print("Computer Choose:")
    print(computer_choice)
    if player_choice == computer_choice:
        print("It's a draw.")
    elif player_choice == rock and computer_choice == scissors:
        print("You Won.")
    elif player_choice == scissors and computer_choice == paper:
        print("You Won.")
    elif player_choice == paper and computer_choice == rock:
        print("You Won.")
    else:
        print("You Lost.")
except IndexError:
    print("You entered an invalid number.")




