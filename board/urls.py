from django.urls import path
from . import views

urlpatterns = [
    path('<int:room_id>/<int:player_id>/', views.board, name='board'),
    path('lobby/', views.lobby, name='lobby'),
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('room/', views.room, name='room'),
    path('room/<int:pk>/<str:name>', views.roomjoin, name='roomjoin'),
    path('<int:room_id>/<int:player_id>/check/', views.dbcheck, name='dbcheck'),
    path('highscores/',views.highscores,name='highscores'),
]
