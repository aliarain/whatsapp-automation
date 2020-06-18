from twilio.rest import Client 
 
account_sid = 'ACffe85f623b1eeee03089530c77ec3861' 
auth_token = '3f85e23fac2638ba9f11f894ead245d9' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your appointment is coming up on July 21 at 3PM',      
                              to='whatsapp:+923341681110' 
                          ) 
 
print(message.sid)