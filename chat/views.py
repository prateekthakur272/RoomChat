from django.shortcuts import render, redirect
from .models import Room
# Create your views here.


def home(req):
    return render(req,'home.html')


def get_room(req, room):
    username = req.GET.get('username')
    room_details = Room.objects.get(name=room)
    context = {
        'username': username,
        'room': room,
        'room_details': room_details
    }
    return render(req, 'room.html', context)


def check_room(req):
    room = req.POST['room_name']
    username = req.POST['username']

    if not Room.objects.filter(name=room).exists():
        new_room = Room.objects.create(name=room)
        new_room.save()

    # return redirect('home')
    return redirect(f'/{room}/?username={username}')
