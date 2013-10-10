#! /usr/bin/python

import sys
import gadfly
    
#Reconnect to db
cxn = gadfly.gadfly("project_db","data_dir")
cur = cxn.cursor()

#Search the phone numbers
cur.execute("select user_name, phone_num from t_users")
for x in cur.fetchall():
    print x
	
cxn.commit()

#temp = phonequery_db.txt
#f = open(phonequery_db.txt, 
