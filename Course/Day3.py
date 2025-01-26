# # number = int(input("Enter a number: "))
# # if number % 2 == 0:
# #     print("Even Number")
# # else:
# #     print("Odd Number")
#
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print("You have selected an incorrect option")
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# else:
#     print("You have selected an incorrect option")
# if extra_cheese == "Y":
#     bill += 1
# else:
#     print("You have selected an incorrect option")
# print(f"Your final bill is: ${bill}.")
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     '"=.|                  |
|___________________|__"=._o'"-._        '"=.______________|___________________
          |                '"=._o'"=._      _'"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
          |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
 _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
|                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
|___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
Welcome to Treasure Island.
Your mission is to find the treasure.''')
road = input('''You're at a cross road. Where do you want to go?
      Type "left" or "right"\n''').lower()
if road == "left":
    lake = input('''You've come to a lake. There is an island in the middle of the lake.
  Type "wait" to wait for a boat. Type "swim" to swim across.\n''').lower()
    if lake == "wait":
        house = input('''You arrive at the island unharmed. There is a house with 3 doors.
  One red, one yellow and one blue. Which colour do you choose?\n''').lower()
        if house == "red":
            print("It's a room full of fire. Game Over.")
        elif house == "blue":
            print("You enter a room of beasts. Game Over.")
        elif house == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("Invalid choice. Game Over!!!")
    elif lake == "swim":
        print("You get attacked by an angry trout. Game Over.")
    else:
        print("Invalid choice. Game Over!!!")
elif road == "right":
    print("You fell into a hole. Game Over.")
else:
    print("Invalid choice. Game Over!!!")
