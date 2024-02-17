from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('interests/', views.interests, name='interests'),
    path('contact/', views.contact, name='contact'),
    path('versailles/', views.versailles, name='versailles'),
]