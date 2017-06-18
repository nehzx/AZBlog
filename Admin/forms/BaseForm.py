#! /usr/bin/env python3
# encoding: utf-8
"""
    BaseForm.py
Created by AZBlog on 2017/6/18 下午7:33
Copyright 2017 azhen All rights reserved.
"""


class BaseForm(object):
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(BaseForm, self).__init__(*args, **kwargs)