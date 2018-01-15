from rest_framework import serializers
from .models import *

class roomSerializer(serializers.ModelSerializer):
    class Meta:
        model= Rooms
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model= PlayerInfo
        fields = '__all__'

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model= PlayerBoard
        fields = '__all__'

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model= PlayerDateTime
        fields = ('player')