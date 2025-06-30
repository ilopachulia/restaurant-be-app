
from django.urls import path
from products import views

urlpatterns = [
    path('', views.get_products, name='products'),
    path('create', views.add_product, name='add_product'),

]

