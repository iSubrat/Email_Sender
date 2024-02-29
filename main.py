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

def send_email(sender_email, sender_password, recipient_email, subject):
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
                background-color: white;
            }}
            header {{
                text-align: center;
                background-color: #E72A73;
                color: #ffffff;
                padding: 20px 0;
            }}
            div {{
                background-color: white;
                color: #000;
                font-size: 14px;
                margin: 10px;
            }}
            .button {{
                display: inline-block;
                padding: 10px 20px;
                background-color: #E72A73; /* Blue color */
                color: white;
                text-decoration: none;
                border-radius: 5px;
                font-size: 16px;
                margin-bottom: 10px;
            }}
            .button-secondary {{
                background-color: #f4be41;
                font-weight: bold;
                color: white;
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
                <p>Dear User,<br>Congratulations! Your app {{appname}} is ready to download. Please click the below button:</p>
                <a href="http://appcollection.in/InstantWeb2App/downloads/0101_Youtube_app.apk" class="button">Download Your App</a><br>
                <br>
                <p>Publish your app on the Play Store for just $50!</p>
                <a href="https://api.whatsapp.com/send?phone=916397285262&text=Hi%20Developer%2C%20I%20want%20to%20publish%20my%20app%20on%20Google%20Play." class="button button-secondary">Publish Now</a>
                <br>
                <br>
                <h4>- Subrat Gupta<br>Web2App Team</h4>
            </div>
        </body>
    </html>
        """
        email_message.attach(MIMEText(html_message, 'html'))

        # # Attach the logo
        # with open('logo.png', 'rb') as logo:
        #     logo_content = logo.read()
        #     logo_part = MIMEImage(logo_content)
        #     logo_part.add_header('Content-ID', '<logo>')
        #     email_message.attach(logo_part)

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

send_email(sender_email, sender_password, recipient_email, subject)
