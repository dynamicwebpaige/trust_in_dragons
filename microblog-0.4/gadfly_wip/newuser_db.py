#!../flask/bin/python
import os
import gadfly
import re
 
#user input variables passed over by Prashant's web stuff
#n_var = 'dummyname'     #form.name
#e_var = 'dummyemail@email.com'    #form.email
#p_var = '11111111'    #form.phone_number 
 
#Create the dir and the db
#os.mkdir("data_dir")
#cxn = gadfly.gadfly()
#cxn.startup("project_db", "data_dir")
 
#Reconnect to db
cxn = gadfly.gadfly("project_db","data_dir")
 
#Create initial set of tables
cur = cxn.cursor()
#cur.execute("drop table t_users")
cur.execute("create table t_users (user_name varchar, user_email varchar, phone_num varchar)")  

#"""Add new user based on web form inputs"""
#insertfun = "insert into t_users (user_name, user_email, phone_num) values (?, ?, ?)"
#cur.execute(insertfun, ("Jessica", "jfreasier@gmail.com", "+18322769634"))
#cur.execute(insertfun, ("Paige", "profoundlypaige@gmail.com", "+12547166034"))
#cur.execute(insertfun, ("Christine", "christine.doig.cardet@gmail.com", "+15126059304"))
#cur.execute(insertfun, ("Prashant", "prashantverma999@gmail.com", "+15127858943"))

#cur.execute("select user_name, user_email from t_users")
#for x in cur.fetchall():
#    print x
#cur.execute("select user_name, phone_num from t_users")
#for x in cur.fetchall():
#    print x

cxn.commit()

