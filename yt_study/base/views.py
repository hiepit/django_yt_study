from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'python'},
    {'id': 2, 'name': 'java'},
    {'id': 3, 'name': 'c'},
    {'id': 4, 'name': 'c++'},
    {'id': 5, 'name': 'js'},

]

def Home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def Room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
            break

    context = {'room': room}
    return render(request, 'base/room.html', context)
