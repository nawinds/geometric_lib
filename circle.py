import math


def area(r: float) -> float:
    """Возвращает площадь круга с радиусом r

        :param r: радиус круга
        :type r: float
        :returns: площадь круга
        :rtype: float
    """
    return math.pi * r * r


def perimeter(r):
    """Возвращает длину окружности с радиусом r

        :param r: радиус круга
        :type r: float
        :returns: длина окружности
        :rtype: float
    """
    return 2 * math.pi * r

