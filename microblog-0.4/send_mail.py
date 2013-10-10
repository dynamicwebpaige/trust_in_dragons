#! flask/bin/python

import sendgrid

def sendOneMail(emailId, name, link, amount,  desc):
# make a secure connection to SendGrid
    s = sendgrid.Sendgrid('profoundlypaige', 'B4ttleH4ck', secure=True)
    
    # make a message object
    #Sender
    message = sendgrid.Message("noreply@trustthedragons.com", "B4ttleH4ck", "Howdy!", '%(personName)s You are awesome. And we delivered. Details of an invoice of amount %(amount)s have been uploaded at %(link)s. The description is as as follows: %(desc)s' % \
    {'personName' : name, 'amount' : amount, 'link' : link, 'desc' : desc})
    
    # placeholder for usernames + emails
    # Receiver
    message.add_to(emailId, name)
    s.smtp.send(message)
