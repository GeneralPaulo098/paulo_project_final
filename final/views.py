from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def home(request):
    return render(request,'home.html')

def login_home(request):
    if(request.method=='POST'):
        print('teste')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.INFO, 'bem vindo')
            return redirect('/final/home') 
        
        else:
            messages.add_message(request, messages.ERROR,'nome ou senha esta errado!')
            return render(request, 'login.html')
    else:
        return render(request,'login.html')
    
