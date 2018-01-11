from django.urls import path,url
from attend import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^lobby/$', views.LobbyList.as_view()),
    url(r'^lobby/(?P<pk>[0-9]+)$', views.LobbyDetail.as_view()),
]+urlpatterns = format_suffix_patterns(urlpatterns)