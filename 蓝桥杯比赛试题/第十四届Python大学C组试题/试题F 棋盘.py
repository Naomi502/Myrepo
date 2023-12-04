def chessboard_operations(n, m, operations):
    # 创建一个 n * n 的 0 矩阵
    chessboard = [[0] * n for _ in range(n)]

    # 对每个操作进行处理
    for operation in operations:
        xi, y1, x2, y2 = operation
        # 遍历每个操作指定的区间
        for i in range(xi-1, x2):
            for j in range(y1-1, y2):
                # 利用操作将棋盘上的值取反
                chessboard[i][j] = 1 - chessboard[i][j]

    # 遍历棋盘上的每一行并输出
    for row in chessboard:
        print(''.join(map(str, row)))

# 输入处理
n, m = map(int, input().split())
operations = [list(map(int, input().split())) for _ in range(m)]

# 调用函数并输出结果
chessboard_operations(n, m, operations)
