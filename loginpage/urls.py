from django.contrib import admin
from django.urls import path
from . import views
from .views import login_info_collect

urlpatterns = [
    path('',views.index,name='index'),
    path('login_info/',login_info_collect.as_view(),name='login_info')
]