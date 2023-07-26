import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv
PORT = 587
EMAIL_SERVER = "smtp.gmail.com"

#mytechprojects909@gmail.com
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd();
envars = current_dir/".env"
load_dotenv(envars)

print(os.getenv("EMAIL"))
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")


def send_email(subject,receiver_email,name,due_date,invoice_no,amount):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Coding is Fun",f"{sender_email}"))
    msg["To"]=receiver_email
    msg["BCC"]=sender_email

    msg.set_content(
        f"""\
        Hi {name},
        I hope you are well.
        I just wanted to drop you a quick note to remind you that {amount} USD in respect of our invoice {invoice_no} is due for payment on {due_date}.
        I would be really grateful if you could confirm that everything is on track for payment.
        Best regards
        YOUR NAME
        """
    )
    msg.add_alternative(
        f"""\
    <html>
      <body>
        <p>Hi {name},</p>
        <p>I hope you are well.</p>
        <p>I just wanted to drop you a quick note to remind you that <strong>{amount} USD</strong> in respect of our invoice {invoice_no} is due for payment on <strong>{due_date}</strong>.</p>
        <p>I would be really grateful if you could confirm that everything is on track for payment.</p>
        <p>Best regards</p>
        <p>YOUR NAME</p>
      </body>
    </html>
    """,
        subtype="html",
    )

    with smtplib.SMTP(EMAIL_SERVER,PORT) as server:
        server.starttls()
        server.login(sender_email,password_email)
        server.sendmail(sender_email,receiver_email,msg.as_string())
    
if __name__ == "__main__":
        send_email(
            subject="Invoice Remainder",
            name="Jon Doe",
            receiver_email="zoyakhatry19@gmail.com",
            due_date="11 Aug 2022",
            invoice_no="INV-21-12-009",
            amount="5",
        )