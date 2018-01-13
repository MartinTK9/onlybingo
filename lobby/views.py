from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import *
from .models import *

from django.http import Http404

from .models import *



#API DOCUMENTATION

#API
#/Api/lobby/<pk>
def RoomDetail(request,pk):
    if request.method == 'GET':
        list = PlayerInfo.objects.get(pk=pk)
        return HttpResponse(list)
    if request.method == 'POST':
        name = request.POST('name')
        return HttpResponse(name)
    return HttpResponse('hi')

def RoomList(request):
    if request.method == 'GET':
        list = Rooms.objects.all()
        return HttpResponse(list)
    if request.method == 'POST':
        name = request.POST('name')
        speed = request.POST('speed')
        players = request.POST('players')
        new = Rooms(name = name,speed=speed,players=players)
        new.save()
        return HttpResponse(new)
