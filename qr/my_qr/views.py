from django.shortcuts import render

# Create your views here.
def render_my_qr(request):
    return render(request, 'qr.html')