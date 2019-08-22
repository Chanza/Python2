
import pandas as pd
import smtplib, ssl
import imaplib,email,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#extra needed code
e_sender = 'mwambjeff905@gmail.com'
e_receiver = 'chaanza.t.s@gmail.com'
msg = MIMEMultipart('alternative')
msg["Subject"] = "Notify Test"
msg["From"] = e_sender
msg["To"] = e_receiver
attachment_dir = 'C:/Users/HP/Documents/CODE/'


# Extract Email
# content = 'example stuff'
imap_url = 'imap.gmail.com'



def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)


def get_attachments(msg):
    for part in msg.walk():
        if part.get_content_maintype()=='multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        fileName = part.get_filename()

        if bool(fileName):
            filePath = os.path.join(attachment_dir, fileName)
            with open(filePath,'wb') as f:
                f.write(part.get_payload(decode=True))

def search(key,value,con):
    result, data = con.search(None,key,'"{}"'.format(value))
    return data


def get_emails(result_bytes):
    msgs = []
    for num in result_bytes[0].split():
        type, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
        return msgs

con = imaplib.IMAP4_SSL(imap_url)
con.login('mwambjeff905@gmail.com', 'princecharming')
con.select('INBOX')

#print(get_body(raw))
#print(get_attachments(raw))


print(search('FROM','chaanza.t.s@gmail.com',con))
mystring = str(search('FROM','chaanza.t.s@gmail.com',con))
xk = mystring.replace("']","")
xk = xk.replace("[","")
xk = xk.replace("b'","")
mystring2 = xk.strip().split()

print(mystring2[-1])

email_id = mystring2[-1]


result, data = con.fetch(email_id,'(RFC822)')
raw = email.message_from_bytes(data[0][1])

print(get_attachments(raw))



#mail.sendmail(e_sender, e_receiver, msg.as_string())
#con.close()



























