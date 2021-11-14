from django.urls import path
from . import views

urlpatterns = [
    # path('',views.Shop, name='shop'),
    path('',views.Home.as_view(), name='shop'),
    path('product-detiels/<pk>/',views.ProductDitels.as_view(), name='product_detiels'),
]
