from django.urls import path

from orderapp.views import order_create

app_name = 'orderapp'

urlpatterns = [
    path('create/', order_create, name='order_create'),
]
