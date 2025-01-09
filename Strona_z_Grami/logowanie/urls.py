from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('logowanie/', views.logowanie, name='logowanie'),
    path('wylogowanie/', views.wyloguj, name='wyloguj'),
    path('rejestracja/', views.rejestracja, name='rejestracja'),
]
