from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('programmes/', views.programmes, name='programmes'),
    path('members/', views.members, name='members'),
    path('donate/', views.donate, name='donate'),
    path('contact/', views.contact, name='contact'),
]
