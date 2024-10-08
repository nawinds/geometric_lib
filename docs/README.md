# Общее описание решения
Этот проект содержит 4 файла с функциями для вычисления площади и периметра различных геометрических 
фигур: 
- circle.py для круга,
- rectangle.py для прямоугольника, 
- square.py для квадрата, 
- triangle.py для треугольника.

Для вычисления периметра и площади фигур используются следующие математический формулы:

## Площадь
- Круг: S = πR²
- Прямоугольник: S = ab
- Квадрат: S = a²

## Периметр
- Круг: P = 2πR
- Прямоугольник: P = 2 * (a + b)
- Квадрат: P = 4a

# Описание функций с примерами вызова
`square.py`:
- `def area(a)`:
  ```python
  def area(a: float) -> float:
      """Возвращает площадь квадрата со стороной a

          :param a: длина стороны квадрата
          :type a: float
          :returns: площадь квадрата
          :rtype: float
      """
      return a * a
  ```
  Функция вычисляет площадь квадрата. Она принимает один аргумент: длину стороны квадрата типа float (или int) 
  и возвращает площадь квадрата типа float (или int).
  ### Пример вызова:
  ```python
  s = area(5)  # В s запишется 25
  ```

- `perimeter(a)`:
  ```python
  def perimeter(a: float) -> float:
      """Возвращает периметр квадрата со стороной a

          :param a: длина стороны квадрата
          :type a: float
          :returns: периметр квадрата
          :rtype: float
      """
    return 4 * a
  ```
  Функция вычисляет периметр квадрата. Она принимает один аргумент: длину стороны квадрата типа float (или int) 
  и возвращает периметр квадрата типа float (или int).
  ### Пример вызова:
  ```python
  p = perimeter(5)  # В p запишется 20
  ```

`rectangle.py`:
- `def area(a, b)`:
  ```python
  def area(a: float, b: float) -> float:
      """Возвращает площадь прямоугольника со сторонами a, b

          :param a: длина прямоугольника
          :type a: float
          :param b: ширина прямоугольника
          :type b: float
          :returns: периметр прямоугольника
          :rtype: float
      """
      return a * b 
  ```
  Функция вычисляет площадь прямоугольника. Она принимает два аргумента: длину и ширину прямоугольника типа float (или int) 
  и возвращает площадь прямоугольника типа float (или int).
  ### Пример вызова:
  ```python
  s = area(5, 2)  # В s запишется 10
  ```

- `perimeter(a, b)`:
  ```python
  def perimeter(a: float, b: float) -> float:
      """Возвращает периметр прямоугольника со сторонами a, b

          :param a: длина прямоугольника
          :type a: float
          :param b: ширина прямоугольника
          :type b: float
          :returns: периметр прямоугольника
          :rtype: float
      """
      return 2 * (a + b)
  ```
  Функция вычисляет периметр прямоугольника. Она принимает 2 аргумента: длину и ширину прямоугольника типа float (или int) 
  и возвращает периметр прямоугольника типа float (или int).
  ### Пример вызова:
  ```python
  p = perimeter(5, 2)  # В p запишется 14
  ```

`triangle.py`:
- `def area(a, h)`:
  ```python
  def area(a: float, h: float) -> float:
      """Возвращает площадь треугольника с основанием a и высотой h

          :param a: основание треугольника
          :type a: float
          :param h: высота треугольника
          :type h: float
          :returns: площадь треугольника
          :rtype: float
      """
      return a * h / 2 
  ```
  Функция вычисляет площадь треугольника. Она принимает два аргумента: основание и высоту треугольника типа float (или int) 
  и возвращает площадь треугольника типа float (или int).
  ### Пример вызова:
  ```python
  s = area(5, 2)  # В s запишется 5
  ```

- `perimeter(a, b, c)`:
  ```python
  def perimeter(a: float, b: float, c: float) -> float:
      """Возвращает периметр треугольника со сторонами a, b, c

          :param a: одна сторона треугольника
          :type a: float
          :param b: вторая сторона треугольника
          :type b: float
          :param c: третья сторона треугольника
          :type c: float
          :returns: периметр треугольника
          :rtype: float
      """
      return a + b + c
  ```
  Функция вычисляет периметр треугольника. Она принимает 3 аргумента: все стороны треугольника типа float (или int) 
  и возвращает периметр треугольника типа float (или int).
  ### Пример вызова:
  ```python
  p = perimeter(5, 2, 3)  # В p запишется 10
  ```
  
`circle.py`:
- `def area(r)`:
  ```python
  def area(r: float) -> float:
      """Возвращает площадь круга с радиусом r

          :param r: радиус круга
          :type r: float
          :returns: площадь круга
          :rtype: float
      """
      return math.pi * r * r
  ```
  Функция вычисляет площадь круга. Она принимает один аргумент: радиус круга типа float (или int) 
  и возвращает площадь круга типа float (или int).
  ### Пример вызова:
  ```python
  s = area(2)  # В s запишется 12.56
  ```

- `perimeter(r)`:
  ```python
  def perimeter(r):
      """Возвращает длину окружности с радиусом r

          :param r: радиус круга
          :type r: float
          :returns: длина окружности
          :rtype: float
      """
      return 2 * math.pi * r
  ```
  Функция вычисляет длину окружности. Она принимает 1 аргумент: радиус окружности типа float (или int) 
  и возвращает длину окружности типа float (или int).
  ### Пример вызова:
  ```python
  p = perimeter(1)  # В p запишется 6.28
  ```
  
# История изменения проекта
## Коммиты

| Название                      | Хеш      | Автор                           | Дата             | Описание                                  |
|-------------------------------|----------|---------------------------------|------------------|-------------------------------------------|
| circle docs                   | c067f4fc | Nikita Aksenov <me@nawinds.top> | 28/09/2024 09:38 | Добавлена документация для круга          |
| triangle docs                 | 27c6ec58 | Nikita Aksenov <me@nawinds.top> | 28/09/2024 09:31 | Добавлена документация для треугольника   |
| rectangle docs                | d5d20b39 | Nikita Aksenov <me@nawinds.top> | 28/09/2024 09:21 | Добавлена документация для прямоугольника |
| square docs                   | b8c6acd2 | Nikita Aksenov <me@nawinds.top> | 28/09/2024 09:12 | Добавлена документация для квадрата       |
| General solution description  | 916e5e94 | Nikita Aksenov <me@nawinds.top> | 28/09/2024 09:03 | Изменен rectangle.md                      |
| modified rectangle.py         | 1d53844e | Nikita Aksenov <me@nawinds.top> | 25/09/2024 09:02 | Изменен rectangle.md                      |
| added triangle.py             | 06fc55e6 | Nikita Aksenov <me@nawinds.top> | 25/09/2024 09:01 | Добавлен triangle.md                      |
| added rectangle.py            | 74f5242e | Nikita Aksenov <me@nawinds.top> | 25/09/2024 08:59 | Добавлен rectangle.md                     |
| L-03: Docs added              | d078c8d9 | smartiqa <info@smartiqa.ru>     | 04/03/2021 14:55 | Добавлен README.md                        |
| L-03: Circle and square added | 8ba9aeb3 | smartiqa <info@smartiqa.ru>     | 04/03/2021 14:54 | Добавлены circle.py и square.py           |
