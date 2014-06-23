from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "<your own twilio account id>"
auth_token  = "<your own twilio auth token>"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="I am Harsh Vardhan",
    to="00000",    # Replace with your phone number
    from_="000000") # Replace with your Twilio number
print message.sid
