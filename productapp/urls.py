from django.urls import path

from .views import ProductByCategoryListView, ProductListView, ProductDetailView, PriceListView

app_name = 'productapp'

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('cat/<int:pk>', ProductByCategoryListView.as_view(), name='products_by_category'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='products_detail'),
    path('price_list', PriceListView.as_view(), name='price_list'),
]
