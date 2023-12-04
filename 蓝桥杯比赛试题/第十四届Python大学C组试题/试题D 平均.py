# 定义函数，计算调整数组使得每种数出现次数相等的最小代价和
def min_cost_to_balance_array(n, counts):
    target_count = n // 10  # 目标每种数出现的次数
    current_counts = [0] * 10  # 每种数当前出现的次数
    cost = 0  # 代价和

    # 统计每种数的当前出现次数
    for count in counts:
        current_counts[count] += 1

    # 遍历每种数，计算需要调整的代价和
    for i in range(10):
        if current_counts[i] > target_count:
            cost += (current_counts[i] - target_count) * i

    # 输出结果
    return cost

# 输入处理
n = int(input())
counts = [int(input()) for _ in range(n)]

# 调用函数并输出结果
result = min_cost_to_balance_array(n, counts)
print(result)
