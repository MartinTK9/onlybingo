from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import *
from .models import *
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
import datetime
from .models import *

#API DOCUMENTATION

#API
#/Api/lobby/<pk>



class roomlist(APIView):
    def get(selfs,request):
        rooms = Rooms.objects.all()
        serializer=roomSerializer(rooms,many=true)
        return Response(serializer.data)
    def post(selfs,request):
        serializer=roomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

class connection(APIView):
    def get(self,request):
        PlayerDateTime.objects.all()
        now = datetime.datetime.now()
        for player in PlayerDateTime:
            last = player.time
            diff=  now-last
            time_s = diff.seconds
            if diff.seconds>10:
                id=player.player
                PlayerBoard.objects.filter(players=id).delete()
                PlayerInfo.objects.filter(players=id).delete()
                player.delete()

        return Response("1")
    def post(self,request):
        player = request.POST('player')
        now = datetime.datetime.now()
        user.player, created = PlayerDateTime.objects.get_or_create(player=player)
        user.update(time=now)


