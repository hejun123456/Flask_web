#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/30 14:27
# @Author : he jun
# @File : web.py

from flask import Flask

app = Flask(__name__)


@app.route("/index")
def index():
    return "Hello World"


@app.route("/login")
def login():
    return "登录成功"

