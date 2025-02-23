from django.shortcuts import render
from .forms import CardForm
from .models import Card

# Create your views here.
def render_card(request):
    form = CardForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            form.save()

    return render(request, 'card.html', context={'form': form})

def render_settings(request):
    return render(request, 'settings.html')