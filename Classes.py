# # def print_hi(name):
# #     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
# #
# # if __name__ == '__main__':
# #     print_hi('PyCharm')
#
# class Figure:
#     s = 100
#     def get_per(self):
#         raise MemoryError("Добавьте метод нахождения периметра")
#
# class Square(Figure):
#     def __init__(self, a):
#         self.a = a
#
#     def get_per(self):
#         return self.a*4
#
# class Rectangular(Figure):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def get_per(self):
#         return (self.a+self.b)*2
#
# class Triangle(Figure):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_per(self):
#         return self.a+self.b+self.c
#
#
# sq1 = Square(5)
# sq2 = Square(6)
# rect1 = Rectangular(3, 4)
# rect2 = Rectangular(5, 6)
# tr1 = Triangle(2, 3, 4)
# tr2 = Triangle(5, 6, 7)
#
# geom = [sq1, sq2, rect1, rect2, tr1, tr2]
# for i in geom:
#     print(i.get_per())
#
# # print(sq1.get_per_sq(), sq2.get_per_sq())
# # print(rect1.get_per_rect(), rect2.get_per_rect())
# # print(tr1.get_per_tr(), tr2.get_per_tr())
#

# a = list(range(1, 8))
# b = [i for i in a if i%2 == 0]
# print(b)
# bb = list(filter(lambda x: not x%2, a))
# print(bb)

"""**************************************************************************************************************"""


# class Cat:
#     __height = 0
#     def __init__(self, name: str, colour: str):
#         self.name = name
#         self.colour = colour
#
#     def cat_meow(self):
#         print(f"I'm {self.name} and my colour is {self.colour}")
#
#     def cat_set_height(self, height):
#         Cat.__height = height
#
#     def cat_jump(self):
#         print(f"I can jump in {self.__height} meters")
#
#
# Vaska = Cat("Васька", "brown")
# Vaska.colour = 'red'
# Vaska.cat_meow()
# Vaska.cat_set_height(7)
# Vaska.cat_jump()
# Vaska._Cat__height = 9
# Vaska.cat_jump()
#
# class LittleCat(Cat):
#
#     def __init__(self, game: str):
#         super().__init__(self)
#         self.game = game
#
#     def littleCat_play(self):
#         print(f"I like to play with a {self.game}")
#
# Maly = LittleCat("Feather")
# print(Maly.name)


class Dog:
    """Описание класса собаки"""

    def __init__(self, name: str, age: int = 10):
        self.name = name
        self.age = age

    def lai_dog(self):
        return "Gav-gav!"


d = Dog("Dina", 5)
print(d.age)
print(d.lai_dog())

class LittleDog(Dog):
    """Описание класса маленькой собаки"""

    def lai_littledog(self):
        return "Tiafff-tiafff!"

poppy = LittleDog("Poppy", 3)
print(f"Little dog is {poppy.name} and she is {poppy.age}")
print(poppy.lai_littledog())
print(poppy.lai_dog())
