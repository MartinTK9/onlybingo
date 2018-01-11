from django.urls import path
from . import views

urlpatterns = [
    path('<str:player_name>/', views.index, name='index'),
]
