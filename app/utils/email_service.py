import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(recipient, subject, body):
    # """
    # Send an email using Gmail SMTP
    # """
    # # Email credentials
    # sender_email = os.getenv("EMAIL_USER")
    # password = os.getenv("EMAIL_PASSWORD")
    #
    # if not sender_email or not password:
    #     return {
    #         "success": False,
    #         "error": "Email credentials not configured"
    #     }
    #
    # try:
    #     # Create message
    #     message = MIMEMultipart()
    #     message["From"] = sender_email
    #     message["To"] = to
    #     message["Subject"] = subject
    #
    #     # Add body to email
    #     message.attach(MIMEText(body, "plain"))
    #
    #     # Connect to SMTP server
    #     with smtplib.SMTP("smtp.gmail.com", 587) as server:
    #         server.starttls()  # Secure the connection
    #         server.login(sender_email, password)
    #         server.send_message(message)
    #
    #     return {
    #         "success": True,
    #         "message": f"Email sent successfully to {to}"
    #     }
    # except Exception as e:
    #     print(f"Error sending email: {e}")
    #     return {
    #         "success": False,
    #         "error": str(e)
    #     }
    #
    """Send an email with the specified details."""
    try:
        # Get email credentials from environment variables
        sender = os.getenv("EMAIL_USERNAME")
        password = os.getenv("EMAIL_PASSWORD")
        smtp_server = os.getenv("SMTP_SERVER")
        smtp_port = int(os.getenv("SMTP_PORT"))

        # Create message
        message = MIMEMultipart()
        message["From"] = sender
        message["To"] = recipient
        message["Subject"] = subject

        # Attach body text
        message.attach(MIMEText(body, "plain"))

        # Connect to server and send
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender, password)
            server.send_message(message)


        print("SYSTEM: send email", recipient, subject, body)

        return {"success": True, "message": f"Email sent to {recipient}"}
    except Exception as e:
        return {"status": "error", "message": f"Failed to send email: {str(e)}"}

