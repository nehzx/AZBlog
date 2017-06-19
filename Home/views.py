from django.shortcuts import render, redirect, HttpResponse

from django.contrib.sessions.backends.db import SessionStore


# Create your views here.

def index(request):

    return render(request, "home/index.html")
