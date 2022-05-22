SIZE = 1000


def hash_fn(obj) -> int:
    return hash(obj) % SIZE


class ChainingHashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class ChainingHashTable:
    def __init__(self):
        self.size: int = SIZE
        self.data: list[None | list[ChainingHashNode]] = [None] * SIZE

    def __str__(self):
        values = []
        for item in self.data:
            if item is not None:
                for node in item:
                    values.append(node.value)
        return 'Chaining hashtable data: [' + ', '.join(values) + ']'

    def get(self, key):
        hashed = hash_fn(key)
        if self.data[hashed] is None:
            return None

        for node in self.data[hashed]:
            if node.key == key:
                return node.value

        return None

    def put(self, key, value):
        hashed = hash_fn(key)

        if self.data[hashed] is None:
            node = ChainingHashNode(key, value)
            self.data[hashed] = [node]

        else:
            node = ChainingHashNode(key, value)
            for existing_node in self.data[hashed]:
                if existing_node.key == key:
                    existing_node.value = value
                    return

            self.data[hashed].append(node)


if __name__ == '__main__':
    table = ChainingHashTable()
    table.put('hello', 'goodbye')
    v = table.get('hello')
    print(v)
    print(table)
