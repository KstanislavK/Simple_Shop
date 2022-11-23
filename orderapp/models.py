from django.db import models

from productapp.models import ProductList


class OrderList(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=128)
    email = models.EmailField(verbose_name='E-mail')
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=15)
    comment = models.TextField(verbose_name='Коментарий', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ № {self.pk}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_orders_products(self):
        return OrderItemList.objects.filter(order=self.pk)


class OrderItemList(models.Model):
    order = models.ForeignKey(OrderList, related_name='items', on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(ProductList, related_name='order_items', on_delete=models.PROTECT, verbose_name='Товар')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f'{self.pk}'

    def get_cost(self):
        return self.price * self.quantity

