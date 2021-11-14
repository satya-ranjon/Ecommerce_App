from django.urls import path
from . import views


urlpatterns = [
    path('add/<pk>/',views.Add_to_cart, name='add'),
    path('card/',views.Cart_Views, name='card'),
    path('card-removed/<pk>/ ',views.Remove_Card_Item, name='remove_card'),
    path('increse/<pk>/ ',views.Increase_Card, name='increse'),
    path('decrese/<pk>/ ',views.Decrese_Cart, name='decrese'),
]