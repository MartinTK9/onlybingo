from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import *
from .models import *

from django.http import Http404

from .models import *

#API DOCUMENTATION

#API
#/Api/lobby/<pk>


def roomdetail(request, pk):
    if request.method == 'GET':
        obj = PlayerInfo.objects.get(pk=pk)
        return HttpResponse(obj)
    if request.method == 'POST':
        name = request.POST('name')
        return HttpResponse(name)
    return HttpResponse('hi')


def roomlist(request):
    if request.method == 'GET':
        obj = Rooms.objects.all()
        return HttpResponse(obj)
    if request.method == 'POST':
        name = request.POST('name')
        speed = request.POST('speed')
        players = request.POST('players')
        new = Rooms(name=name, speed=speed, players=players)
        new.save()
        return HttpResponse(new)
