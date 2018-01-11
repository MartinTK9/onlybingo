from django.db import models


class Rooms(models.Model):
    room_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.room_id) + ' - ' + self.name


class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    room = models.ForeignKey('Rooms', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True)
    bool = models.BooleanField(default=0)
    row0 = models.CharField(null=True, max_length=10)
    row1 = models.CharField(null=True, max_length=10)
    row2 = models.CharField(null=True, max_length=8)
    row3 = models.CharField(null=True, max_length=10)
    row4 = models.CharField(null=True, max_length=10)

    def __str__(self):
        return str(self.room_id) + ' - ' + self.name

