from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .forms import SignUpForm, SignInForm


def home(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    return render(request, 'home.html')


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User()
            user.username = form.cleaned_data.get('username')
            user.email = form.cleaned_data.get('email')
            user.password = make_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('signin')
    else:
        form = SignUpForm()
    return render(request, 'users/sign_up.html', {'form': form})


def sign_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.check_user()
            if user and user.is_active:
                login(request, user)
                return redirect('home')
    else:
        form = SignInForm()
    return render(request, 'users/sign_in.html', {'form': form})


@login_required(login_url='signin')
def sign_out(request):
    logout(request)
    return render(request, 'users/sign_out.html')
