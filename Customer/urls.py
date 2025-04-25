from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('booking/', views.booking, name='booking'),
    path('about/', views.about, name='about'),
    path('cont/', views.cont, name='cont'),
    path('hi/', views.hi, name='hi'),
    path('m/', views.mail, name='mail'),
    path('mail/', views.index, name='index'),

]
