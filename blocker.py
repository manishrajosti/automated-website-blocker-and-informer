from twilio.rest import Client
import time
from datetime import datetime as dt

account_sid = 'AC669cb838e082f828f1af937c94286f4e' 
auth_token = '###################################'
my_twilio_phone = "+############"
my_phone_number = "+############"
a = 0
b= dt.now().second
hosts_path = "hosts"
redirectTO = "127.0.0.1"
website_list = ["www.google.com", "facebook.com", "twitter.com"]

def sendSMS():
    client = Client(account_sid, auth_token)
    client.messages.create(
            from_  = my_twilio_phone,
            to = my_phone_number,
            body = f'''
                    Restricted website blocking started. Wait until you get message for unblocking hours.

            '''
        )

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 21) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23,59):
        with open(hosts_path, 'r+') as file:
            content  = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirectTO + " "+ website+ "\n")
                    a=a+1
                    message = str(a) + " " + "Time of entry: " + str(dt.now())
                    if b == dt.now().second:
                        print(message)
                        sendSMS()
                        
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for lst in content:
                if not any(website in lst for website in website_list):
                    file.write(lst)
            file.truncate()
    time.sleep(3)
