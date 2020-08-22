from Email import Email
import pandas as pd

mail = Email()

mail.receiver="mzagula1992@gmail.com"
mail.subject="Eloeloelo"
mail.sender="marta.testowe123@gmail.com"
mail.message="testtest"

mail.send_mail()