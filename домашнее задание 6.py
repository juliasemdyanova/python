

# Задача-1:
# 
# Создать класс треугольник и реализовать в нем конструктор, методы для площади, периметра и вывод на экран.
# В конструкторе сделать проверку на возможность создания такого треугольника, если нет, то написать, что такой треугольник нельзя создать и сделать exit(1)

class Triangle:
    def __init__(self, x=8, y=0, z=2):
        self.x = x
        self.y = y
        self.z = z


    def get_length_of_triangle_side_a(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


    a = get_length_of_triangle_side_a


    def get_length_of_triangle_side_b(self, other):
        return ((self.z - other.z) ** 2 + (self.y - other.y) ** 2) ** 0.5


    b = get_length_of_triangle_side_b


    def get_length_of_triangle_side_c(self, other):
        return ((self.z - other.z) ** 2 + (self.x - other.x) ** 2) ** 0.5


    c = get_length_of_triangle_side_c


    def get_a_triangle_perimeter(a,b,c):
        return(a+b+c)

    def get_a_triangle_area(a,b,c):
        return ((0, 5 * (a + b + c) * (0, 5(a + b + c) - a) * (0, 5(a + b + c) - b) * (0, 5(a + b + c) - c)) ** 0, 5)