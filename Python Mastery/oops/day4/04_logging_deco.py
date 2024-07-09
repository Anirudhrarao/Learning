import functools

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'calling {func.__name__} with args: {args} and kwargs {kwargs}')
        result = func(*args, **kwargs)
        print(f'{func.__name__} return {result}')
        return result
    return wrapper

@logger
def add(a, b):
    return  a + b 

print(add(1,2))
