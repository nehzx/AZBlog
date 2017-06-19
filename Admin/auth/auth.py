#! /usr/bin/env python3
# encoding: utf-8
"""
    auth.py
Created by AZBlog on 2017/6/19 下午3:09
Copyright 2017 azhen All rights reserved.
"""

from django.shortcuts import redirect


def check_login(func):
    def inner(request, *args, **kwargs):
        if request.session.get('user_info'):
            return func(request, *args, **kwargs)
        else:
            return redirect('/admin/login.html')

    return inner
