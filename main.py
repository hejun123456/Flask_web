
# from web import app
#
# app.run()


from utill import *

if __name__ == '__main__':
    print("开始获取cookie的值")
    a = "这是登录后cookie的值：'shuwhdwhu242323dswd'"
    from config import *
    write_file(COOKIE_PATH, a)

    print(read_file(COOKIE_PATH))