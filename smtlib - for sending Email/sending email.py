import smtplib

#smtplib.SMTP_SSL("localhost") - provide ur email server and port num default port is 465
server = smtplib.SMTP_SSL("smtp.gmail.com" , 465)
'''
server.ehlo()
server.starttls()
#print(help(server))
'''

#sever.login("Email Address","Password") -use for login on server
server.login("nextinnovate.info@gmail.com" , "next@info")


def email(email,msg):
    server.sendmail("nextinnovate.info@gmail.com" , email ,msg)
    #logout from server
    #server.quit()
    print("Succesfully Send Email to : " , email)

email("nextin.520@gmail.com","Hlww Sir! your Assistance service is ready")

