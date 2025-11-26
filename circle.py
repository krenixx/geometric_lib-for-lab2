import math

def area(r):
    '''Принимает на вход радиус круга, возвращает его площадь'''
    if r < 0:
        return 'error'
    return math.pi * r * r


def perimeter(r):
    '''Принимает на вход радиус круга, возвращает длину окружности'''
    if r < 0:
        return 'error'
    return 2 * math.pi * r


                
