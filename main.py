import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage  # Add this import for handling images

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

        # Styling
        html_message = f"""
        <html>
            <style>
                body {{
                    font-family: 'Arial', sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f5f5f5;
                }}
                header {{
                    text-align: center;
                    background-color: #E72A73;
                    color: #ffffff;
                    padding: 20px 0;
                }}
                div {{
                    background-color: #f5f5f5;
                    color: #000;
                }}
                #hidden_url {{
                    text-decoration: none;
                    color: inherit;
                }}
            </style>
            <body>
            <a id="hidden_url" href="https://play.google.com/store/apps/details?id=com.appcollection.web2app">
                <header>
                    <h1>Web2App</h1>
                    <p>Convert Websites to Android Apps</p>
                </header>
            </a>
                <div style="text-align: left;">
                    <p>Dear {{ User }},</p>
                    <p>Congratulations! Your app is ready to download. Please follow the link below:</p>
                    <p><a href="http://appcollection.in/InstantWeb2App/downloads/0101_Youtube_app.apk" style="color: blue;">Download Your App</a></p>
                    <a href="https://api.whatsapp.com/send?phone=916397285262&text=Hi%20Developer%2C%20I%20want%20to%20publish%20my%20app%20on%20Google%20Play."><p style="font-size: 14px;">Publish your app on the Play Store for just $50!</p></a>
                    <br>
                    <br>
                    <p>Subrat Gupta<br>Web2App Team</p>
                </div>
            </body>
        </html>
        """
        email_message.attach(MIMEText(html_message, 'html'))

        # Attach the logo
        with open('logo.png', 'rb') as logo:
            logo_content = logo.read()
            logo_part = MIMEImage(logo_content)
            logo_part.add_header('Content-ID', '<logo>')
            email_message.attach(logo_part)

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
recipient_email = 'isubrat@icloud.com'
subject = 'Your App is Ready to Download'
message = 'Hi,\n Please download your app by clicking link: http://appcollection.in/InstantWeb2App/downloads/0101_Youtube_app.apk'

send_email(sender_email, sender_password, recipient_email, subject, message)
