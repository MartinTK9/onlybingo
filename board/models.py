from django.db import models


class Rooms(models.Model):
    room_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    speed = models.IntegerField(default=20)
    players = models.IntegerField(default=5)

    def __str__(self):
        return str(self.room_id) + ' - ' + self.name

    class Meta:
        db_table = 'rooms'


class PlayerInfo(models.Model):
    player_id = models.AutoField(primary_key=True)
    room = models.ForeignKey('Rooms', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True)
    bool = models.BooleanField(default=0)

    def __str__(self):
        return str(self.room_id) + ' - ' + self.name

    class Meta:
        db_table = 'player_info'


class PlayerBoard(models.Model):
    player = models.ForeignKey('PlayerInfo', on_delete=models.CASCADE)
    bool = models.BooleanField(default=0)
    row0 = models.CharField(null=True, max_length=10)
    row1 = models.CharField(null=True, max_length=10)
    row2 = models.CharField(null=True, max_length=8)
    row3 = models.CharField(null=True, max_length=10)
    row4 = models.CharField(null=True, max_length=10)

    def __str__(self):
        return str(self.player_id) + ' - ' + str(self.bool)

    class Meta:
        db_table = 'player_board'
