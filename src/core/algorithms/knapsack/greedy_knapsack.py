_values = [5, 8, 3, 3, 2, 1, 2, 100, 100, 100]
_weights = [7, 1, 4, 1, 6, 4, 2, 5, 7, 4]
ITEMS = list(zip(_values, _weights))
CAPACITY = 15


class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

    def __str__(self):
        return f'Item (value={self.value}, weight={self.weight})'


def knapsack_problem(items, max_weight):
    items.sort(key=lambda x: x.ratio, reverse=True)

    items_so_far = []
    weight_so_far = 0

    for item in items:
        if item.weight <= (max_weight - weight_so_far):
            items_so_far.append(item)
            weight_so_far += item.weight

    return items_so_far


def main():
    results = knapsack_problem([Item(v, w) for v, w in ITEMS], CAPACITY)
    total_value = sum([r.value for r in results])
    total_weight = sum([r.weight for r in results])
    for result in results:
        print(result)
    print('')
    print('Total value: ' + str(total_value))
    print('Total weight: ' + str(total_weight))


if __name__ == '__main__':
    main()
