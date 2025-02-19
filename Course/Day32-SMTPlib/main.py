##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import smtplib

import pandas
import random

now = dt.datetime.now()
current_month = now.month
current_day = now.day
my_email = "rahulafterdark1@gmail.com"
password = "hqrtyclddsvbqdlh"

birthday_file = pandas.read_csv("birthdays.csv")
birthday_dict = birthday_file.to_dict(orient="records")
for person in birthday_dict:
    if current_month == person["month"] and current_day == person["day"]:
        letter = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(letter) as birthday_letter:
            message = birthday_letter.read().replace("[NAME]", person["name"])
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=person["email"],
                                    msg=f"Subject:Happy Birthday!\n\n{message}")


