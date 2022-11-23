from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from basketapp.forms import CartAddProductForm
from productapp.models import ProductList, CategoryList


class ProductListView(ListView):
    """ Каталог товаров """
    model = ProductList
    template_name = 'productapp/index.html'
    context_object_name = 'objects'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Каталог товаров'
        context['category_links'] = CategoryList.objects.values_list('pk', 'title')
        return context


class ProductByCategoryListView(ProductListView):
    """  Каталог товаров по категориям """
    def get_queryset(self):
        qs = ProductList.objects.filter(is_active=True)
        if self.kwargs['pk'] is not None:
            category = get_object_or_404(CategoryList, pk=self.kwargs['pk'])
            qs = qs.filter(category=category)
        return qs

    def get_context_data(self, **kwargs):
        context = super(ProductByCategoryListView, self).get_context_data(**kwargs)
        context['category'] = get_object_or_404(CategoryList, pk=self.kwargs['pk'])
        return context


class ProductDetailView(DetailView):
    """ Карточки товаров """
    model = ProductList
    template_name = 'productapp/product_detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['cat_prods'] = ProductList.objects.filter(category=self.object.category)
        context['cart_product_form'] = CartAddProductForm()
        return context


class PriceListView(ListView):
    """ Прайс-лист """
    model = CategoryList
    template_name = 'productapp/price_list.html'
    context_object_name = 'objects'

    def get_context_data(self, **kwargs):
        context = super(PriceListView, self).get_context_data(**kwargs)
        context['title'] = 'Прайс-лист'
        return context

