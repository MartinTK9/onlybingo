from django.http import Http404
from django.shortcuts import render
from random import randint
from .models import *


def board(request, room_id, player_id):
    name = PlayerBoard.objects.get(player_id=player_id, bool=0)

    col1num = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15']
    col2num = list(range(16, 31))
    col3num = list(range(31, 46))
    col4num = list(range(46, 61))
    col5num = list(range(61, 76))

    row0 = []
    row1 = []
    row2 = []
    row3 = []
    row4 = []

    def columngenerator(numbers):
        num = numbers[randint(0, 14)]
        numbers.remove(num)
        row0.append(num)
        num = numbers[randint(0, 13)]
        numbers.remove(num)
        row1.append(num)
        num = numbers[randint(0, 12)]
        numbers.remove(num)
        row2.append(num)
        num = numbers[randint(0, 11)]
        numbers.remove(num)
        row3.append(num)
        num = numbers[randint(0, 10)]
        numbers.remove(num)
        row4.append(num)

    def boardgenerator():
        columngenerator(col1num)
        columngenerator(col2num)
        columngenerator(col3num)
        columngenerator(col4num)
        columngenerator(col5num)
        row2[2] = ''
        array = [row0, row1, row2, row3, row4]

        return array

    def dbchecker():
        for i in name:
            dbrow0 = i.row0
            dbrow1 = i.row1
            dbrow2 = i.row2
            dbrow3 = i.row3
            dbrow4 = i.row4

        appender(row0, dbrow0)
        appender(row1, dbrow1)
        appender(row3, dbrow3)
        appender(row4, dbrow4)

        for x in range(0, 2):
            x *= 2
            row2.append(dbrow2[x:x+2])

        row2.append('')

        for x in range(2, 4):
            x *= 2
            row2.append(dbrow2[x:x+2])

        array = [row0, row1, row2, row3, row4]

        return array

    def appender(row, dbrow):
        for x in range(0, 5):
            x *= 2
            row.append(dbrow[x:x+2])

    if name:
        board = dbchecker()

    else:
        board = boardgenerator()

        strrow0 = ''.join(str(e) for e in board[0])
        strrow1 = ''.join(str(e) for e in board[1])
        strrow2 = ''.join(str(e) for e in board[2])
        strrow3 = ''.join(str(e) for e in board[3])
        strrow4 = ''.join(str(e) for e in board[4])

        player = PlayerInfo.objects.get(room_id=room_id, player_id=player_id)

        db = PlayerBoard()

        db.player_id = player
        db.row0 = strrow0
        db.row1 = strrow1
        db.row2 = strrow2
        db.row3 = strrow3
        db.row4 = strrow4
        db.bool = 0

        db.save()

    board[2][2] = 'free'

    context = {
        'board': board,
    }
    return render(request, 'board/board.html', context)


def lobby(request):
    players = PlayerInfo.objects.all()

    if request.POST.get('Nametxt', False):
        rooms = Rooms.objects.filter(name=request.POST['Nametxt'], bool=0)
    elif request.POST.get('Numberofplayerstxt', False):
        rooms = Rooms.objects.filter(players=request.POST['Numberofplayerstxt'], bool=0)
    elif request.POST.get('Ballspeedtxt', False):
        rooms = Rooms.objects.filter(speed=request.POST['Ballspeedtxt'], bool=0)
    else:
        rooms = Rooms.objects.filter(bool=0)

    context = {
        'rooms': rooms,
        'players': players,
    }

    return render(request, 'board/lobby.html', context)


def index(request):
    return render(request, 'board/index.html')


def create(request):
    return render(request, 'board/Create.html')


def room(request):

    newroom = Rooms()

    newroom.name = request.POST['name']
    newroom.speed = request.POST['speed']
    newroom.players = request.POST['players']

    newroom.save()

    player = PlayerInfo()

    player.room_id = newroom.room_id
    player.name = request.POST['player_name']

    player.save()

    players = PlayerInfo.objects.filter(room_id=newroom.room_id)

    context = {
        'host': True,
        'detail': newroom,
        'player': player,
        'players': players,
    }

    return render(request, 'board/room.html', context)


def roomjoin(request, pk, name):
    if Rooms.objects.filter(pk=pk):
        newroom = Rooms.objects.get(pk=pk)

    else:
        raise Http404

    player = PlayerInfo()

    player.room_id = pk
    player.name = name

    player.save()

    players = PlayerInfo.objects.filter(room_id=pk)

    context = {
        'host': False,
        'detail': newroom,
        'player': player,
        'players': players,
    }

    return render(request, 'board/room.html', context)


def hostboard(request):

    context = {}

    return render(request, 'board/room.html', context)
