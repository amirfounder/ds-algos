_values = [5, 8, 3, 3, 2, 1, 2, 100, 100, 100]
_weights = [7, 1, 4, 1, 6, 4, 2, 5, 7, 4]
ITEMS = list(zip(_values, _weights))
CAPACITY = 15


def recursive_knapsack(idx, remaining_capacity):
    prefix = '    ' * idx

    # print(prefix + 'Level: ' + str(idx))

    if idx == len(ITEMS) or remaining_capacity == 0:
        res = 0
    elif ITEMS[idx][1] > remaining_capacity:
        res = recursive_knapsack(idx + 1, remaining_capacity)
    else:
        res1 = recursive_knapsack(idx + 1, remaining_capacity)
        res2 = recursive_knapsack(idx + 1, remaining_capacity - ITEMS[idx][1]) + ITEMS[idx][0]
        res = max(res1, res2)

        print(prefix + 'IDX, RC, R, (R1, R2): ' + ', '.join([str(idx), str(remaining_capacity), str(res), str(res1),
                                                             str(res2)]))
    return res

def main():
    result = recursive_knapsack(0, CAPACITY)
    print(result)


if __name__ == '__main__':
    main()
