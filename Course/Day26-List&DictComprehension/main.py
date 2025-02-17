# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)
nato_phonetic_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
# nato_dict = nato_phonetic_data_frame.to_dict()
# print(nato_dict)
nato_phonetic_dict = {row.letter: row.code for (index, row) in nato_phonetic_data_frame.iterrows()}
print(nato_phonetic_dict)


def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        code_name = [nato_phonetic_dict[each_letter] for each_letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(code_name)


generate_phonetic()
