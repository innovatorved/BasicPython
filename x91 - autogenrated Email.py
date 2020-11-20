##################################

# Author : Ved Prakash Gupta     #

##################################

#ye pura program ready hai but ek chota se claw baccha hua hai isme image html ke through nhi lgr rhi email pr
#file with attachment

import smtplib
from email.mime.multipart import MIMEMultipart as MultI
#from email.mime.application import MIMEApplication as ApP
from email.mime.image import MIMEImage as ImG
from email.mime.text import MIMEText as TexT
from email.mime.base import MIMEBase as BasE
from email import encoders
#import base64

##################################
#import mimetypes
#from email.utils import make_msgid


#content = '''Hello, This is a part Of Next Innovation new Project
#            i will sent you a detail file of What is Next In'''


#sub = "NextInfo"

#Email and Password
sen_email = "nextinnovate.info@gmail.com"
sen_pass = "next@info"
#rec_email = "nextin.520@gmail.com"

#############################################################
#connect with email server
#Create SMTP session for sending the email
server = smtplib.SMTP_SSL("smtp.gmail.com" , 465)

#login to your Gmail
server.login(sen_email , sen_pass)
print("Succesfully Connected with Email.")

##############################################################

def user_for_attachment(rec_email , file , sub , content , html):

    #company mail
    sen_email = "nextinnovate.info@gmail.com"
    #Setup the MIME
    msg = MultI()
    msg['From'] = sen_email
    msg['To'] = rec_email
    msg['Subject'] = sub

    #use for adding html data
    html_body_1 = "<b style='color:orange; font-size:50px ; text-align:center;'>NextIn</b>"
    msg.attach(TexT(html_body_1 , 'html'))

    html_body_tag = "<p style = 'margin:5px auto; color:#8463C8; font-size:20px ;'>#future of technology</p>"
    msg.attach(TexT(html_body_tag , 'html'))
    
    html_body_2 = "<p style='color:#C86381; font-size:20px ;'>"+sub+"</p>"
    msg.attach(TexT(html_body_2 , 'html'))
    
    #set the logo on Email by MIMEImage
    img = "icon.png"
    open_img = open(img , 'rb')
    read_img = ImG(open_img.read())   #connect with MIMEImage
    open_img.close()
    read_img.add_header('Content-ID' , 'attachment; filename=icon')
    msg.attach(read_img)        #attach image into MIMEMultipart
    '''
    html_body_2 = "<img src="+'icon.png'+">"
    msg.attach(TexT(html_body_2 , 'html'))
    
    '''
    #####################################

    #for attaching html section
    if html != None:
        msg.attach(TexT(html , 'html'))
    
    #the subject line
    #the body and the attachment for the mail
    #we edit txt content to html 
    #msg.attach(TexT(content , 'plain'))
    con = "<div style = 'height:200px; width:500px; border:2px solid #C70039; margin: 20px auto;'><h2 style = 'color:#57716A; font-size:15px; margin:20px auto; padding-left:50px;'>"+content+"</h2></div>"
    msg.attach(TexT(con , 'html'))

    #msg.add_header('subject' , sub)
    
    if file != None:
        #name of attached file
        #file = "for_test.pdf"
        
        #open the fileas binary mode
        file_open = open(file , 'rb')

        #setup MIMEBase
        load = BasE('application' , 'octet-stream')

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

    #attach insta link
    html_insta = '''<hr width="70%">
                    <p style='font-size:20px; color:#83BFBD;'>
                    follow our Page on Insta :
                    <a href = 'https://instagram.com/next_in__?igshid=190uoeko97a2c'>
                    <b style='color:#4079AA;'>next_in__@insta</b>
                    </a>
                    </p>

                '''
    msg.attach(TexT(html_insta , 'html'))
    #change msg to string
    text = msg.as_string()
    return text


#user define function for sending an a email
def email(rec_email , msg):
    server.sendmail("nextinnovate.info@gmail.com" , rec_email ,msg)
    #logout from server
    #server.quit()
    print("Succesfully Send Email to : " , rec_email)

#email(rec_email , text)

def send(rec_email , sub , content , file = None , html = None):
    '''
    send(rec_email , sub , content , file = None , html = None)
    u are customize email design by givining your own html Codee
    '''
    
    txt = user_for_attachment(rec_email , file , sub , content , html)
    email(rec_email , txt)
    del(txt)

def logOut():
    out = server.quit()
    print("Email LogOut : " ,out)


#we are ready to send mail

rec_email = "vedprakashgupta463@gmail.com"
#file_name = "for_test.pdf"
sub = "U are now Connected to NextIn !"

content = '''
		heyy ! you are now Succesfully Connected with
		Next Innppovation.
		For any help related queries 
		pls email on : nextinnovate.info@gmail.com
		           - Team NextIn
		'''
#html = "<h2 style='color:orange; font-size:50px ;'>this is NextIn</h2>"


send(rec_email , sub , content)
#logOut()
