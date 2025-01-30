import random
# student_scores = [150, 123, 121, 33, 21, 78, 87, 199, 33, 54, 67, 98, 100]
#
# x = 0
# for score in student_scores:
#     if x < score:
#         x = score
# print(x)
# sum = 0
# for number in range(1, 101):
#     sum += number
# print(sum)
# print(ord('9'))
Alphabets = []
for i in range(65, 91):
    Alphabets.append(chr(i))
for j in range(97, 123):
    Alphabets.append(chr(j))
Alphabets.sort()
numbers = []
for number in range(48, 58):
    numbers.append(chr(number))
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_alphabets = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
password_list = []
for x in range(0, nr_alphabets):
    password_list.append(random.choice(Alphabets))
for x in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
for x in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
# print(password_list)
password_easy = ""
for x in password_list:
    password_easy += x
print("Easy Level Generated Password: " + password_easy)
random.shuffle(password_list)
password_hard = ""
for x in password_list:
    password_hard += x
print("Hard Level Generated Password: " + password_hard)



