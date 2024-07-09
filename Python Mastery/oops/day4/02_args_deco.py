def decorator_with_args(deco_args):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'Decorator args: {deco_args}')
            return func(*args, **kwargs)
        return wrapper
    return decorator

@decorator_with_args('Python')
def greet(name:str):
    print(f'Hello {name} welcome to python mastery course')

greet('Aniruddh')