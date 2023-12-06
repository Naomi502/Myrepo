# 1、输入3个数，输出最大数。
def find_max():
    # 输入3个数
    num1 = float(input("请输入第一个数: "))
    num2 = float(input("请输入第二个数: "))
    num3 = float(input("请输入第三个数: "))

    # 输出最大数
    max_num = max(num1, num2, num3)
    print(f"最大数是: {max_num}")


# 2、输出200到500之间，可被6整除，但不是5倍数的所有数，输出时按逗号分隔。

:wq

# 3、输入一行字符串，分别统计出其中英文字母、空格、数字和其它字符的个数。

def count_characters():
    # 输入一行字符串
    user_input = input('请输入一行字符串：')

    # 统计各类字符个数
    alphabetic_count = sum(char.isalpha() for char in user_input)
    space_count = user_input.count(' ')
    numeric_count = sum(char.isdigit() for char in user_input)
    other_count = len(user_input) - alphabetic_count - space_count - numeric_count

    # 打印结果
    print(f"英文字母个数：{alphabetic_count}")
    print(f"空格个数：{space_count}")
    print(f"数字个数：{numeric_count}")
    print(f"其他字符个数：{other_count}")


# 4、输入一个整数，判断是否是回文数。由前向后和由后向前都一样的数为回文数。

def check_palindrome():
    # 输入一个整数
    num = input("请输入一个整数: ")

    # 判断是否是回文数
    is_palindrome = num == num[::-1]
    print(f"{num} 是回文数" if is_palindrome else f"{num} 不是回文数")


# 5、将一个整数分解质因数。例如：输入90，打印出90=2*3*3*5。

def factorize_number():
    def prime_factors(n):
        factors = []
        divisor = 2

        while n > 1:
            while n % divisor == 0:
                factors.append(divisor)
                n //= divisor
            divisor += 1

        return factors

    # 输入一个整数
    num = int(input("请输入一个整数: "))

    # 打印整数的质因数分解结果
    print(f"{num} =", " * ".join(map(str, prime_factors(num))))


# 主程序
print("请选择要运行的部分：")
print("1. 寻找最大数")
print("2. 查找特殊数字")
print("3. 统计字符个数")
print("4. 检查回文数")
print("5. 整数质因数分解")

choice = input("请输入相应的数字（1-5）：")
if choice == '1':
    find_max()
elif choice == '2':
    find_special_numbers()
elif choice == '3':
    count_characters()
elif choice == '4':
    check_palindrome()
elif choice == '5':
    factorize_number()
else:
    print("无效的选择。请在1到5之间选择。")
