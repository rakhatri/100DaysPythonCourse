import random
import art


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(u_score, c_score):
    if c_score == u_score:
        return "It's a draw."
    elif c_score == 0:
        return "Lose, opponent has Blackjack."
    elif u_score == 0:
        return "You win with Blackjack"
    elif u_score > 21:
        return "You lose."
    elif c_score > 21:
        return "Opponent went over. You win."
    elif u_score > c_score:
        return "You win."
    else:
        return "You lose."


def play_game():
    print(art.logo_blackjack)
    user_cards = []
    computer_cards = []
    is_game_over = False
    computer_score = -1
    user_score = -1

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\tYour cards: {user_cards}, current score: {user_score}")
        print(f"\tComputer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"\tYour final hand: {user_cards}, final score: {user_score}")
    print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print('\n' * 20)
    play_game()


# def play_blackjack():
#
#     check_score(user_cards)
#     if not game_over:
#         draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
#         if draw_card == 'y':
#             user_cards.append(deal_card())
#             check_score(user_cards)
#         else:
#             while calculate_score(computer_cards) < 17:
#                 computer_cards.append(deal_card())
#
#             compare(user_score, computer_score)
#
#
# play_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
# while play_choice == 'y':
#     play_blackjack()


# player_cards = []
# computer_cards = []
# player_score = 0
# computer_score = 0
# is_game_still_on = True
# wanna_play = True
#
# def has_ace(hand):
#     for card in hand:
#         if card == 11:
#             return True
#         else:
#             return False
# def print_hand(player_hand, computer_hand):
#     player_hand_score = sum(player_hand)
#     computer_hand_score = sum(computer_hand)
#     print(f"\tYour final hand: {player_cards}, final score: {player_hand_score}")
#     print(f"\tComputer's final hand: {computer_cards}, current score: {computer_hand_score}")
#
# play_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
# if play_choice == 'y':
#     wanna_play = True
# else:
#     print("Thank you for playing. Have a nice day.")
#     wanna_play = False
#
# print(art.logo)
# for draw in range(0, 2):
#     player_cards.append(random.choice(cards))
#     computer_cards.append(random.choice(cards))
# while is_game_still_on:
#     player_score = sum(player_cards)
#     computer_score = sum(computer_cards)
#     print(f"\tYour cards: {player_cards}, current score: {player_score}")
#     print(f"\tComputer's first card: {computer_cards[0]}")
#     if computer_score == 21:
#         print_hand(player_cards, computer_cards)
#         print("Computer win with Blackjack. You lose.")
#         is_game_still_on = False
#     elif player_score == 21:
#         print("You win with Blackjack.")
#         is_game_still_on = False
#     else:
#         if player_score > 21:
#             if has_ace(player_cards):
#                 if player_score - 10 > 21:
#                     print_hand(player_cards, computer_cards)
#                     print('You lose.')
#                     is_game_still_on = False
#     hit_or_stay = input("Type 'y' to get another card, type 'n' to pass: ")
#     if hit_or_stay == 'y':
#         player_cards.append(random.choice(cards))
#         computer_cards.append(random.choice(cards))
#         if player_score == computer_score:
#             print_hand(player_cards, computer_cards)
#             print("It's a draw.")
#             is_game_still_on = False
#         elif player_score > computer_score:
#             print_hand(player_cards, computer_cards)
#             print("You win.")
#             is_game_still_on = False
#         else:
#             print_hand(player_cards, computer_cards)
#             print("You lose.")
#             is_game_still_on = False
#     else:
#         while computer_score < 17:
#             computer_cards.append(random.choice(cards))
#             computer_score = sum(computer_cards)
#         if computer_score > 21:
#             print_hand(player_cards, computer_cards)
#             print("You Win.")
#             is_game_still_on = False
#         elif player_score == computer_score:
#             print_hand(player_cards, computer_cards)
#             print("It's a draw.")
#             is_game_still_on = False
#         elif player_score > computer_score:
#             print_hand(player_cards, computer_cards)
#             print("You win.")
#             is_game_still_on = False
#         else:
#             print_hand(player_cards, computer_cards)
#             print("You lose.")
#             is_game_still_on = False
# play_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
# if play_choice == 'y':
#     wanna_play = True
# else:
#     print("Thank you for playing. Have a nice day.")
#     wanna_play = False
# def check_blackjack(list_cards):
#     if sum(list_cards) == 21:
#         return True
#     else:
#         return False
#
# def contains_ace(list_cards):
#     for card in list_cards:
#         if card == 11:
#             return True
#         else:
#             return False
#
# def change_ace_value(list_cards):
#     for card in list_cards:
#         if card == 11:
#             list_cards[indexOf(card)] = 1
#         return list_cards
#
# wanna_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
# if wanna_play == 'y':
#     for draw in range(0,2):
#         player_cards.append(random.choice(cards))
#         computer_cards.append(random.choice(cards))
#     player_score = sum(player_cards)
#     computer_score = sum(computer_cards)
#     print(f"\tYour cards: {player_cards}, current score: {player_score}")
#     print(f"\tComputer's first card: {computer_cards[0]}")
#     if check_blackjack(computer_cards):
#         print("You lose.")
#         game_over = True
#     elif check_blackjack(player_cards):
#         print("Win with a Blackjack.")
#     hit_or_stay = input("Type 'y' to get another card, type 'n' to pass: ")
#     while hit_or_stay == 'y':
#         player_cards.append(random.choice(cards))
#         player_score = sum(player_cards)
#         computer_cards.append(random.choice(cards))
#         computer_score = sum(computer_cards)
#         if player_score > 21:
#             if contains_ace(player_cards):
#                 player_cards = change_ace_value(player_cards)
#                 player_score = sum(player_cards)
#             else:
#                 print("You went over. You lose")
#                 game_over == True
#         print(f"\tYour cards: {player_cards}, current score: {player_score}")
#         print(f"\tComputer's first card: {computer_cards[0]}")
#     else:
#         print(player_cards)
#         print(computer_cards)
#         print(f"\tYour final hand: {player_cards}, final score: {player_score}")
#         print(f"\tComputer's final hand: {computer_cards}, current score: {computer_score}")
#         if player_score == 21:
#             print("Win with a Blackjack.")
#         elif computer_score == 21:
#             print("Computer has a Blackjack. You lost.")
#         elif player_score == computer_score:
#             print("It's a draw")
#         elif (21 - player_score) > (21 - computer_score):
#             print("You lose.")
#         else:
#             print("You Win.")
# else:
#     print("Thank you for playing. Have a nice day.")
