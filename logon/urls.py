from django.conf.urls import url
from django.urls import path
from logon import views

app_name = 'logon'

urlpatterns=[
    path('register',views.register,name='register'),
    path('user_login',views.user_login,name='user_login'),
]