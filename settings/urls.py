from reg.views import reg
from django.urls import path
from .views import render_card

urlpatterns = [
    path('card/', render_card),
]