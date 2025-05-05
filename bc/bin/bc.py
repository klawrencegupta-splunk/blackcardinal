#!/usr/bin/python
import datetime
import random
import string

# Time Date stamper
def tds():
    tds = str(datetime.datetime.now())
    return tds

# Time Date stamper
def last_login():
    last_login = str(datetime.datetime.now())
    return last_login

# Time Date stamper
def prev_login():
    #timedelta = random.randint(0, 999)
    prev_login = str(datetime.datetime.now())
    #prev_login = str(now) - str(timedelta)
    return prev_login

def user_id():
    length = 10
    user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return user_id

def emailbooler():
    emailbooler = ['.com', '.org', '.net']
    emailbooler = random.choice(emailbooler)
    return emailbooler

def user_email_addr():
    length = 10
    user_email_addr = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    length = 5
    user_email_domain = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    user_email_addr = str(user_email_addr+"@"+user_email_domain+emailbooler())
    return user_email_addr

def user_location():
    latitude = random.uniform(-90, 90)  # Latitude ranges from -90 to 90
    longitude = random.uniform(-180, 180)  # Longitude ranges from -180 to 180
    return latitude, longitude

def bal_amt():
    bal_amt = random.randint(0, 999999)
    return bal_amt

def debit_amt():
    debit_amt = random.randint(0, 999999)
    return debit_amt

def ip_addr():
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    return ip

def booler():
    booler = ['T','F']
    booler = random.choice(booler)
    return booler


if __name__ == "__main__":
    tds = str(tds())
    user_id = str(user_id())
    last_login = str(last_login())
    prev_login = str(prev_login())
    last_ip = str(ip_addr())
    prev_ip = str(ip_addr())
    debit_amt = str(debit_amt())
    bal_amt = str(bal_amt())
    user_email_addr = str(user_email_addr())
    latitude, longitude = user_location()
    user_id_event = "user_id:" + user_id + ",last_login:" +last_login + ",prev_login:" +prev_login + ",last_ip:" + last_ip + ",prev_ip:" + prev_ip + ",debit_amt:" + debit_amt + ",bal_amt:" + bal_amt
    user_email_event = "user_email_addr:" + user_email_addr + ",last_login:" +last_login + ",prev_login:" +prev_login + ",last_ip:" + last_ip + ",prev_ip:" + prev_ip + ",valid_addr:" + str(booler()) + ",active_addr:" + str(booler())
    user_location_event = "user_location:"+ str(latitude)+"/"+str(longitude)+ ",last_login:"+ last_login + ",prev_login:" +prev_login + ",last_ip:" + last_ip + ",prev_ip:" + prev_ip + ",latitude:" + str(latitude) + ",longitude:" + str(longitude)     
#    print(tds)
    print(user_id_event)
    print(user_email_event)
    print(user_location_event)
