from django.shortcuts import render, redirect, HttpResponse
from django import forms


# Create your views here.

def admin(request):
    pass


class User(forms.Form):
    pass


def login(request):
    return render(request, "admin/login.html")
