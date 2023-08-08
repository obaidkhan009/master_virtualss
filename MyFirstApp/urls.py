from django.contrib import admin
from django.urls import path ,include
from MyFirstApp import views
urlpatterns = [
   
    path("", views.home, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path('login/', views.admin_login, name='admin_login'),
    path('client_forms/', views.client_forms, name='client_forms'),
    path('create_admin/', views.create_admin, name='create_admin'),
    path('login/', views.login_view, name='login'),
   
]
