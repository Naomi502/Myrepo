# # a = 5
# # def BOOM():
# #     while a < 10:
# #         print("循环中")
# #         a + 1
# #
# # BOOM()
# #
# # name = 'jason'
# # age = 20
# #
# # # message = "my name is {0},age is {1}"
# # message = "my name is {name},age is {age}"
# #
# # print(message.format_map({'name': name, 'age': age})
# #
# t = float(input('请输入华氏温度'))  # 输入变量（华氏温度:浮点）
# s = (t - 32) / 1.8  # 计算表达式
#
# print("摄氏温度是：", round(s, 2))
#
#
# # char = input("请输入一个字符: ")
# # print("该字符的Unicode编码为:", ord(char))
# # if len(char) > 0:
# #     print("该字符前的一个字符是:", chr(ord(char)-1))
# #     print("该字符后的一个字符是:", chr(ord(char)+1))
# # else:
# #     print("该字符没有前后字符")
#
#
# # 输入一个三位整数
# # def numberin():
# #     num = int(input("请输入一个三位整数: "))
# #
# #     while num < 999:
# #         # 输出个位数字
# #         num1 = num % 10
# #         print("个位数字为: ", num1)
# #
# #         # 输出十位数字
# #         num10 = (num // 10) % 10
# #         print("十位数字为: ", num10)
# #
# #         # 输出百位数字
# #         num100 = num // 100
# #         print("百位数字为: ", num100)
# #         break
# #     else:
# #         print("输入的是不是三位整数,请继续输入")
# #         numberin()
# #
# #
# # numberin()
#
# def numberin():
#     while True:
#         num = input("请输入一个三位整数: ")
#         try:
#             num = int(num)  # 转换整型
#             if 999 >= num > 99:
#                 print("个位数字为: ", num % 10)
#                 print("十位数字为: ", (num // 10) % 10)
#                 print("百位数字为: ", num // 100)
#                 break
#             else:
#                 print("这不是一个三位整数,请重新输入")
#         except ValueError:
#             print("这不是一个整数,请重新输入")
#
# #
# # numberin()
#
# # x = {1,2,3,4,5}
# # x.pop()
# # print(x)
# # x.pop()
# # print(x)
# # x.pop()
# # print(x)
# # x.pop()
# # print(x)
#
#
#
# def setall():
#     x = {1, 2, 3, 4, 5}  # 定义集合x
#     y = {4, 2, 3, 4, 5}  # 定义集合y
#     z = {1, 2, 6, 4, 5}  # 定义集合z
#     frozen = frozenset({1, 2, 3, 4, 5})
#
#
#     print(x & y)  # x和y的交集
#     print(x | y)  # x和y的并集
#     print(x ^ y)  # x和y的对称差集
#     print(x - y)  # x和y的差集
#     print(x ^ z)  # x和z的对称差集
#     print(frozen)
#
#
# setall()
#
#


# def dict1():
#     dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#     print(dict.keys())
#     print(dict.values())
#     print(dict.items())
#     print(dict.get('a'))
#     print(dict.get('f'))
#     print(dict.setdefault('f', 6))
#     print(dict.setdefault('f', 6))
#
# dict1()
# for a in range(1,101):
#     if a % 7 == 0 or a % 10 == 7 or a // 10 == 7:
#         continue
#     else:，
#         print(a)
# x = [1,'a','b']
# x.extend('abc')
# print(x)
# sticks = 21
#
# print("There are 21 sticks, you can take 1-4 number of sticks at a time.")
# print("Whoever will take the last stick will lose")
#
# while True:
#     print("Sticks left: ", sticks)
#
#     # 玩家的回合
#     player_choice = int(input("Take sticks (1-4): "))
#     if player_choice < 1 or player_choice > 4 or player_choice > sticks:
#         print("Wrong choice. Try again.")
#         continue
#     sticks -= player_choice
#
#     if sticks == 0:
#         print("Congratulations! You took the last stick. You win!")
#         break
#
#     # 计算机的回合
#     computer_choice = 5 - player_choice
#     print("Computer took: ", computer_choice, "\n")
#     sticks -= computer_choice
#
#     if sticks == 0:
#         print("Computer took the last stick. You lose!")
#         break

# a = 36*30
# print(a)
# b = 2**2023%1000
# print(b)