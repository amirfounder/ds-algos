import inspect


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def log_operations(cls):
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

            print(f'BEFORE fn call... "{str(func.__name__)}({params})" : {str(self)}')
            func(self, *args, **kwargs)
            print(f'AFTER fn call.... "{str(func.__name__)}({params})" : {str(self)}')
        return inner

    members = inspect.getmembers(cls)
    members = [member for member in members if not member[0].startswith('_') and callable(member[1])]

    for name, method in members:
        new = log_operation(method)
        setattr(cls, name, new)

    return cls
