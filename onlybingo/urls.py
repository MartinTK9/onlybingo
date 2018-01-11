from django.contrib import admin
from django.urls import url, include

# noinspection PyInterpreter
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^board/', include('board.urls')),
    url(r'^API/',include('lobby.urls'))
]
