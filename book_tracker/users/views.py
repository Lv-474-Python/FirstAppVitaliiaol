from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, SignInForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


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
    return render(request, 'signup.html', {'form': form})


def sign_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignInForm(request.POST)
        username = request.POST.get('username')
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect('home')
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})


@login_required(login_url='signin')
def sign_out(request):
    logout(request)
    return render(request, 'signout.html')

