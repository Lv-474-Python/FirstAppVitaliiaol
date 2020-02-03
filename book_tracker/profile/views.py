from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import EditUserInfo, EditUserProfile, ChangeUserPassword


@login_required(login_url='signin')
def view_profile(request):
    context = {'user': request.user}
    return render(request, 'profile/profile.html', context)


@login_required(login_url='signin')
def edit_profile(request):
    if request.method == "POST":
        info_form = EditUserInfo(request.POST, instance=request.user)
        profile_from = EditUserProfile(request.POST, instance=request.user.userprofile)
        if info_form.is_valid() and profile_from.is_valid():
            user_info_form = info_form.save()
            user_profile_form = profile_from.save(False)
            user_profile_form.user = user_info_form
            user_profile_form.save()
            return redirect('profile')
    info_form = EditUserInfo(instance=request.user)
    profile_from = EditUserProfile(instance=request.user.userprofile)
    context = {'info_form': info_form, 'profile_form': profile_from}
    return render(request, 'profile/edit_profile.html', context)


@login_required(login_url='signin')
def change_password(request):
    if request.method == "POST":
        form = ChangeUserPassword(request.POST)
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        user = User.objects.get(username=request.user.username)
        if not user.check_password(old_password):
            form.flag_old_password()
        if form.is_valid():
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    form = ChangeUserPassword()
    return render(request, 'profile/change_password.html', {'form': form})
