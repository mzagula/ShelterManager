import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from DBConnection import DBConnection
import pandas as pd


class Email:
    message = ""
    receiver = ""
    sender = ""
    subject = ""

    def __init__(self):
        self.server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        self.server.starttls()

    def send_mail(self):
        connection = DBConnection()
        email_users = connection.select("email_users", "")
        df = pd.DataFrame(email_users)
        self.server.login(df[0][0], df[1][0])
        receiver_mail = self.receiver
        sender_mail = df[0][0]

        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject
        message["From"] = sender_mail
        message["To"] = receiver_mail

        text = self.message
        body = MIMEText(text, "plain")
        message.attach(body)
        self.server.sendmail(sender_mail, receiver_mail, message.as_string())

    # def send_to_manager(self):
    #     connection = DBConnection()
    #     email_users = connection.select("email_users","")
    #     df = pd.DataFrame(email_users)
    #     s.login("marta.testowe123@gmail.com", "AlaMaKota123")
    # sender_email = "marta.testowe123@gmail.com"
    # receiver_email = "mzagula1992@gmail.com"
    #
    # message = MIMEMultipart("alternative")
    # message["Subject"] = "multipart test"
    # message["From"] = sender_email
    # message["To"] = receiver_email
    #
    # text = self.message
    #
    # part1 = MIMEText(text, "plain")
    # message.attach(part1)
    # s.sendmail(sender_email, receiver_email, message.as_string())
