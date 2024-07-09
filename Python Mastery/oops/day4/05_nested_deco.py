def words_count(func):
    def wrapper(name, *args, **kwargs):
        result = len(name)
        print(f'Length of name args is {result}')
        return func(name, *args, **kwargs)
    return wrapper

def uppercase_word(func):
    def wrapper(name, *args, **kwargs):
        name = name.upper()
        return func(name, *args, **kwargs)
    return wrapper

@words_count
@uppercase_word
def get_name(name):
    return f'Hello {name}'

print(get_name('aniruddh'))