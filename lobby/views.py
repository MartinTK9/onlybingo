from rest_framework.views import APIView
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
        serializer = roomSerializer(rooms, many=true)
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
        players = PlayerDateTime.objects.all()
        now = datetime.datetime.now()
        for player in players:
            last = player.time
            diff = now-last
            if diff.seconds > 10:
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
        da = DrawnSerializer(test)
        return Response(da.data, status=status.HTTP_201_CREATED)


class gettingball(APIView):
    def get(self, request, pk):
        latest = 0
        room = Rooms.objects.get(pk=pk)
        drawn = Drawn.objects.filter(room=room)
        for ball in drawn:
            if ball.pk > latest:
                latest = ball.pk
        ball = Drawn.objects.get(pk=latest)
        da = DrawnSerializer(ball)
        return Response(da.data, status=status.HTTP_200_OK)