#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/30 16:16
# @Author : he jun
# @File : config.py


import os


BASE_PATH = os.path.dirname(os.path.abspath(__file__))

COOKIE_PATH = os.path.join(os.path.join(BASE_PATH, 'authentication'), 'cookie.txt')


