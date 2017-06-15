from django.shortcuts import render, redirect, HttpResponse


# Create your views here.

def index(request):

    print(request.environ.get("HTTP_USER_AGENT"))

    return render(request, "home/index.html")
