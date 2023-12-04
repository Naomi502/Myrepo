# import sys
# def count_same_digit_sum_numbers(n):
#     count = 0
#     k = 0
#     while count < n:
#         digit_sum = sum(int(digit) for digit in str(2**k))
#         if digit_sum == 2**k:
#             count += 1
#         k += 1
#     return 2**k-1
# sys.set_int_max_str_digits(8000)
# for i in range(1, 23):
#     result = count_same_digit_sum_numbers(i)
#     print(result)
# else:
#     print("打印完成")


# def left_rotate(x):
#     # 将整数 x 转换为字符串
#     x_str = str(x)
#
#     # 将字符串左移一位
#     rotated_str = x_str[1:] + x_str[0]
#
#     # 将左移后的字符串转换为整数并输出
#     rotated_int = int(rotated_str)
#     print(rotated_int)
#
#
# # 读取输入的整数
# x = int(input().strip())
#
# # 调用左移函数并输出结果
# left_rotate(x)

#
# x = input("输入一行包含一个字符串，仅由小写英文字符组成，字符串中至少包含一个元音字母：")
# eng = ['a','e','i','o','u']
#
# for i in x:
#     if i in eng:
#         result = i
# print(result)

x = int(input("输入一行包含一个整数:"))
c = []
result = x

while result >= 10:
        out = 1
        for char in str(result):  # 遍历添加数字到列表内
            num = int(char)
            if num != 0:
                out *= num
                c.append(num)
        print(out)
        result = out
        c = []

# def count_divisors(number):
#     count = 0
#     for i in range(1, number + 1):
#         if number % i == 0:
#             count += 1
#     return count
#
# numbers = [
#     [393353, 901440, 123481, 850930, 423154, 240461],
#     [373746, 232926, 396677, 486579, 744860, 468782],
#     [941389, 777714, 992588, 343292, 385198, 876426],
#     [483857, 241899, 544851, 647930, 772403, 109929],
#     [882745, 372491, 877710, 340000, 659788, 658675],
#     [296521, 491295, 609764, 718967, 842000, 670302]
# ]
#
# max_divisors = 0
# max_divisors_number = None
#
# for row in numbers:
#     for num in row:
#         divisors_count = count_divisors(num)
#         if divisors_count > max_divisors:
#             max_divisors = divisors_count
#             max_divisors_number = num
#
# print(f"约数个数最多的数是：{max_divisors_number}，约数个数为：{max_divisors}")

# Define the matrix
# matrix = [
#     [0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0,1,0,0,1,0,0,1,1,0,0,0,0,0,0,1,1],
#     [0,1,0,1,1,1,1,0,0,1,1,1,1,0,1,1,0,1,1,1,1,0,0,0,0,1,0,1,0,1,0,1,0,0,1,1,1,1,1,1],
#     [1,0,0,0,0,1,0,0,0,0,0,1,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0],
#     [0,1,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0],
#     [0,0,0,0,0,1,1,0,1,0,1,0,0,0,0,1,1,1,1,1,1,0,0,1,1,0,1,1,0,0,0,1,0,1,0,1,0,0,1,1],
#     [0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,1,0,0,0,1,1],
#     [0,1,0,0,1,1,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,1,1,0,0,0,0,0]
# ]
#
# # Function to spread the "2" in the matrix
# def spread(matrix):
#     # Copy the matrix to avoid modifying the original
#     new_matrix = [row[:] for row in matrix]
#     rows = len(matrix)
#     cols = len(matrix[0])
#     changed = False
#
#     for r in range(rows):
#         for c in range(cols):
#             # Check if the current element is 2
#             if matrix[r][c] == 2:
#                 # Spread to adjacent cells
#                 for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                     new_r, new_c = r + dr, c + dc
#                     if 0 <= new_r < rows and 0 <= new_c < cols and matrix[new_r][new_c] == 0:
#                         new_matrix[new_r][new_c] = 2
#                         changed = True
#
#     return new_matrix, changed
#
# # Start the spread from the top-left corner
# matrix[0][0] = 2
#
# # Keep spreading until no more changes
# while True:
#     matrix, changed = spread(matrix)
#     if not changed:
#         break
#
# # Count the number of 2's in the final matrix
# num_twos = sum(row.count(2) for row in matrix)
# print(num_twos)
