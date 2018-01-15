from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import *
from .models import *
from rest_framework.views import APIView
from django.http import *
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
    def get(self, request):
        rooms = Rooms.objects.all()
        serializer = roomSerializer(rooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = roomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class connection(APIView):
    def get(self, request):
        PlayerDateTime.objects.all()
        now = datetime.datetime.now()
        for player in PlayerDateTime:
            last = player.time
            diff = now-last
            if diff.seconds>10:
                id = player.player
                PlayerBoard.objects.filter(players=id).delete()
                PlayerInfo.objects.filter(players=id).delete()
                player.delete()

        return Response("1")

    def post(self, request):
        player = request.POST('player')
        now = datetime.datetime.now()
        p, created = PlayerDateTime.objects.get_or_create(player=player)
        test.update(time=now)
        return Response(user)


class Draw(APIView):
    def get(self, request, pk):
        i = 0
        all = list(range(76))
        while i == 0:
            num = all[randint(0, 74)]
            room = Rooms.objects.get(pk=pk)
            test, created = Drawn.objects.get_or_create(num=num, room=room)
            if created == 1:
                i = 1
        da=DrawnSerializer(test)
        return Response(da.data, status=status.HTTP_201_CREATED)


        # for ball in drawn:
        #     if ball.pk > latest:
        #         latest = ball
        # ball = Drawn.objects.filter(pk=latest)
        # return Response(ball)