import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from DBConnection import DBConnection
import pandas as pd

connection = DBConnection()
email_users = connection.select("email_users","")

df = pd.DataFrame(email_users)
print("aaa "+str(df[1][0]))

s = smtplib.SMTP(host='smtp.gmail.com', port=587)

s.starttls()
s.login(df[0][0], df[1][0])
sender_email = "marta.testowe123@gmail.com"
receiver_email = "mzagula1992@gmail.com"

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

text = """\
Hi,"""

part1 = MIMEText(text, "plain")
message.attach(part1)
s.sendmail(sender_email, receiver_email, message.as_string())