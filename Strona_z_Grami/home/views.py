from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.template import loader


def home(request):
    return render(request, 'home.html', {})  