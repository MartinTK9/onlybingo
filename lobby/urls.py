from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('lobby/', views.RoomList),
    path('lobby/(?P<pk>[0-9]+)', views.RoomDetail),
]
urlpatterns = format_suffix_patterns(urlpatterns)