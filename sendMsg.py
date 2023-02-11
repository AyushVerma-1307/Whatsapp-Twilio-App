from twilio.rest import Client

def message(number,message):
    sid='AC23f06e1e176da7ab10fe40b368e4b914'
    authToken='a3dd07a3195cca1d383125605d31b111'
    client=Client(sid,authToken)
    
    message=client.messages.create(to='whatsapp:'+number,
                from_='whatsapp:+14155238886',body=message)
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
