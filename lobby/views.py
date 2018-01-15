from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
import datetime
from .models import *
from random import randint
from django.shortcuts import get_object_or_404
#API DOCUMENTATION

#API
#/Api/lobby/<pk>


class roomlist(APIView):
    def get(self, request):
        rooms = Rooms.objects.all()
        serializer = roomSerializer(rooms, many=true)
        return Response(serializer.data)

    def post(self, request):
        serializer = roomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# class connection(APIView):
#     def get(self, request):
#         players = PlayerDateTime.objects.all()
#         now = datetime.datetime.now()
#         seconds_since_midnight_now = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
#         for player in players:
#             last = player.time
#             seconds_since_midnight_last = (last - last.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
#             diff = seconds_since_midnight_now - seconds_since_midnight_last
#             print (diff)
#             if diff > 10:
#                 PlayerBoard.objects.filter(player=player).delete()
#                 PlayerInfo.objects.filter(player=player).delete()
#                 player.delete()
#                 return Response("1")
#
#         return Response("2")
#
#
#
#     def post(self, request):
#         pk = request.POST['player']
#         now = datetime.datetime.now()
#         player=PlayerInfo.objects.get(pk=pk)
#         p, created = PlayerDateTime.objects.get_or_create(player=player)
#         p.time = now
#         p.save()
#         return Response("2")


class Draw(APIView):
    def get(self, request, pk):
        i = 0
        all = list(range(76))
        while i == 0:
            num = all[randint(0, 74)]
            try:
                room = Rooms.objects.get(pk=pk)
            except Rooms.DoesNotExist:
                return Response("0")
            test, created = Drawn.objects.get_or_create(num=num, room=room)
            if created == 1:
                i = 1
        da = DrawnSerializer(test)
        return Response(da.data, status=status.HTTP_201_CREATED)


class gettingball(APIView):
    def get(self, request, pk):

        latest = 0
        try:
            room = Rooms.objects.get(pk=pk)
        except Rooms.DoesNotExist:
            return Response("0",status=status.HTTP_400_BAD_REQUEST)
        drawn = Drawn.objects.filter(room=room)
        for ball in drawn:
            if ball.pk > latest:
                latest = ball.pk
        ball = Drawn.objects.get(pk=latest)
        da = DrawnSerializer(ball)
        return Response(da.data, status=status.HTTP_200_OK)