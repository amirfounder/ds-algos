from src.commons import log_operations


@log_operations
class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return ' - '.join([str(i) for i in self.items])

    def add(self, obj):
        self.items.append(obj)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


def test():
    q = Queue()
    q.add(1)
    q.add(23)
    q.add(232)
    q.pop()
    q.pop()
    q.pop()


if __name__ == '__main__':
    test()

