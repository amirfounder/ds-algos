_values = [5, 8, 3, 3, 2, 1, 2, 100, 100, 100]
_weights = [7, 1, 4, 1, 6, 4, 2, 5, 7, 4]
ITEMS = list(zip(_values, _weights))
CAPACITY = 15


def dynamic_knapsack(idx, remaining_capacity, memo):
    if memo[idx][remaining_capacity] is not None:
        return memo[idx][remaining_capacity]

    if idx == 0 or remaining_capacity == 0:
        res = 0
    elif ITEMS[idx][1] > remaining_capacity:
        res = dynamic_knapsack(idx - 1, remaining_capacity, memo)
    else:
        res1 = dynamic_knapsack(idx - 1, remaining_capacity, memo)
        res2 = dynamic_knapsack(idx - 1, remaining_capacity - ITEMS[idx][1], memo) + ITEMS[idx][0]
        res = max(res1, res2)

    memo[idx][remaining_capacity] = res
    return res


def main():
    memo = []
    for _ in range(len(ITEMS)):
        memo.append([None] * (CAPACITY + 1))
    result = dynamic_knapsack(len(ITEMS) - 1, CAPACITY, memo)
    print(result)


if __name__ == '__main__':
    main()
