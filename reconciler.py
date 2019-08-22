
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

email_id_A = mystring2[-1]
email_id_B = mystring2[-2]


result, data_A = con.fetch(email_id_A,'(RFC822)')
raw_A = email.message_from_bytes(data_A[0][1])

result, data_B = con.fetch(email_id_B,'(RFC822)')
raw_B = email.message_from_bytes(data_B[0][1])

print(get_attachments(raw_A))
print(get_attachments(raw_B))

con.close()

#COMPARING THE TWO
#opening file
#pd.read_csv
file1 = pd.read_csv('C:/Users/HP/Documents/CODE/from_savanna.csv')
file2 = pd.read_csv('C:/Users/HP/Documents/CODE/from_shop.csv')

#Selecting sheet
df1 = file1.iloc[:,0:7]
df2 = file2.iloc[9:]
df2.columns = ['DOC DATE','REFERENCE','Transaction Number','REF2','ASSIGNMENT','REF3','DOC TYPE','INVOICE AMOUNT','DISCOUNT','WITH TAX','PAID AMOUNT','TEXT']


#df2 = df2a.rename(columns = {'REF1':'Transaction Number'})

print(df1)
print(df2)

#Merging columns
mergedStuff1a = pd.merge(df1, df2, on=['Transaction Number'], how='left')
mergedStuff1b = pd.merge(df1, df2, on=['Transaction Number'], how='right')



#removing NaN
mergedStuff2a = mergedStuff1a[mergedStuff1a.isna().any(axis=1)]
mergedStuff2b = mergedStuff1b[mergedStuff1b.isna().any(axis=1)]


#Printing Missing From Savanna
print('\nMissing From First File')
print(mergedStuff2a)
#mergedStuff2a.to_excel(r'C:/Users/HP/Documents/CODE/data/output1.xlsx')
#Printing Missing From Shoprite
print('\nMissing From Second File')
print(mergedStuff2b)
#mergedStuff2b.to_excel(r'C:/Users/HP/Documents/CODE/data/output2.xlsx')




#mail.sendmail(e_sender, e_receiver, msg.as_string())
#con.close()



























