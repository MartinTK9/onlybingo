from django.db import models


class Rooms(models.Model):
    room_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.room_id) + ' - ' + self.name


class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    room = models.ForeignKey('Rooms', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.player_id) + ' - ' + str(self.room_id)
