##################################

# Author : Ved Prakash Gupta     #

##################################


#file with attachment

import smtplib
from email.mime.multipart import MIMEMultipart as MultI
#from email.mime.application import MIMEApplication as ApP
from email.mime.text import MIMEText as TexT
from email.mime.base import MIMEBase
from email import encoders 


#Email and Password


#############################################################
def Connect(sen_email , sen_pass):
    global email
    email = sen_email
    #connect with email server
    #Create SMTP session for sending the email
    
    global server
    server = smtplib.SMTP_SSL("smtp.gmail.com" , 465)

    #login to your Gmail
    server.login(sen_email , sen_pass)
    print("Succesfully Connected with Email.")

##############################################################

def user_for_attachment(sen_email , rec_email , file , sub , content , html):
    
    #sen_email
    #company mail
    #sen_email = "nextinnovate.info@gmail.com"
    #Setup the MIME
    msg = MultI()
    msg['From'] = sen_email
    msg['To'] = rec_email
    msg['Subject'] = sub

    html_body_2 = "<p style='color:#C86381; font-size:20px ;'>"+sub+"</p>"
    msg.attach(TexT(html_body_2 , 'html'))
    
    #for attaching html section
    if html != None:
        msg.attach(TexT(html , 'html'))
    
    #the subject line
    #the body and the attachment for the mail
    msg.attach(TexT(content , 'plain'))

    #msg.add_header('subject' , sub)
    
    if file != None:
        #name of attached file
        file = "for_test.pdf"
        
        #open the fileas binary mode
        file_open = open(file , 'rb')

        #setup MIMEBase
        load = MIMEBase('application' , 'octet-stream')

        #read file with payload
        load.set_payload((file_open).read())

        #encode the statement
        encoders.encode_base64(load)
        #file_open.close()
        
        #add payload header with filename
        #load = ApP((file_open).read())
        load.add_header('Content-Disposition' , 'attachment; filename="%s"' % file)

        #attach header and filename payload to msg
        msg.attach(load)

    #change msg to string
    text = msg.as_string()
    return text


#user define function for sending an a email
def mail(sen_email , rec_email , msg):
    server.sendmail(sen_email , rec_email ,msg)
    #logout from server
    #server.quit()
    print("Succesfully Send Email to : " , rec_email)

#email(rec_email , text)

def send(rec_email , sub , content , file = None , html = None):
    '''
    send(rec_email , sub , content , file = None , html = None)
    u are customize email design by givining your own html Codee
    '''
    sen_email = email
    #print(sen_email)
    txt = user_for_attachment(sen_email , rec_email , file , sub , content , html)
    #print("Done")
    #print(type(txt))
    #print(txt)
    mail(sen_email , rec_email , txt)
    #del(txt)

def logOut():
    out = server.quit()
    print("Email LogOut : " ,out)


#we are ready to send mail


