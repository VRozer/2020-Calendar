from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'jul_c'),
]