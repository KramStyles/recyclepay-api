import random

from decouple import config
from django.core.mail import send_mail


class Util:
    # Generate OTP
    @staticmethod
    def generate_otp():
        otp_code = random.randrange(100000, 999999)
        return otp_code

    @staticmethod
    def generate_password():
        letters = "abcdefghijklmnopqrstuvwxyz"
        password = ""
        for i in range(8):
            password += random.choice(letters)
        return password

    # Send email
    @staticmethod
    def send_email(data):
        email_subject = data["email_subject"]
        message = data["email_body"]
        email_from = config("EMAIL_HOST_USER", default="dummy@gmail.com")
        email_to = data["to_email"]
        html_format = data["email_body"]
        try:
            send_mail(
                email_subject,
                message,
                email_from,
                email_to,
                fail_silently=False,
                html_message=html_format,
            )
        except Exception as err:
            raise err

    # Encode text
    @staticmethod
    def encode_text(text):
        return text.encode('ibm500')

    # Decode text
    @staticmethod
    def decode_text(text):
        return text.decode('ibm500')
