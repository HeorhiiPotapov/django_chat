from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Room, Message


@login_required
def index(request):
    rooms = Room.objects.all()
    template_name = 'core/index.html'
    context = {
        'rooms': rooms
    }
    return render(request, template_name, context)


@login_required
def room(request, room_name):

    template_name = 'core/room.html'
    context = {
        'room_name': room_name,
        'username': request.user.username,
    }
    return render(request, template_name, context)


@login_required
def remove_chat_room(request, room_name):
    room = get_object_or_404(Room, name=room_name)
    if request.method == 'POST':
        if request.user.is_staff:
            room.delete()
            return redirect('index')
        else:
            return redirect('index')
    else:
        return redirect('index')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()

    template_name = 'core/users/register.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
    template_name = 'core/users/profile.html'
    context = {
        'user_form': user_form
    }
    return render(request, template_name, context)
