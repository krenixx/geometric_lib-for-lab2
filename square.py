def area(a):
    """Принимает на вход длину стороны квадрата, возвращает его площадь"""
    if a < 0:
        return 'error'
    return a * a


def perimeter(a):
    """Принимает на вход длину стороны квадрата, возвращает его периметр"""
    if a < 0:
        return 'error'
    return 4 * a
