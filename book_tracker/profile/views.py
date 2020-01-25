from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from users.models import UserProfile
from django.contrib.auth.models import User


@login_required(login_url='signin')
def profile(request):
    context = {'user': request.user}
    return render(request, 'profile.html', context)