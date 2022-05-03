from django.shortcuts import render
from .models import Room

# rooms = [
#     {'id': 1, 'name': 'python'},
#     {'id': 2, 'name': 'java'},
#     {'id': 3, 'name': 'c'},
#     {'id': 4, 'name': 'c++'},
#     {'id': 5, 'name': 'js'},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id = pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)
