import PySimpleGUI as sg
import sys
import datetime
import random

user_information = {}
loginmain = False


def loadfile(file_path):
    information = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # 解析文件中的每一行，将信息添加到字典中
                parts = line.strip().split(', ')
                username = parts[0].split(': ')[1]
                password = parts[1].split(': ')[1]
                login_count = int(parts[2].split(': ')[1])
                registration_time_str = parts[3].split(': ')[1]

                # 将字符串时间转换为datetime对象
                registration_time = datetime.datetime.strptime(registration_time_str, '%Y-%m-%d %H:%M:%S.%f')

                information[username] = {
                    'password': password,
                    'login_count': login_count,
                    'registration_time': registration_time
                }
        return information
    except FileNotFoundError:
        return {}


def savefile(information, file_path):
    with open(file_path, 'w') as file:
        for username, data in information.items():
            file.write(
                f"用户名: {username}, 密码: {data['password']}, 登录次数: {data['login_count']}, 注册时间: {data['registration_time']}\n")


# 保存字典到txt




# 注册页面
user_information = loadfile('C:\\Users\\Administrator\\Desktop\\user_information.txt')


def denglu():
    sg.theme('LightGrey')
    layout1 = [[sg.Text('用户名'), sg.InputText('Naomi502')],
               [sg.Text('密码    '), sg.InputText()],
               [sg.Button('登陆'), sg.Button('注册'), sg.Button('退出')]]

    layout2 = [[],
               [sg.Button('登出'), sg.Button('温度转换'), sg.Button('随机数生成'), sg.Button('显示账户信息'),
                sg.Button('查看排行榜')],
               []]
    layout3 = [[sg.Text('用户名'), sg.InputText('Naomi502')],
               [sg.Text('密码    '), sg.InputText()],
               [sg.Button('注册账户'), sg.Button('退出注册')]]


    window = sg.Window('小程序工具包——登陆', layout1)

    while True:
        event, values = window.read()
        if event in '退出':
            window.close()
            savefile(user_information, 'C:\\Users\\Administrator\\Desktop\\user_information.txt')
            sys.exit('程序正常退出')
        if event in '登陆':
            print('收到用户名', values[0])
            print('收到密码', values[1])
            if values[0] not in user_information:
                print("用户名不存在")
            else:
                if values[1] == user_information[values[0]]['password']:
                    # 登陆计数
                    user_information[values[0]]['login_count'] += 1
                    print("登录成功")
                    print("欢迎您", values[0])
                    window.close()
                    window = sg.Window('小程序工具包——主页面', layout2)
                    while True:
                        event, values = window.read()
                        if event in '登出':
                            window.close()
                            denglu()
                else:
                    print("密码错误")
        if event in '注册':
            window.close()
            window = sg.Window('小程序工具包——注册', layout3)
            while True:
                event, values = window.read()
                if event in '注册账户':
                    user_information[values[0]] = {
                        # 创建字典格式，保存注册时间
                        'password': values[1],
                        'login_count': 0,
                        'registration_time': datetime.datetime.now()
                    }
                    print("注册成功")
                if event in '退出注册':
                    window.close()
                    denglu()


denglu()