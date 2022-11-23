import smtplib
import ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.template.loader import get_template
from dotenv import load_dotenv

from mainapp.models import CompanyList

load_dotenv()


def send_mail_to_client(order, email_attrs):
    """ Отправка письма с заказом КЛИЕНТУ """
    template = get_template('orderapp/mail_for_client.html')
    context = {'object': order}
    content = template.render(context)

    msg = MIMEMultipart()
    msg['from'] = CompanyList.objects.get(pk=1).title
    msg['To'] = order.first_name
    msg['Subject'] = 'Ваш заказ'
    msg.attach(MIMEText(content, 'html'))

    try:
        with smtplib.SMTP(email_attrs['domain'], port=email_attrs['port']) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(email_attrs['sender'], email_attrs['password'])
            server.sendmail(email_attrs['sender'], order.email, msg.as_string())
    except Exception as e:
        print(e)


def send_mail_to_manager(order, email_attrs):
    """ Отправка письма с заказом МЕНЕДЖЕРУ """
    template = get_template('orderapp/mail_for_manager.html')
    context = {'object': order}
    content = template.render(context)
    company_object = CompanyList.objects.get(pk=1)

    msg = MIMEMultipart()
    msg['from'] = 'Сайт. Новый заказ'
    msg['To'] = company_object.title
    msg['Subject'] = 'Новый заказ с сайта'
    msg.attach(MIMEText(content, 'html'))

    try:
        with smtplib.SMTP(email_attrs['domain'], port=email_attrs['port']) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(email_attrs['sender'], email_attrs['password'])
            server.sendmail(email_attrs['sender'], company_object.email, msg.as_string())
    except Exception as e:
        print(e)


def send_mails(order):
    email_attrs = {
        'sender': os.getenv('EMAIL_SENDER'),
        'password': os.getenv('EMAIL_SENDER_PASSWORD'),
        'domain': os.getenv('EMAIL_SENDER_DOMAIN'),
        'port': int(os.getenv('EMAIL_SENDER_PORT')),
    }

    send_mail_to_client(order, email_attrs)
    send_mail_to_manager(order, email_attrs)
