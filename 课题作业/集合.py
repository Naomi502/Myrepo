# 集合A
A = {1, 2, 3, 4, 5}
# 集合B
B = {4, 5, 6, 7, 8}

# 差集
diff = A - B
print("差集：", diff)

# 并集
union = A | B
print("并集：", union)

# 交集
intersection = A & B
print("交集：", intersection)

num = 0


# 初始化集合变量

def ifin(data):
    if data in A or data in B:
        return True
    else:
        return False


# 初始化判断函数
def input1():
    while True:  # 持续循环
        try:
            num = int(input("请输入一个数："))
            if num <= 0:
                raise ValueError()  # 抛出异常
            break
        except ValueError:  # 捕获异常
            print("输入有误，请重新输入一个正整数")  # 回到try


# 初始化输入纠错函数

'''程序开始'''

input1()

if ifin(int(num)):  # 调用判断函数，并输入变量num
    print("在集合中")
else:
    print("不在集合中")
