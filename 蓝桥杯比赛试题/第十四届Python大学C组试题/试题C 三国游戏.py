# 定义函数，计算游戏结束时某国获胜的最多事件数
def max_winning_events(n, A, B, C):
    max_events = 0
    x, y, z = 0, 0, 0

    # 模拟游戏过程
    for i in range(n):
        x += A[i]
        y += B[i]
        z += C[i]

        # 判断是否有国家获胜
        if (x > y + z) or (y > x + z) or (z > x + y):
            # 如果有国家获胜，更新最多事件数并结束循环
            max_events = i + 1
            break

    # 输出结果
    if max_events == 0:
        return -1
    else:
        return max_events

# 输入处理
n = int(input())  # 输入国家数量
A = list(map(int, input().split()))  # 输入事件A列表
B = list(map(int, input().split()))  # 输入事件B列表
C = list(map(int, input().split()))  # 输入事件C列表

# 调用函数并输出结果
result = max_winning_events(n, A, B, C)
print(result)
