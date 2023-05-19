from django.contrib import admin
from django.urls import path
from .views import landingview, loginview, login_action, logout_action

urlpatterns = [
    #Main page
    path('', landingview),


    #Login
    path('please_login/', loginview),
    path('login/', login_action),
    path('logout', logout_action),

]