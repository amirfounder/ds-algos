import inspect
import types


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def log_operations(cls):

    def stringify(obj):
        if isinstance(obj, cls):
            return 'self'
        return str(obj)

    def log_operation(func):
        is_static = isinstance(func, types.FunctionType)

        def inner(*args, **kwargs):

            _args = ', '.join([stringify(a) for a in args])
            _kwargs = ', '.join([f'{k}={stringify(v)}' for k, v in kwargs.items()])
            _params = []
            if _args:
                _params.append(_args)

            if _kwargs:
                _params.append(_kwargs)

            params = ', '.join(_params)

            before_call_message = f'BEFORE fn call... "{str(func.__name__)}({params})"'
            after_call_message = f'AFTER fn call.... "{str(func.__name__)}({params})"'
            state_message = 'No State Available - Static Method Call' if not is_static else \
                f'Instance State: {str(args[0])}'

            print(' : '.join([before_call_message, state_message]))
            result = func(*args, **kwargs)
            print(' : '.join([after_call_message, state_message]))

            return result

        return inner

    members = inspect.getmembers(cls)
    members = [member for member in members if not member[0].startswith('_') and callable(member[1])]

    for name, method in members:
        new = log_operation(method)
        setattr(cls, name, new)

    return cls
