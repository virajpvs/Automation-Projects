import smtplib
import ssl
from email.message import EmailMessage

subject = "email form python"
body = "this is a test email from python"
sender_email = "mlapplication71@gmail.com"
receiver_email = "mlapplication71@gmail.com"
password = input("enter password: ")

message = EmailMessage()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
message.set_content(body)

context = ssl.create_default_context()

print("sending email...")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("email sent successfully")
