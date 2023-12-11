import smtplib
import random
import getpass
import os
from email.mime.text import MIMEText  
from dotenv import load_dotenv


load_dotenv()

def generate_otp():
    return str(random.randint(1000000, 999999))

def send_otp_email(email, otp):
    sender_email = os.getenv("EMAIL_ADDRESS")
    sender_password = os.getenv("EMAIL_PASSWORD")

    subject = "Your OTP Code"
    body = f"Your OTP code is: {otp}"

    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, message.as_string())

def main():
    otp = generate_otp()

    user_email = input("Enter your email address: ")

    send_otp_email(user_email, otp)
    print("OTP has been send to your email.")

    user_input_otp = input("Enter the OTP received in your email: ")

    if user_input_otp == otp:
        print("OTP verification successful")
    else:
        print("Invalid OTP. Please try again.")

if __name__ == "__main__":
    main()