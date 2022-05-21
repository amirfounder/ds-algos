class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def insert_sorted(root, value):
    if not isinstance(value, (int, float)):
        raise "Cannot store non-ints or non-floats"
    return _insert_sorted(root, None, value)


def _insert_sorted(current, prev, value):
    if value == current.value:
        node = Node(value)
        node.next = current.next
        current.next = node
        return node
    if value > current.value:
        if current.next:
            _insert_sorted(current.next, current, value)
        else:
            node = Node(value)
            current.next = node
            return node
    if value < current.value:
        node = Node(value)
        if prev:
            prev.next = node
        node.next = current
        return node


if __name__ == '__main__':
    nodes = [Node(i) for i in range(10)]
    for i, n in enumerate(nodes):
        n.next = nodes[i + 1] if i < len(nodes) - 1 else None

    n = nodes[0]
    n = insert_sorted(n, -7)
    insert_sorted(n, 7)
    insert_sorted(n, 100)
    insert_sorted(n, 8.5)
    insert_sorted(n, -4)

    while n:
        print(n.value)
        n = n.next
