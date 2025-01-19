from django.shortcuts import render, redirect
from django.contrib.auth import logout


def render_home(request):
    return render(request, 'home.html')

def logout_user(request):
    logout(request)
    return redirect('auth')