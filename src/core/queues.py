import inspect


def log_operations(cls):
    members = inspect.getmembers(cls)
    members = [member for member in members if not member[0].startswith('_') and callable(member[1])]

    def log_operation(func):
        def inner(self, *args, **kwargs):
            _args = ', '.join([str(a) for a in args])
            _kwargs = ', '.join([f'{k}={v}' for k, v in kwargs.items()])
            _params = []
            if _args:
                _params.append(_args)

            if _kwargs:
                _params.append(_kwargs)

            params = ', '.join(_params)

            print(f'PRIOR  -- "{str(func.__name__)}({params})" : {str(self)}')
            func(self, *args, **kwargs)
            print(f'AFTER  -- "{str(func.__name__)}({params})" : {str(self)}')
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

