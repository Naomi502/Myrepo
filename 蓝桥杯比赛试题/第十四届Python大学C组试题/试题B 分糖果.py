from itertools import product


def count_distributions(candies, children, min_candies, max_candies):
    """
    计算满足给定条件的糖果分配方案数量

    参数：
    candies: tuple，表示两种不同类型的糖果数量的元组 (candies1_count, candies2_count)
    children: int，表示孩子的数量
    min_candies: int，表示每个孩子至少分配的糖果数量
    max_candies: int，表示每个孩子最多分配的糖果数量

    返回值：
    int，满足条件的糖果分配方案数量
    """
    # 生成每种糖果分配给每个孩子的所有可能分配方案
    all_distributions = product(range(min_candies, max_candies + 1), repeat=children)

    valid_distributions = 0

    for distribution in all_distributions:
        # 将分配方案分为两种类型的糖果列表
        for split_index in range(1, children):
            first_candy_distribution = distribution[:split_index]
            second_candy_distribution = distribution[split_index:]

            # 检查分配方案是否与给定的糖果数量一致
            if sum(first_candy_distribution) == candies[0] and sum(second_candy_distribution) == candies[1]:
                valid_distributions += 1

    return valid_distributions


# 糖果数量
candy_counts = (9, 16)
# 孩子的数量
num_children = 7
# 每个孩子至少分配的糖果数量
min_candies = 2
# 每个孩子最多分配的糖果数量
max_candies = 5

# Calculate the number of ways to distribute the candies
print("有", count_distributions(candy_counts, num_children, min_candies, max_candies), "种不同的分法")
