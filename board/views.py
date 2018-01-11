from django.shortcuts import render
from random import randint
from .models import Player


def index(request, player_name):
    name = Player.objects.filter(name=player_name, bool=0)

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

        db = Player()

        db.room_id = 1
        db.name = player_name
        db.row0 = strrow0
        db.row1 = strrow1
        db.row2 = strrow2
        db.row3 = strrow3
        db.row4 = strrow4
        db.bool = 0

        db.save()

    context = {
        'message': 'render test',
        'board': board,
    }
    return render(request, 'board/index.html', context)
