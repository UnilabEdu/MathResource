from flask_mail import Message
import threading
from itsdangerous import URLSafeSerializer
from src.config import TestConfig
from src.extensions import mail
from flask import render_template
import os

def send_mail(receiver, text):
    msg = Message("Email Confirmation",
                  sender="Mathrecourse@gmail.com",
                  recipients=[receiver])
    msg.html = text

    return threading.Thread(mail.send(msg))


def generate_confirmation_token(email):
    serializer = URLSafeSerializer(TestConfig.SECRET_KEY)
    return serializer.dumps(email, salt=TestConfig.SECURITY_PASSWORD_SALT)


def confirm_token(token, expiration=3600):
    serializer = URLSafeSerializer(TestConfig.SECRET_KEY)
    try:
        email = serializer.loads(
            token,
            salt=TestConfig.SECURITY_PASSWORD_SALT,
            max_age=expiration
        )
    except:
        return "Invalid Token I think"

    return email

