from django.contrib import admin
from django.urls import path, include

# noinspection PyInterpreter
urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')),
    path('API/', include('lobby.urls')),
]
