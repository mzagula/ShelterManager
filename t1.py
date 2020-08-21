import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

s = smtplib.SMTP(host='smtp.gmail.com', port=587)

s.starttls()
s.login("marta.testowe123@gmail.com", "AlaMaKota123")
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