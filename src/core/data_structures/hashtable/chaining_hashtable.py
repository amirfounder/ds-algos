SIZE = 1000


def hash_fn(obj) -> int:
    return hash(obj) % SIZE


class NIL:
    def __init__(self, value='NIL'):
        self.value = value


class ChainingHashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class Bucket:
    def __init__(self):
        self.pairs = []

    def is_empty(self):
        return not self.pairs

    def add(self, key, value):
        for i, (k, v) in enumerate(self.pairs):
            if k == key:
                self.pairs[i] = (key, value)
                return

        self.pairs.append((key, value))

    def get(self, key):
        for k, v in self.pairs:
            if k == key:
                return v

        return None


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


class ChainingHashTableWithBuckets:
    def __init__(self):
        self.size = 0
        self.data = [Bucket() for _ in range(SIZE)]

    def __str__(self):
        values = []
        for bucket in self.data:
            for k, v in bucket.pairs:
                values.append(f'{k}={v}')

        return 'Chaining hashtable data: [' + ', '.join(values) + ']'

    def get(self, key):
        hashed = hash_fn(key)
        return self.data[hashed].get(key)

    def put(self, key, value):
        hashed = hash_fn(key)
        self.data[hashed].add(key, value)


def main():
    table = ChainingHashTableWithBuckets()
    table.put('hello', 'goodbye')
    table.put('key', 'value')
    table.put('lol', 'haha')
    print(table)

    table = ChainingHashTable()
    table.put('hello', 'goodbye')
    table.put('key', 'value')
    table.put('lol', 'haha')


if __name__ == '__main__':
    main()
