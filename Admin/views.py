from django.shortcuts import render, redirect, HttpResponse
from django import forms
from Admin import models
import json
from Admin.forms.account import LoginForm


# Create your views here.

def admin(request):
    return render(request, "admin/admin.html")


class User(forms.Form):
    pass


def login(request):
    if request.method == "GET":

        return render(request, "admin/login.html")

    elif request.method == "POST":

        result = {"status": None, "message": None, "data": None}
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user_info = models.UserProfile.objects. \
            filter(username=username, password=password). \
            values("user_info__nick_name", "user_info__email",
                   "user_info__phone", "user_info__user_type"). \
            first()
        print(user_info)
        if not user_info:
            result['message'] = "账号密码错误"
        else:
            result['status'] = True
            request.session["user_info"] = user_info
            if request.POST.get("is_remember") == "no":
                request.session.set_expiry(60 * 60 * 24 * 7)
        return HttpResponse(json.dumps(result))
