import json
import logging

from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from blog.models import Profile
from decorators import authentication_required, paginate
from .chatroom_deco import update_record, create_record, delete_record
from .forms import RoomForm
from .models import Room, Message, PrivateChat, PrivateMessage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


logger = logging.getLogger(__name__)


def rooms(request):
    all_rooms = Room.objects.all()
    return render(request, 'rooms.html', {'all_rooms': all_rooms})


@create_record(Room, RoomForm, 'room_form.html', 'rooms', redirect_id=None)
def create_room(request):
    pass


@update_record(Room, RoomForm, 'room_form.html', 'rooms', redirect_id=None)
def update_room(request, pk):
    pass


@delete_record(Room, 'rooms', redirect_id=None)
def delete_room(request, pk):
    pass


def users_list(request):
    all_users = User.objects.prefetch_related(
        Prefetch('profile', queryset=Profile.objects.all())
    )
    return render(request, 'users_list.html', {'all_users': all_users})


def open_room(request, slug):
    room = get_object_or_404(Room, slug=slug)
    messages = Message.objects.filter(room=room).order_by('created_on')
    return render(request, 'room.html', {
        'room': room,
        'messages': messages,
        'slug': slug,
        'username': request.user.username,
    })


@csrf_exempt
def send_message(request, room_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            content = data.get('content')
            user = request.user  # Assuming the user is authenticated
            room = get_object_or_404(Room, id=room_id)  # Get the chat room

            # Create and save the message
            message = Message.objects.create(content=content, user=user, room=room)
            message.save()

            logger.info('Message sent successfully')
            return JsonResponse({'status': 'success', 'message': 'Message sent successfully'})
        except Exception as e:
            logger.error(f'Error sending message: {e}')
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        logger.error('Invalid request method')
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


@authentication_required
def start_private_chat(request, user_id):
    user1 = request.user
    user2 = get_object_or_404(User, id=user_id)
    if user1 != user2:
        chat, created = PrivateChat.objects.get_or_create(user1=min(user1, user2, key=lambda u: u.id), user2=max(user1, user2, key=lambda u: u.id))
        messages = PrivateMessage.objects.filter(chat=chat).order_by('created_on')  # Fetch messages for the chat
        return render(request, 'private_chat.html', {'chat': chat, 'messages': messages, 'user2': user2})
    else:
        return JsonResponse({'status': 'error', 'message': 'You cannot chat with yourself.'})



@authentication_required
@csrf_exempt
def send_private_message(request, chat_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            content = data.get('content')
            sender = request.user
            chat = get_object_or_404(PrivateChat, id=chat_id)

            # Create and save the message
            message = PrivateMessage.objects.create(chat=chat, sender=sender, content=content)
            message.save()

            return JsonResponse({'status': 'success', 'message': 'Message sent successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)