from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book_event/', views.book_event, name='book_event'),
    path('view_event/', views.view_event, name='view_event'),
    path('calender_view/', views.calender_view, name='calender_view'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('testingevents/', views.testingevents, name='testingevents'),
]
