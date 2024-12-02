from django.shortcuts import render

# Create your views here.
def render_gen_qr(request):
    return render(request, 'gen.html')