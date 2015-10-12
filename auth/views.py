from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User

from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('musicd:index'))
        form = LoginForm(request.POST)
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('musicd:index'))

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password)
        if user is not None:
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('musicd:index'))
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()

    return render(request, 'auth/signup.html', {'form': form})
