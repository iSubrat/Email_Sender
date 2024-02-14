# Importing the Required Modules
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_host = os.environ['SMTP_HOST']
smtp_port = os.environ['SMTP_PORT']
email_username = os.environ['EMAIL_USERNAME']
email_password = os.environ['EMAIL_PASSWORD']

# Defining the send_email Function
def send_email(sender_email, receiver_email, subject, message, smtp_server, smtp_port, smtp_username, smtp_password):
    # Create a multipart message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    # Add body to the email
    msg.attach(MIMEText(message, "plain"))

    # try:
    # Create a secure SSL/TLS connection to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.connect(smtp_server, smtp_port)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Login to the SMTP server
    server.login(smtp_username, smtp_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())

    # Close the SMTP connection
    server.quit()

    print("Email sent successfully!")
    # except Exception as e:
    #     print("Failed to send email. Error:", str(e))

# Creating all the parameters
sender_email = "web2app@appcollection.in"
receiver_email = "isubrat@icloud.com"
subject = "Hello from Python!"
message = "This is a test email sent from Python."

smtp_server = smtp_host
smtp_port = smtp_port
smtp_username = email_username
smtp_password = email_password

# Call the function
send_email(sender_email, receiver_email, subject, message, smtp_server, smtp_port, smtp_username, smtp_password)
