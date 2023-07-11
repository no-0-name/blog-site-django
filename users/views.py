from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm


def signup_view(request):
    msg = None
    success = False
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('articles:list')
        else:
            messages.error(request, 'Form is not valid.')
    else:
        form = SignUpForm()

    return render(request, 'users/signup.html', {'form': form, 
                                                 'msg': msg, 
                                                 'success': success})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if not request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
                if user is not None:
                    login(request, user)
                    return redirect('articles:list')
                else:
                    messages.error(request, 'Invalid credentials.')
            else:
                messages.error(request, 'Error validating the form.')
        return render(request, 'users/login.html', {'form': form, 
                                                    'msg': msg})


def logout_view(request):
    logout(request)
    return redirect('articles:list')