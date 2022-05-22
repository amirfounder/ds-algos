import inspect


def log_operations(cls):
    members = inspect.getmembers(cls)
    members = [member for member in members if not member[0].startswith('_') and callable(member[1])]

    def log_operation(func):
        def inner(self, *args, **kwargs):
            print(f'State before calling "{str(func.__name__)}" : {str(self)}')
            func(self, *args, **kwargs)
            print(f'State after calling "{str(func.__name__)}" : {str(self)}')
        return inner

    for name, function in members:
        new = log_operation(function)
        setattr(cls, name, new)

    return cls


@log_operations
class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return ' - '.join([str(x) for x in self.items])

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

