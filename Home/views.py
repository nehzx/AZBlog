from django.shortcuts import render, redirect, HttpResponse

from django.contrib.sessions.backends.db import SessionStore


def index(request):
    return render(request, "home/index.html")
