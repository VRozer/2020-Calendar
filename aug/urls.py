from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='aug_c'),
]