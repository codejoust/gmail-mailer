import poplib

import email
import time

import lobapi 

import sendemail
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('email.ini')

print('Fetching new email :).')

M = poplib.POP3_SSL(config.get('server', 'pop'), '995')
M.user(config.get('login', 'username'))
M.pass_(config.get('login', 'password'))

def getNumMessages():
    try:
        return len(M.list()[1]) + 1
    except:
        print 'fetch err'
        return 0

def fetchMessages():

    numMessages = getNumMessages()

    #Get messages from server:
    messages = [M.retr(i) for i in range(1, numMessages)]

    print('Fetching %d messages.' % numMessages)

    for indx, message in enumerate(messages):
        print message
        b = email.message_from_string("\n".join(message[1]))
        if b.is_multipart():
            for payload in b.get_payload():
                if (payload.get_content_type() == 'text/plain'):
                # if payload.is_multipart(): ...
                    output = payload.get_payload()
        else:
            output = b.get_payload()
        if output:
            print '----- email ----'
            print b['from']
            print b['subject']
            print output
            print 'sending content'
            letter = lobapi.deal_with_email_data(b['subject'], b['from'], ''.join(output))
            sendemail.send_email(b['from'], letter)
        print 'deleting message'
        M.dele(indx+1)

    print('Done fetching messages')
    return numMessages

numMessagesOld = fetchMessages()

#M.quit()

while True:
    time.sleep(10)
    print('waiting for new messages...')
    if (numMessagesOld != getNumMessages()):
        fetchMessages()
    else:
        time.sleep(10)

