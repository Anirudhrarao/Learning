class Decorator:
    def __init__(self,func):
        self.func = func 
    
    def __call__(self, *args, **kwargs):
        print("Something is happening before function is called")
        result = self.func(*args, **kwargs)
        print("Something is happening after function is called")
        return result
    

@Decorator
def say_hello(name):
    print(f"Hello {name}")

say_hello("Anirudhra")