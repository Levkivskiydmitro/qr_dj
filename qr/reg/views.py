from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def render_reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create_user(username= username, surname=surname, email=email, password= password)
    return render(request, 'reg.html')