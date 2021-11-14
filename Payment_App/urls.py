from django.urls import path
from . import views

urlpatterns = [
    path('chackout/',views.ChackOut,name='chackout')
]
