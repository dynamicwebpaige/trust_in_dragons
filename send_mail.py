#! flask/bin/python

import sendgrid

def sendOneMail(emailId, name):
# make a secure connection to SendGrid
s = sendgrid.Sendgrid('profoundlypaige', 'B4ttleH4ck', secure=True)

# make a message object
#Sender
message = sendgrid.Message("noreply@trustthedragons.com", "B4ttleH4ck", "Howdy, y'all!", "HTML Body Exmaple. You %(name)s just made a donation of 20 golden eggs to the dragons.")

# placeholder for usernames + emails
# Receiver
message.add_to(emailId, name)
s.smtp.send(message)
