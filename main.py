import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Retrieve secrets from GitHub Secrets
smtp_host = os.environ['SMTP_HOST']
smtp_port = os.environ['SMTP_PORT']
email_username = os.environ['EMAIL_USERNAME']
email_password = os.environ['EMAIL_PASSWORD']

def send_email(sender_email, sender_password, recipient_email, subject, message):
    try:
        # Setup the email message
        email_message = MIMEMultipart()
        email_message['From'] = sender_email
        email_message['To'] = recipient_email
        email_message['Subject'] = subject

        # Attach the message body
        email_message.attach(MIMEText(message, 'plain'))

        # Create SMTP session for sending the mail
        with smtplib.SMTP_SSL(smtp_host, smtp_port) as session:
            session.login(sender_email, sender_password)
            session.sendmail(sender_email, recipient_email, email_message.as_string())

        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
sender_email = email_username
sender_password = email_password
recipient_email = 'irojalgupta@gmail.com'
subject = 'Your App is Ready to Download'
message = 'Hi,\n Please download your app by clicking link: https://www.google.com'

send_email(sender_email, sender_password, recipient_email, subject, message)
