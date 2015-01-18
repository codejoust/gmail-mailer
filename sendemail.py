#!/usr/bin/python

import smtplib
import ConfigParser

# Import the email modules we'll need
from email.mime.text import MIMEText



config = ConfigParser.ConfigParser()
config.read('email.ini')

def send_email(to, letter):

    toclean = to
    if to.find('<') != -1:
        toclean = to[:to.find('<')]

    message = """
    Hi %s,

    Just a confirmation that your letter has been sent at %s.


    Thanks your using lobthat@gmail.com,
    The LobThat Team

    """ % (toclean, letter['objects'][0]['url'])

    # Create a text/plain message
    msg = MIMEText(message)

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'Lobthat letter send confirmation!'
    msg['From'] = 'lobthat@gmail.com'
    msg['To'] = to  

    sender = msg['From']
    
    receivers = [to]

    try:
       server = smtplib.SMTP(config.get('server','smtp'), 587)
       server.ehlo()
       server.starttls()
       server.ehlo()
       server.login(config.get('login', 'username'), config.get('login', 'password'))

       server.sendmail(sender, receivers, msg.as_string())         
       print "Successfully sent email"
       server.quit()
    except SMTPException:
       print "Error: unable to send email"

