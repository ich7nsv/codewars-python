"""
Create a function that gives a personalized greeting.
This function takes two parameters: name and owner.

Use conditionals to return the proper message:

case	            return
name equals owner	'Hello boss'
otherwise	        'Hello guest'

"""


def greet(name: str, owner: str) -> str:
    """Функция выполняет персональное приветствие"""
    if name == owner:
        return "Hello boss"

    return "Hello guest"

if __name__ == "__main__":
    print(greet("Daniel", "Daniel"))