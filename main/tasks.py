from django.core.mail import send_mail
import stackOverflowApi
from stackOverflowApi._celery import app


@stackOverflowApi._celery.app.task()
def notify_user_task(email):
    send_mail(
        'вы создали новый запрос',
        'Спасибо за испоьзование нашего сайта',
        'test@gmail.com',
        [email, ]
    )
    return 'Success'
