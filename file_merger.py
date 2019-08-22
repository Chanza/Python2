
import pandas as pd
import smtplib, ssl
import imaplib,email,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import glob


def concatenate(indir, outfile):
    os.chdir(indir)
    fielist = glob.glob("*.xlsx")
    dfList=[]
    for filename in fielist:
        print(filename)
        df = pd.read_csv(filename,header=None)
        dfList.append(df)
    concatdf=pd.concat(dfList,axis=0)
    concatdf.to_excel(r'C:/Users/HP/Documents/CODE/data/merged_output2.xlsx')
    print(concatdf)


concatenate(indir="C:/Users/HP/Desktop/aft2",outfile="C:/Users/HP/Desktop/concated")





#mail.sendmail(e_sender, e_receiver, msg.as_string())
#con.close()



























