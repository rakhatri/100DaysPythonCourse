import smtplib
import datetime as dt
import random


my_email = "rahulafterdark1@gmail.com"
password = "hqrtyclddsvbqdlh"


now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 1:
    with open("quotes.txt") as file:
        data = file.read().splitlines()
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="rahulk46@mailinator.com",
                                msg=f"Subject:Motivational Quote of the day\n\n{random.choice(data)}")



