#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/30 16:04
# @Author : he jun
# @File : utill.py


#将登录后的cookie写入文件
def write_file(file, txt):
    with open(file, 'w', encoding="utf-8") as f:
        f.write(txt)
    return file

# 读取cookie
def read_file(file):
    with open(file, "r", encoding="utf-8") as f:
        file_txt = f.read()
    return file_txt


if __name__ == '__main__':
    a = "这是登录后cookie的值"
    from config import *
    write_file(COOKIE_PATH, a)

    print(read_file(COOKIE_PATH))