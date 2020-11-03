from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'chat_app/index.html')

def room(request, room_name):
    return render(request, 'chat_app/room.html', {
        'room_name': room_name
    })
