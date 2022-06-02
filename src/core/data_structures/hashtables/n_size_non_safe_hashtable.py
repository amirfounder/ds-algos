class NSizedNonSafeHashTable:
    def __init__(self, size=10):
        self.num_elements = 0
        self.size = 10
        self.data = [0] * size

    def get(self, key):
        hash_value = hash(key) % 10
        return self.data[hash_value]

    def put(self, key, value):
        hash_value = hash(key) % 10
        self.data[hash_value] = value


if __name__ == '__main__':
    table = NSizedNonSafeHashTable()
    table.put('hello', 'goodbye')
    table.put('goodbye', 'hello')
    v = table.get('hello')
    print(v)
    print(table.data)
