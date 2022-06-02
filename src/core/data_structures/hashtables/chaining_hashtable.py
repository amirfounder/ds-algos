SIZE = 1000


def hash_fn(obj) -> int:
    return hash(obj) % SIZE


class NIL:
    def __init__(self):
        self.value = "NIL"


class ChainingHashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class ChainingHashTable:
    def __init__(self):
        self.size: int = SIZE
        self.data: list[NIL | list[ChainingHashNode]] = [NIL()] * SIZE

    def __str__(self):
        values = []
        for item in self.data:
            if isinstance(item, NIL):
                continue
            for node in item:
                values.append(node.value)
        return 'Chaining hashtable data: [' + ', '.join(values) + ']'

    def get(self, key):
        hashed = hash_fn(key)
        if isinstance(self.data[hashed], NIL):
            return None

        for node in self.data[hashed]:
            if node.key == key:
                return node.value

        return None

    def put(self, key, value):
        hashed = hash_fn(key)

        if isinstance(self.data[hashed], NIL):
            node = ChainingHashNode(key, value)
            self.data[hashed] = [node]

        else:
            node = ChainingHashNode(key, value)
            for existing_node in self.data[hashed]:
                if existing_node.key == key:
                    existing_node.value = value
                    return

            self.data[hashed].append(node)


def main():
    table = ChainingHashTable()
    table.put('hello', 'goodbye')
    table.put('key', 'value')
    table.put('lol', 'haha')


if __name__ == '__main__':
    main()
