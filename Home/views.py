from django.shortcuts import render, redirect, HttpResponse

from django.contrib.sessions.backends.db import SessionStore


def index(request):
    return render(request, "home/index.html")


def detaile(request):
    return render(request, "home/index.html")


def essay_list(request):
    return render(request, "home/essay_list.html")


def about(request):
    return render(request, "home/about.html")