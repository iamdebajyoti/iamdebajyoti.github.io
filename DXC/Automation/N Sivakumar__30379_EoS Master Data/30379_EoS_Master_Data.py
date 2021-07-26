
from numpy import datetime64
import pandas as pd
import numpy as np
import os
from operator import itemgetter

sample_file_path = r"C:\Users\ddutta8\OneDrive - DXC Production\Documents\DXC_Automation\N Sivakumar__30379_EoS Master Data\Sample file for EOS Master Data.xlsx"

sample_file_sheets = pd.ExcelFile(os.path.join(sample_file_path))
# print(*sample_file_sheets.sheet_names, sep='\n')

# print('\n\n')
# df_Sw = pd.DataFrame()
# df_Sw = pd.read_excel(os.path.join(sample_file_path), sheet_name="Software Title", usecols=["ProductName","EndOfLifeDate"], index_col=None, engine="openpyxl", header=0)
# # print(df_Sw.shape, df_Sw.columns, df_Sw.info())
# print('\n\n')
# # df_Sw["Check"] = (df_Sw["EndOfLifeDate"].str.isnumeric())
# # df_Sw .dropna(how='any', inplace=True)
# df_Sw = df_Sw[df_Sw["EndOfLifeDate"].notnull()]
# df_Sw = df_Sw[df_Sw["EndOfLifeDate"]
# df_Sw["EndOfLifeDate"].apply(np.isreal)
# # df_Sw["EndOfLifeDate"] = df_Sw["EndOfLifeDate"].astype('datetime64')
# print(df_Sw.shape, df_Sw.columns, df_Sw.info())
# print('\n\n')
# # print(df_Sw.groupby("EndOfLifeDate").groups.keys(), df_Sw.groupby("EndOfLifeDate").groups.values())
# for _groups_ in df_Sw.groupby("EndOfLifeDate").groups:
#     print(type(_groups_), _groups_)

# print(df_Sw.info())

df_SOE = pd.DataFrame()
df_SOE = pd.read_excel(os.path.join(sample_file_path), sheet_name="SOE Application", usecols=["LATEST SOFTWARE NAME","GENERAL SUPPORT END DATE"], index_col=None, engine="openpyxl", header=0,)
df_SOE.rename(columns={"LATEST SOFTWARE NAME":"ProductName","GENERAL SUPPORT END DATE":"EndOfLifeDate"}, inplace=True)
# print(df_SOE.columns, df_SOE.shape, df_SOE.info())
df_SOE["EndOfLifeDate"].dropna(inplace=True)
print(df_SOE["EndOfLifeDate"].iloc[0:50])
print(df_SOE["EndOfLifeDate"].iloc[50:100])
print(df_SOE["EndOfLifeDate"].iloc[100:150])
print(df_SOE["EndOfLifeDate"].iloc[150:])

# print(df_SOE.columns, df_SOE.shape, df_SOE.info())

# df_OS = pd.DataFrame()
# df_OS = pd.read_excel(os.path.join(sample_file_path), sheet_name="OS", usecols=["OSName","COSVersion","EndOfLifeDate"], index_col=None, engine="openpyxl", header=0)
# # print(df_OS.columns.shape)
# df_OS ["ProductName"] = df_OS["OSName"] + df_OS["COSVersion"].astype('str')
# # print(df_OS.columns)
# # print(df_OS.columns.shape)
# df_OS.drop(columns=["OSName","COSVersion"], inplace=True)
# df_OS = df_OS[["ProductName","EndOfLifeDate"]]
# print(df_OS.columns)
# print(df_OS.shape)
# print(df_OS.info())

# df_Samples = pd.DataFrame()
# df_Samples = df_Sw + df_SOE + df_OS
# print(df_Samples.columns)
# print(df_Samples.shape)
# print(df_Samples.info())

  


# """
# If you want to add your Microsoft 365 account to another mail app that supports POP, IMAP, or SMTP, here are the manual server settings you'll need:

#     IMAP server name: outlook.office365.com
#     IMAP port: 993
#     IMAP encryption method: SSL/TLS
#     POP server name: outlook.office365.com
#     POP port: 995
#     POP encryption method: SSL/TLS
#     SMTP server name: smtp.office365.com
#     SMTP port: 587
#     SMTP encryption method: STARTTLS
# """
# '''
# import email
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders
# import os.path
# import sys

# def select_mail_template():
#     pass

# def send_email(email_sender,email_recipient, email_subject, email_message, attachment_location = ''):
#     your_login_name = input("Enter your email login name ::  ")
#     your_login_pass = input("Enter your email password ::  ")
#     print("Sending email please wait ...")
#     msg = MIMEMultipart()
#     msg['From'] = email_sender
#     msg['To'] = email_recipient
#     msg['Subject'] = email_subject
#     msg.attach(MIMEText(email_message, 'plain'))
#     if attachment_location != '':
#         filename = os.path.basename(attachment_location)
#         attachment = open(attachment_location, "rb")
#         part = MIMEBase('application', 'octet-stream')
#         part.set_payload(attachment.read())
#         encoders.encode_base64(part)
#         part.add_header('Content-Disposition',
#                         "attachment; filename= %s" % filename)
#         msg.attach(part)
#     try:
#         server = smtplib.SMTP('smtp.office365.com', 587)
#         server.ehlo()
#         server.starttls()
#         server.login(your_login_name, your_login_pass)
#         text = msg.as_string()
#         server.sendmail(email_sender, email_recipient, text)
#         print('Email sent successfully to {}'.format(email_recipient))
#         server.quit()
#     except:
#         print("SMPT server connection error")
#     return True
# print("\n\n")
# email_sender = input(r"Enter your email address or send-as email address  (From)  :  ")
# print("\n")
# email_recipient = input(r"Enter the recipient email address   (To)  :  ")
# print("\n")
# email_subject = input(r"Enter your email's subject line  (Subject)  :  ")
# print("\nEnter/Paste your message.   [Ctrl-D or Ctrl-Z ( windows ) to save it.   ]\n")
# email_message = '\n'.join((sys.stdin.readlines()))
# attachment_location = input(r"Enter the full path with name for the attachment file/ Hit Enter for no attachment -   (Attachment)  :  ")
# print("\n\n")
# print("\n\n")
# send_email(email_sender, email_recipient, email_subject, email_message, attachment_location)


# # send_email('debajyoti.dutta@dxc.com', 'mqhelpdesk@dxc.com', 'Happy New Year', 'We love Outlook', "C:\\Users\\ddutta8\\OneDrive - DXC Production\\Desktop\\Badge red flag with logo.png")


# # send_email('debajyoti.dutta@dxc.com', 'sivakumar.n3@dxc.com', 'Testing for 30379_EoS_Master_Data', 'Hi Siva, Please find the sample attachment', "C:\\Users\\ddutta8\\OneDrive - DXC Production\\Desktop\\Badge red flag with logo.png")
# '''