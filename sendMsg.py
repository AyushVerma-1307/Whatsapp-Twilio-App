from twilio.rest import Client
sid='AC23f06e1e176da7ab10fe40b368e4b914'
authToken='92de112c5b0be86179658a3bcf83e1e9'
client=Client(sid,authToken)

message=client.messages.create(to='whatsapp:+916388160613',
            from_='whatsapp:+14155238886',body='hello its mee.')

# python -m virtualenv env 
# pip show twilio 
# if WARNING: Package(s) not found: twilio is output
# run pip install twilio 
# python .\sendMsg.py 

# if script do not execute 
# run on powershell 
# Set-ExecutionPolicy Unrestricted
# then type A 
# When you are done, you can set the policy back to its default value with: 
# Set-ExecutionPolicy Restricted 
