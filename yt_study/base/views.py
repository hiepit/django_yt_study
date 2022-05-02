from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'base/home.html')

def Room(request):
    return render(request , 'base/room.html')