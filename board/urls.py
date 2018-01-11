from django.urls import path
from . import views

urlpatterns = [
    path('<int:player_id>/', views.index, name='index'),
]
