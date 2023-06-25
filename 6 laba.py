class Point:
    def __init__(self, x, y, a, b, p):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.p = p

        if self.x != None and self.y != None:
            if not ((self.y ** 2) % self.p == (self.x ** 3 + self.a * self.x + self.b) % self.p):
                raise ValueError("Точка не находится на кривой")
        

    def __add__(self, other):
        # Если мы складываем точку с самой собой, то удваиваем ее, используя метод double()
        if self.x == other.x and self.y == other.y:
            return self.double()

        # Если x-координаты двух точек равны, то результатом
        # сложения является точка (None, None)
        if self.x == other.x:
            return Point(None, None, self.a, self.b, self.p)

        # Вычисляем коэффициенты x и y
        s = (other.y - self.y) * pow(other.x - self.x, -1, self.p)
        x = (s ** 2 - self.x - other.x) % self.p
        y = (s * (self.x - x) - self.y) % self.p

        return Point(x, y, self.a, self.b, self.p)

    def double(self):
        # Вычисляем коэффициенты x и y
        s = (3 * self.x ** 2 + self.a) * pow(2 * self.y, -1, self.p)
        x = (s ** 2 - 2 * self.x) % self.p
        y = (s * (self.x - x) - self.y) % self.p

        return Point(x, y, self.a, self.b, self.p)

# Функция для нахождения точек, которые принадлежат кривой
get_points_on_curve = lambda a, b, p: [Point(x, y, a, b, p) for x in range(p) for y in range(p) if (y ** 2) % p == (x ** 3 + a * x + b) % p]

# Пример использования:
p = 5
a = 2
b = 1

points = get_points_on_curve(a, b, p)

for point in points:
    print(f"({point.x}, {point.y})")

# Находим сумму точек (2, 4) и (3, 5)
point1 = Point(1, 2, a, b, p)
point2 = Point(3, 2, a, b, p)
point3 = Point(0, 1, a, b, p)

sum_point = point1 + point2
print(f"Сумма двух точек ({point1.x}, {point1.y}) и ({point2.x}, {point2.y}): ({sum_point.x}, {sum_point.y})")

# Находим удвоение точки (2, 4)
double_point = point3.double()
print(f"Удвоение точки ({point3.x}, {point3.y}): ({double_point.x}, {double_point.y})")

# Делаем проверку, что удвоение точки эквивалентно сложению точки с ей самой
sum_point = point3 + point3
print(f"Сумма точки ({point3.x}, {point3.y}) с ей самой: ({sum_point.x}, {sum_point.y})")
