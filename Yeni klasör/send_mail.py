import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(toMail, subject , context):

    fromMail ="mail"
    server=smtplib.SMTP("smtp.gmail.com",587)

    server.starttls()

    server.login(fromMail,"sifre")

    message =MIMEMultipart('alternative')
    message['Subject']=subject


    htmlContent =MIMEText(context,'html')
    message.attach(htmlContent)

    server.sendmail(
        fromMail,
        toMail,
        message.as_string()
    )
    server.quit()