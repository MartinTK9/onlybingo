from django.urls import path,url
from . import views

urlpatterns = [
    url(r'^lobby/$', views.LobbyDetail.as_view()),
]+urlpatterns = format_suffix_patterns(urlpatterns)