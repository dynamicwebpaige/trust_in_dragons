#!flask/bin/python

import sys
import gadfly
from send_mail import sendOneMail
#Reconnect to db
def sendMails(name,amount,desc):
    cxn = gadfly.gadfly("project_db","data_dir")
    cur = cxn.cursor()
    
    #Search query on email
    cur.execute("select user_name, user_email from t_users")
    for x in cur.fetchall():
        print x[1]
        #sendOneMail(x[1],x[0],name,amount,desc)
    cxn.commit()
    
