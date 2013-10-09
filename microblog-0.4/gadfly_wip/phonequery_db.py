#!../flask/bin/python


import sys
import gadfly
from ../send_sms import send_one_sms

#Reconnect to db
cxn = gadfly.gadfly("project_db","data_dir")
cur = cxn.cursor()

#Search the phone numbers
cur.execute("select user_name, phone_num from t_users")
for x in cur.fetchall():
    print x[1]
    send_one_sms(x[1])


cxn.commit()

