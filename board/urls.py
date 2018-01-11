from django.urls import path
from . import views

urlpatterns = [
    path('<int:room_id>/<str:player_name>/', views.index, name='index'),
]
