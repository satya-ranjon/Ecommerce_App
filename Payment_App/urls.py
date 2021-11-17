from django.urls import path
from . import views

urlpatterns = [
    path('chackout/',views.ChackOut,name='chackout'),
    path('payment/',views.Payment,name='payment'),
    path('pay-com/',views.Complate,name='py_com'),
    path('purched/<val_id>/<tran_id>/',views.Purched,name='purched'),
    path('order-history/',views.order_view_his,name='ord_his'),
]
