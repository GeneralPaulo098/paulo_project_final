from django.shortcuts import render
from django.contrib.auth.models import User


def home(request):
    return render(request,'home.html')
    messages.add_message(request, messages.INFO, 'bem vindo')
