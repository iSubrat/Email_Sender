import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Retrieve secrets from GitHub Secrets
smtp_host = os.environ['SMTP_HOST']
smtp_port = os.environ['SMTP_PORT']
email_username = os.environ['EMAIL_USERNAME']
email_password = os.environ['EMAIL_PASSWORD']

# Sender and recipient email addresses
sender_email = email_username
recipient_email = 'recipient@example.com'

# Create message
message = MIMEMultipart("alternative")
message["Subject"] = "Test Email from GitHub Actions"
message["From"] = sender_email
message["To"] = recipient_email

# Plain-text version of the email
text = """\
This is a test email sent from GitHub Actions."""

# HTML version of the email
html = """\
<html>
  <body>
    <p>This is a test email sent from <b>GitHub Actions</b>.</p>
  </body>
</html>
"""

# Attach both plain-text and HTML versions
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)

# Connect to SMTP server
server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()  # Identify yourself to the SMTP server
server.starttls()  # Enable TLS encryption
server.login(email_username, email_password)

# Send email
server.sendmail(sender_email, recipient_email, message.as_string())
server.quit()

print("Email sent successfully!")
