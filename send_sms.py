# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
def send_one_sms(phoneNum):
    account_sid = ""
    auth_token  = ""
    client = TwilioRestClient(account_sid, auth_token)
     
    message = client.sms.messages.create(body="Your donation to XXXX was succesfully used to purchase XXX",
        to=phoneNum, #"",    # Replace with your phone number
        from_="") # Replace with your Twilio number
    print message.sid
