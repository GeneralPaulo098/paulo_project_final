from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages


def home(request):
    
    soma = request.session.get('soma',0)
    request.session['soma'] = soma + 1
    conta = request.session['soma']
    print(conta)
    if conta == 1:
        print(55)
        messages.add_message(request, messages.INFO, 'bem vindo')
    return render(request,'home.html')

    
