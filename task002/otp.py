import smtplib
import random
import getpass
from email.mime.text import MIMEText

def generate_otp():
    return str(random.randint(100000, 999999))

def send_email(email, otp):
    sender_email = "johnythebonyboy@gmail.com"  # Replace with your email address
    sender_password = getpass.getpass("Enter your email password: ")

    subject = "OTP for Verification"
    body = f"Your OTP is: {otp}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = email

    try:
        with smtplib.SMTP("localhost", 1025) as server:  # Assuming MailHog is running on default port 1025
            server.sendmail(sender_email, [email], msg.as_string())
        print("OTP sent successfully.")
    except Exception as e:
        print(f"Error sending OTP: {e}")

def main():
    
    otp = generate_otp()
    user_email = input("Enter your email address: ")
    send_email(user_email, otp)
    user_input_otp = input("Enter the OTP received in your email: ")

    if user_input_otp == otp:
        print("OTP verification successful.")
    else:
        print("OTP verification failed. Please try again.")

if __name__ == "__main__":
    main()
