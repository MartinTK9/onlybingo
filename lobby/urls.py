from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('lobby/', views.roomlist),
    path('lobby/<int:pk>', views.roomdetail),
]
urlpatterns = format_suffix_patterns(urlpatterns)