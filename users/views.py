from django.http import HttpRequest
from django.shortcuts import render, redirect
from urllib.request import Request

from bot.forms import BookForm
from .forms import UserRegisterForm, UserLoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def user_register(request: Request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Account created successfully for {
                             user.username}. You can now login.")
            return redirect('users:login')
        else:
            return render(request, 'users/register.html', context={'form': form})
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', context={'form': form})


def user_login(request: Request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', 'users:profile')
                messages.success(request, "Logged in successfully")
                return redirect(next_url)
        else:
            return render(request, 'users/login.html', context={'form': form})
    else:
        form = UserLoginForm()
        return render(request, 'users/login.html', context={'form': form})


def user_logout(request):
    logout(request)
    return redirect('users:login')


@login_required
def user_profile(request: HttpRequest):
    if request.method == "POST":
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        photo_update_form = ProfileUpdateForm(
            request.POST, request.FILES,
            instance=request.user.profile)

        if user_update_form.is_valid() and photo_update_form.is_valid():
            user_update_form.save()
            photo_update_form.save()
            messages.success(request, "Data updated successfully")
            return redirect('users:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        photo_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'users/profile.html',
                  context={'user_form': user_form, 'photo_form': photo_form, 'create_book_form': BookForm()})


@login_required
def create_book(request: HttpRequest):
    if request.method == "POST":
        form = BookForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"Book '{
                             form.cleaned_data['name']}' created successfully!")
            return redirect('users:create-book')
    return render(request, 'users/profile.html', context={"form": BookForm()})
