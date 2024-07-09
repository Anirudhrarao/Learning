from typing import Callable

def add(a: int, b: int) -> int:
    return a + b

def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    return operation(a, b)

result = apply_operation(2,3,add)
print(result)