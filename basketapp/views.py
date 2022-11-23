from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from productapp.models import ProductList
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, pk):
    """Создание корзины"""
    cart = Cart(request)
    product = get_object_or_404(ProductList, pk=pk)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            update_quantity=cd['update']
        )

    return redirect('basketapp:cart_detail')


def cart_remove(request, pk):
    """ Удаление корзины """
    cart = Cart(request)
    product = get_object_or_404(ProductList, id=pk)
    cart.remove(product)
    return redirect('basketapp:cart_detail')


def cart_detail(request):
    """ Детали корзины """
    cart = Cart(request)
    return render(request, 'basketapp/cart_detail.html', {'object': cart})
