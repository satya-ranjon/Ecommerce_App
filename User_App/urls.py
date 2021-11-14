from django.urls import path
from User_App import views


urlpatterns = [
    path('',views.Sign_Up, name='sign_up'),
    path('login/',views.Login_User, name='login'),
    path('logout/',views.Logout_User, name='logout'),
    path('user-change-profile/',views.User_Ch_Profile, name='user_ch_pro'),
    path('change-password',views.Change_Password, name='change_password'),
]
