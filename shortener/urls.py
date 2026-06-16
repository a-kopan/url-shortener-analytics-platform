from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_link, name='generate link'),
    path('redirect/', views.redirect, name='redirect')
]