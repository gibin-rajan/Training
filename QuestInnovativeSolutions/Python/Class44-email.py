import smtplib

s = smtplib.SMTP('smtp.gmail.com',587)     #create smtp session

s.starttls()                            #start transport layer security

s.login('rajangibin@gmail.com','*******')#authendication
#s.login("sender email address",'password for the same')

msg='Hi How are ya??'

s.sendmail('rajangibin@gmail.com','rajangibin@gmail.com',msg)
# s.sendmail("sender email address","receiver mail address",message we have typed)

s.quit()


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from_add = "#sender email address#"
to_add = "#receiver email address#"

msg = MIMEMultipart() #instance of mimemultipart
msg["From"]=from_add #storing sender email address
msg["To"]=to_add #storing receivers email address
msg["Subject"]="Subject of email" #storing subject

#string to store body of email
body="Body of email"
msg.attach(MIMEText(body,'plain')) #attach body with msg instance 

filename="setss.py" #filename with extension
attachment = open(filename,"rb") #open file in read&binary mode

p = MIMEBase('application', 'octet-stream') #instance of mimebase
p.set_payload((attachment).read())#to encode
encoders.encode_base64(p)   #encode into base64

p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
msg.attach(p)

s = smtplib.SMTP('smtp.gmail.com', 587)   
s.starttls()  #for security start tls      
s.login(from_add,"#Password#")
#convert multipart msg into a string
text=msg.as_string()
s.sendmail(from_add,to_add,text) #sending mail
s.quit() #terminating session