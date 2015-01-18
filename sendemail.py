#!/usr/bin/python

import smtplib
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('email.ini')

def send_email(to, letter):
    sender = 'lobthat@gmail.com'
    receivers = [to[to.find('<'):-1]]

    message = """From: Lob Mailer <lobthat@gmail.com>
    To: %s
    Subject: Sent letter!

    Just a confirmation that your letter has been sent at %s.


    Thanks your using lobthat@gmail.com!

    """ % (to, letter.url)

    try:
       server = smtplib.SMTP(config.get('server','smtp'), 587)
       server.ehlo()
       server.starttls()
       server.ehlo()
       server.login(config.get('login', 'username'), config.get('login', 'password'))

       server.sendmail(sender, receivers, message)         
       print "Successfully sent email"
    except SMTPException:
       print "Error: unable to send email"