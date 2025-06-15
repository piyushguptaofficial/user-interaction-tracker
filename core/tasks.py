from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(username, email):
    subject = 'Welcome to User Interaction Tracker'
    message = f'Hello {username},\n \n Thanks for registering!'
    from_email = 'noreply@gmail.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    