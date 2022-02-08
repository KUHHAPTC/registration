from django.core.mail import send_mail
from registration.celery import app
from registration.settings import EMAIL_HOST_USER


@app.task
def task_send_mail(uri, uid64, token, user_email):
    to_send = f"Link to activate your account: {uri}{uid64}/{token}"
    print(to_send, user_email)
    mail_subject = 'Activate your account.'
    send_mail(mail_subject, to_send, EMAIL_HOST_USER, [user_email])
