def max_non_overlapping_substrings(s):
    n = len(s)  # 字符串的长度
    start, end = 0, -1  # 初始化起始位置和结束位置
    intervals = []  # 存储所有可能的 01 子串区间

    # 寻找所有可能的 01 子串区间
    for i in range(n):
        if s[i] == '0':  # 如果当前字符为 '0'，则更新结束位置
            end = i
        elif i + 1 < n and s[i + 1] == '1':  # 如果当前字符为 '1'，并且下一个字符也是 '1'，则表示有一个 01 子串区间
            start = i + 1  # 更新起始位置
            intervals.append((start, end))  # 将子串区间添加到 intervals 列表中

    # 根据区间结束位置贪心地选择最多的非重叠区间
    result = []  # 存储最终结果
    last_end = -1
    for interval in sorted(intervals, key=lambda x: x[1]):
        if interval[0] > last_end:  # 如果当前区间的起始位置大于上一个区间的结束位置，则两个区间不重叠
            result.append(interval)  # 将当前区间添加到结果中
            last_end = interval[1]  # 更新 last_end 变量为当前区间的结束位置

    return len(result)  # 返回结果的长度

# 输入处理
s = input()  # 从输入中获取字符串 s

# 调用函数并输出结果
result = max_non_overlapping_substrings(s)  # 调用 max_non_overlapping_substrings 函数计算结果
print(result)  # 输出结果