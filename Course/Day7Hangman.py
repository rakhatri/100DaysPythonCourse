import random
from hangman_art import hangman_logo, stages

word_list = ["time", "person", "year", "way", "day", "thing", "man", "world", "life", "hand",
             "part", "child", "eye", "woman", "place", "work", "week", "case", "point", "government",
             "company", "number", "group", "problem", "fact", "idea", "water", "money", "question", "story",
             "book", "night", "lot", "right", "study", "mother", "issue", "name", "theory", "body",
             "report", "line", "order", "voice", "family", "price", "action", "reason", "view", "term",
             "business", "friend", "power", "hour", "game", "law", "scene", "paper", "earth", "father",
             "force", "education", "baby", "cost", "car", "truth", "music", "art", "party", "nature"]
lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ""
print(hangman_logo)
for position in range(len(chosen_word)):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter? ").lower()
    display = ""
    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"You Lose!!! It was: {chosen_word}")
    if "_" not in display:
        game_over = True
        print(f"You Win!!! {chosen_word} is the correct answer.")
    else:
        print(stages[lives])
        print(f'''**************************** {lives}/6 LIVES LEFT****************************''')
        print("Word to guess: " + display)
