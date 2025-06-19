##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import smtplib
from random import randint

my_email = "singhkatiyarvarun717@gmail.com"
my_password = "lpgm dxsq oapk gakn"


today = dt.datetime.now()


def creating_love_message(item_index) :
    num = randint(1,3)
    with open(f"letter_templates/wish_{num}.txt","r") as text_file :
        list_of_lines = text_file.readlines()
        list_of_lines[0] = "Dear " + file["name"][item_index] + "\n"
        message = "".join(list_of_lines)
        return message





# reading csv file
file = pandas.read_csv("birthdays.csv")
for index in range(len(file)) :
    if  file["day"][index] == today.day and  file["month"][index] == today.month :
        with smtplib.SMTP("smtp.gmail.com",587) as wish_file :
            wish_file.starttls()
            wish_file.login(user=my_email,password=my_password)
            wish_file.sendmail(from_addr=my_email , to_addrs=file["email"][index],msg=f"subject:My {file["name"][index]}\n\n{creating_love_message(index)}")










