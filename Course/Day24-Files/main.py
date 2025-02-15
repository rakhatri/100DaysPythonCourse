
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.read().splitlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    starting_letter = letter.read()

for name in names:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as output_file:
        final_letter = starting_letter.replace("[name]", name)
        output_file.write(final_letter)
