from django.contrib import admin
from django.urls import path, include

# noinspection PyInterpreter
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('board.urls')),
    path('api/', include('lobby.urls')),
]
