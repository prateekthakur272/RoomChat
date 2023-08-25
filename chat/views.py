from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse
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


def send(req):
    message = req.POST['message']
    username = req.POST['username']
    room_id = req.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()

    return HttpResponse('Message sent')


def get_messages(req, room):

    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)

    return JsonResponse({'messages': list(messages.values())})
