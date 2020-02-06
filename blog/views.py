from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView


def home(request):
    context = {'title': 'Home Page'}
    return render(request, 'blog/home.html', context)


def login(request):
    context = {'title': 'Login Page'}
    return render(request, 'users/login.html', context)


