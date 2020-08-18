from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.About, name='about'),
    path('quizz/', views.Quizz, name='quizz'),
    path('contact/', views.Contact, name='contact'),
    path('apply/', views.Apply, name='apply'),
    path('logout/', views.userlogout, name='logout'),
    path('profile/', views.Profile, name='profile'),

    ]
