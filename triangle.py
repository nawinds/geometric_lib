def area(a: float, h: float) -> float:
    """
    Возвращает площадь треугольника с основанием a и высотой h

        :param a: основание треугольника
        :type a: float
        :param h: высота треугольника
        :type h: float
        :returns: площадь треугольника
        :rtype: float

    Пример вызова:
        s = area(5, 2)  # В s запишется 5
    """
    return a * h / 2 


def perimeter(a: float, b: float, c: float) -> float:
    """
    Возвращает периметр треугольника со сторонами a, b, c

        :param a: одна сторона треугольника
        :type a: float
        :param b: вторая сторона треугольника
        :type b: float
        :param c: третья сторона треугольника
        :type c: float
        :returns: периметр треугольника
        :rtype: float

    Пример вызова:
         p = perimeter(5, 2, 3)  # В p запишется 10
    """
    return a + b + c

