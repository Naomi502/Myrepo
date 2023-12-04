# 初始化
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
# 读取文件


def savefile(information, file_path):
    with open(file_path, 'w') as file:
        for username, data in information.items():
            file.write(
                f"用户名: {username}, 密码: {data['password']}, 登录次数: {data['login_count']}, 注册时间: {data['registration_time']}\n")
# 保存字典到txt


def zhuce(information):
    username = str(input("请输入你的用户名："))
    password = str(input("请输入你的密码："))

    information[username] = {
        # 创建字典格式，保存注册时间
        'password': password,
        'login_count': 0,
        'registration_time': datetime.datetime.now()
    }
    print("注册成功")
# 注册页面


def denglu():
    # 定义全局变量，以便调整函数外初始化变量
    global loginmain
    while True:
        login1 = str(input("请输入你的用户名："))
        password1 = str(input("请输入你的密码："))
        if login1 not in user_information:
            print("用户名不存在")
            return False
        else:
            if password1 == user_information[login1]['password']:
                # 登陆计数
                user_information[login1]['login_count'] += 1
                print("登录成功")
                print("欢迎您", login1)
                loginmain = True
                return True
            else:
                print("密码错误")
                retry = input("是否重新登录？(是/否): ").lower()
                if retry != '是':
                    return False
# 登陆页面


def display_accounts(information):
    print("所有账户信息：")
    for username, data in information.items():
        print(
            f"用户名: {username}, 密码: {data['password']}, 登录次数: {data['login_count']}, 注册时间: {data['registration_time']}")
    confirm_continue()
# 显示账户信息


def appmain():
    global loginmain
    while True:
        if loginmain:
            print("小程序工具包")
            print("1. 登出\n2. 温度转换\n3. 随机数生成\n4. 显示账户信息\n5. 查看排行榜")
            choice = input("请选择操作(1，2，3，4, 5): ")

            if choice == '1':
                loginmain = False
                loginpage()
            elif choice == '2':
                temperature()
            elif choice == '3':
                random_program()
            elif choice == '4':
                if loginmain:
                    display_accounts(user_information)
                else:
                    print("检测到违法操作，禁止访问")
                    break
            elif choice == '5':
                display_ranking()
        else:
            break
# 程序主函数


def temperature():
    t = float(input('请输入华氏温度：'))
    s = (t - 32) / 1.8

    print("摄氏温度是：", round(s, 2))
    confirm_continue()
# 温度转换小程序


def random_program():
    try:
        start = int(input("请输入随机数范围的起始值："))
        end = int(input("请输入随机数范围的结束值："))
        count = int(input("请输入要生成的随机数的个数："))

        if start >= end:
            print("错误：起始值必须小于结束值")
            return

        random_numbers = [random.randint(start, end) for _ in range(count)]

        print(f"\n在范围[{start}, {end}]内生成的随机数为：")
        for number in random_numbers:
            print(number)

        confirm_continue()

    except ValueError:
        print("错误：请输入有效的整数")
# 随机数小程序


def confirm_continue():
    confirm = input("按Enter键继续...")
    if confirm != '':
        sys.exit()
# 切换下一个函数时enter停顿


def display_ranking():
    sorted_users = sorted(user_information.items(), key=lambda x: x[1]['login_count'], reverse=True)

    print("排行榜：")
    for i, (username, data) in enumerate(sorted_users, start=1):
        print(f"{i}. 用户名: {username}, 登录次数: {data['login_count']}, 注册时间: {data['registration_time']}")

    confirm_continue()
# 显示排行榜


def loginpage():
    global loginmain
    while True:
        print("小程序网站登录页面")
        print("1. 注册\n2. 登录\n3. 退出")
        choice = input("请选择操作(1/2/3/4): ")

        if choice == '1':
            zhuce(user_information)
        elif choice == '2':
            login_success = denglu()
            while not login_success:
                retry_main = input("是否返回主界面？(是/否): ").lower()
                if retry_main != '是':
                    login_success = denglu()
                else:
                    break
            if login_success:
                appmain()
        elif choice == '3':
            savefile(user_information, 'C:\\Users\\User\\Desktop\\user_information.txt')
            sys.exit('程序正常退出')
        elif choice == '4':
            if loginmain:
                display_accounts(user_information)
            else:
                print("检测到违法操作，禁止访问")
                break
        else:
            print("无效的选项，请重新输入")
# 登陆页面


# 在程序启动时加载用户信息，调用loadfile函数
user_information = loadfile('C:\\Users\\User\\Desktop\\user_information.txt')

# 开始
loginpage()
