from django.shortcuts import render

from basketapp.cart import Cart
from orderapp.email_sending import send_mails
from orderapp.forms import OrderCreateForm
from orderapp.models import OrderItemList


def order_create(request):
    """ Создание заказа и добавление его в базу """
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItemList.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])
            cart.clear()  # после создания заказа, корзина очищается
            send_mails(order)
            context = {
                'object': order,
                'title': 'Новый заказ',
            }
            return render(request, 'orderapp/order_created.html', context)

    else:
        form = OrderCreateForm
        context = {
            'object': cart,
            'form': form,
            'title': 'Новый заказ',
        }

        return render(request, 'orderapp/order_create.html', context)
