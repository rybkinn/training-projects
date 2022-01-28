"""
Николаю требуется проверить, возможно ли из представленных отрезков
условной длины сформировать треугольник.
Для этого он решил создать класс TriangleChecker,
принимающий только положительные числа.
С помощью метода is_triangle()
возвращаются следующие значения (в зависимости от ситуации):
– Ура, можно построить треугольник!;
– С отрицательными числами ничего не выйдет!;
– Нужно вводить только числа!;
– Жаль, но из этого треугольник не сделать.
"""


class TriangleChecker:
    def __init__(self, *args):
        self._args = args

    def is_triangle(self):
        if self._args is not None and len(self._args) == 3:
            for item in self._args:
                if not isinstance(item, (int, float)):
                    return 'Нужно вводить только числа!'
                elif item < 0:
                    return 'С отрицательными числами ничего не выйдет!'
            args_sorted = sorted(self._args)
            if args_sorted[0] + args_sorted[1] > args_sorted[2]:
                return 'Ура, можно построить треугольник!'
            else:
                return 'Жаль, но из этого треугольник не сделать.'


# Тесты
triangle_1 = TriangleChecker(2, 3, 4)
triangle_2 = TriangleChecker(77, 3, 4)
triangle_3 = TriangleChecker(77, 3, 'Сторона3')
triangle_4 = TriangleChecker(77, -3, 4)

triangles = [triangle_1, triangle_2, triangle_3, triangle_4]

for triangles_object in triangles:
    print(triangles_object.is_triangle())
