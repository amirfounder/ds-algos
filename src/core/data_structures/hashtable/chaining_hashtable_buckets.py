SIZE = 1000


def hash_fn(obj):
    return hash(obj) % SIZE


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


if __name__ == '__main__':
    main()