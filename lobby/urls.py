from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('lobby/', views.roomlist.as_view()),
    # path('lobby/<int:pk>', views.roomdetail.as_view()),
    path('draw/', views.Draw.as_view()),
    path('connect/', views.connection.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)