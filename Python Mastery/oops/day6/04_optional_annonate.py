from typing import Optional

def greet(name: Optional[str] = None) -> str:
    if name:
        return f'Hello {name}'
    else:
        return f'Hello, World!'