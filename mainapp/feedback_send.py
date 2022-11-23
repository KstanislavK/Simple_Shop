import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.template.loader import get_template
from dotenv import load_dotenv

from mainapp.models import CompanyList, FeedbackList

load_dotenv()


def feedback_send(fb_id):
    """ Отправка формы обратной связи """
    email_attrs = {
        'sender': os.getenv('EMAIL_SENDER'),
        'password': os.getenv('EMAIL_SENDER_PASSWORD'),
        'domain': os.getenv('EMAIL_SENDER_DOMAIN'),
        'port': int(os.getenv('EMAIL_SENDER_PORT')),
    }

    feedback_obj = FeedbackList.objects.get(pk=fb_id)

    template = get_template('mainapp/feedback_send.html')
    context = {'object': feedback_obj}
    content = template.render(context)
    company_object = CompanyList.objects.get(pk=1)

    msg = MIMEMultipart()
    msg['from'] = 'Сайт. Обратная связь'
    msg['To'] = company_object.title
    msg['Subject'] = 'Новое сообщение'
    msg.attach(MIMEText(content, 'html'))

    try:
        with smtplib.SMTP(email_attrs['domain'], port=email_attrs['port']) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(email_attrs['sender'], email_attrs['password'])
            server.sendmail(email_attrs['sender'], company_object.email, msg.as_string())
    except Exception as e:
        print(e)
