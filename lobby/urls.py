from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('lobby/', views.LobbyList),
    # path('lobby/(?P<pk>[0-9]+)', views.LobbyDetail),
]
urlpatterns = format_suffix_patterns(urlpatterns)