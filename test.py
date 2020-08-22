from DBConnection import DBConnection
import pandas as pd

connection = DBConnection()
email_users = connection.select("email_users","")

df = pd.DataFrame(email_users)
print("aaa "+str(df[1][0]))

