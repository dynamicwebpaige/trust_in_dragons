# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
def send_one_sms(phoneNum):
    account_sid = "ACbed2373fd3953a3779dc6de74d1300df"
    auth_token  = "1410cc3ba58b8e555c94e91409a3e351"
    client = TwilioRestClient(account_sid, auth_token)
     
    message = client.sms.messages.create(body="Your donation to was succesfully utilized. Details have been mailed to you.",
        to=phoneNum, #"+15126059304",    # Replace with your phone number
        from_="+15122706308") # Replace with your Twilio number
    print message.sid
