from twilio.rest import Client


account_sid = 'your_account_sid_here'
auth_token = 'your_auth_token_here'
twilio_number = 'Your_twilio_number' 
receiver_number = 'reciver_number'

client = Client(account_sid, auth_token)


message = client.messages.create(
    body= input('Type your message Here: '),
    from_=twilio_number,
    to=receiver_number
)

print(f"Message sent! SID: {message.sid}")
