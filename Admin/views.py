from django.shortcuts import render, redirect, HttpResponse


# Create your views here.

def admin(request):
    pass


def login(request):
    return render(request, "admin/login.html")
