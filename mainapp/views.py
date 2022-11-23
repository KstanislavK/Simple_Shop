from django.shortcuts import render, get_object_or_404

from .feedback_send import feedback_send
from .forms import FeedbackForm
from .models import CompanyList


def index(request):
    """ Главная страница сайта """
    return render(request, 'mainapp/index.html')


def contacts(request):
    """ Страница контакты """
    company = get_object_or_404(CompanyList, is_active=True)
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save()
            feedback_send(feedback.pk)

            context = {
                'title': 'Сообщение отправлено',
                'name': form.data['name'],
                'message': form.data['message'],
            }

            return render(request, 'mainapp/feedback_sent.html', context)

    context = {
        'title': 'Контакты',
        'object': company,
    }
    return render(request, 'mainapp/contacts.html', context)
