from django.urls import path
from . import views

urlpatterns = [
    path('<int:room_id>/<str:player_name>/', views.board, name='index'),
    path('lobby', views.lobby, name='lobby'),
    path('index', views.index, name='lobby'),
]
