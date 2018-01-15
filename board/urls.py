from django.urls import path
from . import views

urlpatterns = [
    path('<int:room_id>/<str:player_name>/', views.board, name='board'),
    path('lobby/', views.lobby, name='lobby'),
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('room/', views.room, name='room'),
    path('room/<int:pk>', views.roomjoin, name='roomjoin'),
]
