"""
ls = [0, 1, 3, 6, 10]
ls = [1, 3, 6, 10]
ls = [3, 6, 10]
ls = [6, 10]
ls = [10]
ls = []
[20, 20, 19, 16, 10, 0]

ls = [1, 2, 3, 4, 5, 6]
parts_sums(ls) -> [21, 20, 18, 15, 11, 6, 0]

ls = [744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]
parts_sums(ls) -> [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]
"""

# def parts_sums(ls):
#     return [sum(ls[i:]) for i in range(len(ls)+1)]
#
# print(parts_sums([0, 1, 3, 6, 10]))

# def parts_sums(ls):
#     sum_ls = sum(ls)
#     # res = [sum_ls]
#     res = []
#     for i in range(len(ls)):
#         sum_ls -= ls[i]
#         res.append(sum_ls)
#         print(sum_ls)
#
#     return res
#
# rt = parts_sums([0, 1, 3, 6, 10])
# print(rt)


"""
Print the list of all directories and subdirectories
"""

# import os
#
# parent_dir = os.getcwd()
# print(parent_dir)
# target_dir = "/Users/Sasha"
# os.chdir(target_dir)
# print("Went to directory: " + os.getcwd())
# print("This directory contains the next dirs and files:")
# for i in os.listdir():
#     if os.path.isdir(i) and not str(i).startswith("."):
#         print(f"- {i}")
#         sbd = target_dir + "/" + i
#         print(sbd)
#         for subdir in os.listdir(sbd):
#             print(subdir)
#             if os.path.isdir(sbd) and not str(sbd).startswith("."):
#                 print(f"   - {subdir}")


# with open(f"{parent_dir}/NF.txt", "w", encoding="UTF-8") as file:
#     for i in os.listdir():
#         file.write(f"- {i} \n")

#
# def nested(spisok: list, level=1):
#     print(f"{spisok}, level = {level}")
#     for i in spisok:
#         if type(i) == list:
#             nested(i, level + 1)
#
# a = [1, 2, 4, [4, 2, [4, 3]], 4, 5, [2, 3, [4, 3, 2, [5, 6, [5]]]]]
# nested(a)


"""
Напишите декоратор debug, который при каждом вызове декорируемой функции выводит её имя (вместе со всеми передаваемыми аргументами), а затем — какое значение она возвращает. После этого выводится результат её выполнения.


Результат:
Вызывается greeting('Том')
'greeting' вернула значение 'Привет, Том!'
Привет, Том!

Вызывается greeting('Миша', age=100)
'greeting' вернула значение 'Ого, Миша! Тебе уже 100 лет, ты быстро растёшь!'
Ого, Миша! Тебе уже 100 лет, ты быстро растешь!

Вызывается greeting(name='Катя', age=16)
'greeting' вернула значение 'Ого, Катя! Тебе уже 16 лет, ты быстро растёшь!'
Ого, Катя! Тебе уже 16 лет, ты быстро растешь!

['__new__', '__repr__', '__call__', '__get__', '__closure__', '__doc__', '__globals__', '__module__', '__builtins__', '__code__', '__defaults__', '__kwdefaults__', '__annotations__', '__dict__', '__name__', '__qualname__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
None
"""


#
# def debug(func):
#     def wrapper(*args, **kwargs):
#         func_name = func.__name__
#         data = (", ".join([i for i in args] + [f"{k} = {v}" for k, v in kwargs.items()]))
#         print(f"Вызывается {func_name}({data})")
#         print(f"{func_name} вернула значение '{func(*args, **kwargs)}'")
#     return wrapper
#
# @debug
# def greeting(name, age=None):
#     if age:
#         return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
#     else:
#         return "Привет, {name}!".format(name=name)
#
#
# print(greeting("Том"))
# print(greeting("Миша", age=100))
# print(greeting(name="Катя", age=16))


import datetime


def get_time_execute(func):
    def wrap(*args):
        start = datetime.datetime.now()
        result = func(*args)
        exec_time = datetime.datetime.now() - start
        print(exec_time)
        return result
    return wrap


@get_time_execute
def func1(a: list) -> int:
    summa = 0
    for i in a:
        summa += i
    return summa


@get_time_execute
def func2(a: list) -> int:
    return sum(a)


a = list(range(10 ** 8))
print(func1(a))
print(func2(a))

