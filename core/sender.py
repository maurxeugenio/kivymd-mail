#! /usr/bin/python3

# aqui a magia acontece usamos uma biblioteca propria do python3 para mandar os email
# esta configurado para enviar sempre do gmail

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def mail(*args):

    msg = MIMEMultipart('alternative')
    msg['Subject'] = args[0][3]
    msg['From'] = args[0][1]
    msg['To'] = args[0][4]
    text = args[0][5]

    part1 = MIMEText(text, 'plain')
    msg.attach(part1)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    password = args[0][2]
    s.login(args[0][1], password)

    s.sendmail(args[0][1], args[0][4], msg.as_string())
    s.quit()
