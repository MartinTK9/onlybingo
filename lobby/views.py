from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import *
from .models import *
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

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
