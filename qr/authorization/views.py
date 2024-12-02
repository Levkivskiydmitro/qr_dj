from django.shortcuts import render

# Create your views here.
def render_auth(request):
    return render(request, 'auth.html')