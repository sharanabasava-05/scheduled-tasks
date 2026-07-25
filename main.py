import csv
import datetime as dt
import random
import smtplib



place_holder="[NAME]"
# 2. Check if today matches a birthday in the birthdays.csv
with open("birthdays.csv","r") as f:
    csv_dict=csv.DictReader(f)
    # print(csv_dict)
    birthday_dict = {}
    for birth_dict in csv_dict:
       birthday_dict[(int(birth_dict["day"]),int(birth_dict["month"]))]=birth_dict["name"]

#Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
today=dt.datetime.now().date().day
month=dt.datetime.now().date().month
random_file=random.randint(1,3)

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
def letter_generator(text):
    my_email=os.environ.get("my_email")
    password=os.environ.get("password")

    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="sharanabasavabasava841@gmail.com",
                            msg=f"subject:Birthaday whishes\n\n{text}")
        connection.close()

if (today,month) in birthday_dict:
    with open(f"letter_templates/letter_{random_file}.txt","r") as f:
        content=f.read()
        final_content=content.replace(place_holder,birthday_dict[(today,month)])
        letter_generator(final_content)
