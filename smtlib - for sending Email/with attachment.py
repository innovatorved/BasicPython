#file with attachment

import smtplib
from email.mime.multipart import MIMEMultipart as MultI
from email.mime.text import MIMEText as TexT
from email.mime.base import MIMEBase
from email import encoders 

content = '''Hello, This is a part Of Next Innovation new Project
            i will sent you a detail file of What is Next In'''

sub = "NextInfo"

#Email and Password
sen_email = "nextinnovate.info@gmail.com"
sen_pass = "next@info"
rec_email = "nextin.520@gmail.com"

#############################################################

#connect with email server
#Create SMTP session for sending the email
server = smtplib.SMTP_SSL("smtp.gmail.com" , 465)

#login to your Gmail
server.login(sen_email , sen_pass)


##############################################################

#Setup the MIME
msg = MultI()
msg['From'] = sen_email
msg['To'] = rec_email
msg['Subject'] = sub

#the subject line
#the body and the attachment for the mail
msg.attach(TexT(content , 'plain'))

#name of attached file
file = "for_test.pdf"

#open the fileas binary mode
file_open = open(file , 'rb')

#setup MIMEBase
load = MIMEBase('application' , 'octate-stream')

#read file with payload
load.set_payload((file_open).read())

#encode the statement
encoders.encode_base64(load)

#add payload header with filename
load.add_header('Content-Decomposition' , 'attachment' , filename = file)

#attach header aand filename payload to msg
msg.attach(load)

#change msg to string
text = msg.as_string()


#user define function for sending an a email
def email(email , msg):
    server.sendmail("nextinnovate.info@gmail.com" , email ,msg)
    #logout from server
    #server.quit()
    print("Succesfully Send Email to : " , email)

#email(rec_email , text)


