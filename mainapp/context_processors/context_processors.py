from django.shortcuts import get_object_or_404

from basketapp.cart import Cart
from mainapp.models import CompanyList


def get_contacts(request):
    return {'company': get_object_or_404(CompanyList, is_active=True)}


def cart(request):
    return {'cart': Cart(request)}
