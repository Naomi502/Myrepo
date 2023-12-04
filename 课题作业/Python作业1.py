# Page 55 第一题
t = float(input('请输入华氏温度'))  # 输入变量（华氏温度:浮点）
s = (t - 32) / 1.8  # 计算表达式

print("摄氏温度是：", round(s, 2))

# Page 55 第二题
import math
r1 = float(input("请输入外圆半径 r1: "))
r2 = float(input("请输入内圆半径 r2: "))
area = math.pi * (r1**2 - r2**2)
print("圆环的面积为:", area)

# Page 55 第三题
up = float(input("请输入梯形的上底: "))
low = float(input("请输入梯形的下底: "))
height = float(input("请输入梯形的高: "))
area = 0.5 * (up + low) * height
print("梯形的面积为:", area)

# Page 55 第四题
# 从键盘输入一个字符
char = input("请输入一个字符: ")
unicode = ord(char)
char1 = chr(unicode - 1)
char2 = chr(unicode + 1)
print(f"字符 '{char}' 的Unicode码为: {unicode}")
print(f"前一个字符 '{char1}' 的Unicode码为: {ord(char1)}")
print(f"后一个字符 '{char2}' 的Unicode码为: {ord(char2)}")

# Page 55 第五题
def numberin():
    while True:
        num = input("请输入一个三位整数: ")
        try:
            num = int(num)  # 转换整型
            if 999 >= num > 99:
                print("个位数字为: ", num % 10)
                print("十位数字为: ", (num // 10) % 10)
                print("百位数字为: ", num // 100)
                break
            else:
                print("这不是一个三位整数,请重新输入")
        except ValueError:
            print("这不是一个整数,请重新输入")

numberin()
# 上面的为旧代码
# Page 81 第二题

num1 = [int(input('请输入一个数')) for _ in range(5)]
print('从小到大：', sorted(num1))
print('从大到小：', sorted(num1, reverse=True))

# Page 81 第三题
s = input('请输入一个字符串')
c = input('请输入一个字符')
print('字符', c, '在字符串', s, '中出现的次数为', s.count(c))

# Page 81 第四题
l = [i for i in range(20) if i % 2 == 1]
print('列表所有数的和为：', sum(l))
