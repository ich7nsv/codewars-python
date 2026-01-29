"""
You are given two interior angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested.

"""


def other_angle(a: int, b: int) -> int:
    """Функция возвращает градус третьего угла треугольника по двум"""
    return int(180 - (a + b))

if __name__ == "__main__":
    print(other_angle(10, 20))