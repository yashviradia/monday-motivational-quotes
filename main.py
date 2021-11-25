import os
from dotenv import load_dotenv, find_dotenv
import smtplib
import datetime as dt
import random

load_dotenv(find_dotenv())

MY_EMAIL = os.environ.get("FROM_ADDR")
PASSWORD = os.environ.get("PASSWORD")
TO_ADDRS = os.environ.get("TO_ADDRS")

now = dt.datetime.now()
day_of_week = now.weekday()

# Get random quote for Monday
with open("quotes.txt") as quote_file:
    quote_list = quote_file.readlines()
    monday_quote = random.choice(quote_list)


if day_of_week == 2:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_ADDRS,
            msg="Hallo."
    )
    connection.close()






