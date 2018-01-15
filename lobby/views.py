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
from random import randint
#API DOCUMENTATION

#API
#/Api/lobby/<pk>



class roomlist(APIView):
    def get(self,request):
        rooms = Rooms.objects.all()
        serializer=roomSerializer(rooms,many=true)
        return Response(serializer.data)
    def post(self,request):
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
            if diff.seconds>10:
                id=player.player
                PlayerBoard.objects.filter(players=id).delete()
                PlayerInfo.objects.filter(players=id).delete()
                player.delete()

        return Response("1")
    def post(self,request):
        player = request.POST('player')
        now = datetime.datetime.now()
        p, created = PlayerDateTime.objects.get_or_create(player=player)
        test.update(time=now)
        return Response(user)

class Draw(APIView):
    def get(self,request):
        Drawn.objects.all()
        latest=0
        for ball in Drawn:
            if ball.pk>latest:
                latest=ball
        ball=Drawn.objects.filter(pk=latest)
        return Response(ball)


    def post(self,request):
        serializer=DrawSerializer(data=request.data)
        i=0
        if serializer.is_valid():
            id=serializer.validated_data
            all=list(range(76))
            while (i==0):
                num= all[randint(0,74)]
                ball,created=Drawn.objects.get_or_create(num=num,room=id)
                if created==1:
                    i=1
        return Response(ball.num)