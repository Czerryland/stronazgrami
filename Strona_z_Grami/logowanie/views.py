from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def logowanie(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.success(request, ("There Was An Error Logging In. Try again"))
            return redirect('logowanie')
    else:
        return render(request, 'authenticator/logowanie.html', {})  
def wyloguj(request):
    messages.success(request, ("You were logged out"))
    logout(request)
    return redirect('home')

def rejestracja(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have been registered"))
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'authenticator/rejestracja.html', {
        'form': form,
    })
    