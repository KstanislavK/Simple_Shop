import os

from django.conf.global_settings import MEDIA_ROOT
from django.db import models


class CategoryList(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)
    description = models.TextField(verbose_name='Описание', default='', blank=True)
    image = models.ImageField(upload_to='category_img', blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

    def get_products_by_category(self):
        return ProductList.objects.filter(category=self.pk)


class ProductList(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)
    category = models.ForeignKey(CategoryList, verbose_name='Категория', on_delete=models.PROTECT)
    image = models.ImageField(upload_to='products_img', blank=True, default=os.path.join(MEDIA_ROOT, 'default_img.jpg'))
    price = models.DecimalField(verbose_name='Цена', blank=True, decimal_places=2, max_digits=7, default=0)
    description = models.TextField(verbose_name='Описание', max_length=512, blank=True)
    is_active = models.BooleanField(verbose_name='Активно', default=True)
    is_sale = models.BooleanField(verbose_name='Распродажа', default=False)
    sale_price = models.DecimalField(verbose_name='Цена распродажи', blank=True,
                                     decimal_places=2, max_digits=7, default=0)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.is_sale:
            self.sale_price = self.price
        super().save(*args, **kwargs)
