
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Product_App.urls')),
    # path('user_accound/',include('User_App.urls')),
    path('accound/',include('User_App.urls')),
    path('order/',include('User_Order.urls')),
    path('payment/',include('Payment_App.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)