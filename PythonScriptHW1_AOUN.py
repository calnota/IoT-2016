#### Carlotta Aoun, HW1
#### Create a Python script that takes 3 arguments from terminal, does some processing on the arguments, and emails the results to yourself using the Python mailer script.


import random
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


def XenoPoet(a,b,c):
    
    a=raw_input(" type an absurd experimental object ")
    b=raw_input(" type something that transcends visibility or that incites devotion ")
    c=raw_input(" type a weird or unexpected noun in its plural form ")
    
    one=[" An experimental ", " An algorithmic ", " An embedded "]
    two=[" uncovering the invisible ", " exploring the dark side of ", " mocking technological "]
    three=[" of transhumanist ", " while collecting Internet ", " of empathetic "]
    
    fromaddr = "youremail@gmail.com"
    toaddr = "anotheremail@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Congratulations! You are a XenoPoet!"
    body = "THIS POETIC SEQUENCE IS INPIRED BY NICOLAS MAIGRET'S PREDICTIVE ART BOT: @PREDARTBOT. YOU ARE NOW A XENOPOET: A MACHINE INCITES YOU TO THINK LIKE A POET AND GENERATES A UNIQUE POETIC SENTENCE OUT OF YOUR ANSWERS. HERE IS YOUR UNIQUE POETIC SENTENCE: "+(random.choice(one))+str(a)+(random.choice(two))+str(b)+(random.choice(three))+str(c)
    msg.attach(MIMEText(body,'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "***yourpassword***")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()



XenoPoet(1,2,3)



