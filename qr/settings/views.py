from django.shortcuts import render

# Create your views here.
def render_settings(request):
    return render(request, 'settings.html')