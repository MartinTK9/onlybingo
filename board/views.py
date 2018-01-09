from django.shortcuts import render
from random import randint


def index(request):
    col1num = list(range(1, 16))
    col2num = list(range(16, 31))
    col3num = list(range(31, 46))
    col4num = list(range(46, 61))
    col5num = list(range(61, 76))

    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []

    def columngenerator(numbers):
        num = numbers[randint(0, 14)]
        numbers.remove(num)
        row1.append(num)
        num = numbers[randint(0, 13)]
        numbers.remove(num)
        row2.append(num)
        num = numbers[randint(0, 12)]
        numbers.remove(num)
        row3.append(num)
        num = numbers[randint(0, 11)]
        numbers.remove(num)
        row4.append(num)
        num = numbers[randint(0, 10)]
        numbers.remove(num)
        row5.append(num)

    def boardgenerator():
        columngenerator(col1num)
        columngenerator(col2num)
        columngenerator(col3num)
        columngenerator(col4num)
        columngenerator(col5num)
        row3[2] = ''
        array = [row1, row2, row3, row4, row5]

        return array

    board = boardgenerator()

    context = {
        'message': 'render test',
        'board': board,
    }
    return render(request, 'board/index.html', context)
