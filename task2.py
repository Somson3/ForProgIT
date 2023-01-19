class Goods:

    def __init__(self, good, price, product_description, dimensions_of_the_product):
        self.good = good
        self.price = price
        self.product_description = product_description
        self.dimensions_of_the_product = dimensions_of_the_product
        self.type = 'good'

    def __str__(self):
        return f'{self.good} - {self.price} {self.product_description}.'


class Shopper:

    def __init__(self, surname, name, phone_number, dimensions_of_the_product):
        self.surname = surname
        self.name = name
        self.phone_number = phone_number
        self.dimensions_of_the_product = dimensions_of_the_product
        self.type = 'shopper'

    def __str__(self):
        return f'{self.surname} - {self.name} {self.phone_number} {self.dimensions_of_the_product}.'


class Zakaz:

    def __init__(self, shoper):
        self.shoper = shoper
        self.goods = []
        self.quantities = []

    def add_good(self, good, quantities):
        self.goods.append(good)
        self.quantities.append(quantities)

    def zakaz_sum(self):
        return sum(self.goods[i].price*self.quantities[i] for i in range(len(self.goods)))


    def __str__(self):
        return f'{self.shoper, self.goods, self.quantities, self.price}'



x_1 = Goods('banana', 40, 'good banana', '1x2x3')
x_2 = Goods('milk', 25, 'good milk', '3')
x_3 = Goods('bread', 20, 'white bread with raisins and poppy seeds', '500 g.')



ivanov = Shopper('Ivanov', 'Ivan', '066 817 20 35', 5)
petrov = Shopper('Petrov', 'Nikolay', '067 320 20 55', 2)
sidorov = Shopper('Sidorov', 'Ura', '063 138 40 89', 4)
kovalenko = Shopper('Kovalenko', 'Dmutro', '063 658 50 78', 1)



# zakaz_1 = Zacaz('Ivanov')
# zakaz_1.add_good(x_1, 5)
#
# zakaz_2 = Zacaz('Peterov')
# zakaz_2.add_good(x_1, 5)




zakaz1 = Zakaz(ivanov)
zakaz1.add_good(x_1, 5)
zakaz1.add_good(x_2, 3)
print(zakaz1.shoper, zakaz1.zakaz_sum())

















# f = {
#      0 :"zero",
#      1: "one",
#      2: "two",
#      3: "three",
#      4: "four",
#      5: "five",
#      6: "six",
#      7: "seven",
#      8: "eight",
#      9: "nine"
#     }
# l = {
#
#     10: 'ten',
#     11: 'eleven',
#     12: 'twelve',
#     13: 'thirteen',
#     14: 'fourteen',
#     15: 'fifteen',
#     16: 'sixteen',
#     17: 'seventeen',
#     18: 'eighteen',
#     19: 'eighteen',
#     20: 'twenty',
#     30: 'thirty',
#     40: 'forty',
#     50: 'fifty',
#     60: 'sixty',
#     70: 'seventy',
#     80: 'eighty',
#     90: 'ninety'
#     }
#
# class_dict = {
#     1: "hundred",
#     2:"thouthend",
#     3:"milion"
# }
#
# x = 123.60
# n = str(2585.52)
# # n = input("number",)
# a = n.split(".")
# print(a)
# dol = a[0]
# # q = len(dol)
# print(dol)
# # print(q)
#
#
#
# # def dolars():
# #     v = " "
# #     dollar_len = len(dol[0])
# #     if dollar_len == 4:
# #        dol[0] + "thousand " + " "
# #
# #     elif dollar_len == 3:
# #         a[0] + "hundred" + " "
# #     else:
# #         pass
#
#
#     for w in a[0]:
#         v = v + f.get(int(w)) + " "
#
#     return v
# def cent(cen):
#
#     res = " "
#     if len(cen[1]) == 1:
#         cen[1] += "0"
#         cent_1 = int(cen[1])
#
#         res = l.get(cent_1)
#     else:
#         if cen[1][0] == "0":
#             res = f.get(int(cen[1][1]))
#         else:
#             res = f'{l.get(int(cen[1][0]+"0"))} {f.get(int(cen[1][1]))}'
#                 # res = res + f.get(int(p)) + " "
#
#
#     return res
# # print(cent())
#
# print(f"{dolars()} dlars {cent(a)} cent")


# import turtle
#
# def move(a):
#     turtle.forward(a)
#     turtle.left(90)
# def drawSqweare(a):
#     for i in range(4):
#         move(a)
#
# def drawSqweareColor(a, color):
#     turtle.color(color)
#     turtle.begin_fill()
#     drawSqweare(a)
#     turtle.end_fill()
#
# drawSqweareColor(50, "red")
# turtle.goto(150, 150)
#
# drawSqweareColor(300, "green")


# def square(x):
#     print(x**2)


# def factorial(x):
#     pr = 1
#     for i in range(2, x + 1):
#         pr = pr * i
#     return pr
#
# for i in range(1, 8):
#     print(i, factorial(i))
# def socher(n, k):
#     return factorial(n)/(factorial(k) * factorial(n-k))
# print(socher(5, 3))


# def s():
#     a, b, c = 1, 2, 4
#     print(a, b, c)
#
# w = "hello"
#
# s()


# def even(a):
#     if a % 2 == 0:
#         print(a, 'chetnoe')
#     else:
#         print(a, 'ne chetnor')
#
#
#
# for i in range(20, 31):
#     even(i)

# def factorial(n):
#     pr=1
#     for i in range(2, n + 1):
#         pr = pr * i
#     print(pr)
# factorial(5)


# def square(x):
#     return x ** 2
#
# a = square(square(3))
# print(a)


# def squre(x):
#     return (x**2)
#
#
# def exampel():
#     print(1)
#     print(2)
#     return ("hello")
#     print(3)
#     print(4)


# exampel()


# def even(x):
#     return x % 2 == 0
#
#
# for i in range(1, 11):
#     print(i, even(i))
#
# def sqAndPer(a,b):
#     mas = []
#     mas.append(a * b)
#     mas.append(2 * (a + b))
#     return mas
#
#
# print(sqAndPer(2, 6))


# def dollars_cents(money: str):
#     money = money.split('.')
#     if len(money) == 1:
#         return money[0], '00'
#     if len(money) == 2:
#         return money[0], money[1]
#
#     return None
#
#
# def number_0_999_to_str(number: str):
#     numbers = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
#                10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'eighteen',
#                20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
#     if 0 <= int(number) <= 19:
#         return numbers[int(number)]
#     if 20 <= int(number) <= 99:
#         tens, units = number
#         tens, units = int(tens) * 10, int(units)
#         return f'{numbers[tens]} {numbers[units]}'
#     if 100 <= int(number) <= 999:
#         hundreds, tens, units = number
#         hundreds, tens, units = int(hundreds), int(tens) * 10, int(units)
#         return f'{numbers[hundreds]} hundreds {numbers[tens]} {numbers[units]}'
#
#     return None
#
# def get_triads(number):
#     triads = []
#     while number:
#         triads.append(number[-3:])
#         number = number[:-3]
#     return triads
#
# def transform_nimber_to_str(number):
#     numbers = ['', 'thousands', 'millions', 'billions']
#     triads = get_triads(number)
#     res = list(zip(triads, numbers[-len(numbers):]))
#     res_str = ''
#     for item in reversed(res):
#         res_str += f'{number_0_999_to_str(item[0])} {item[1]} '
#
#     return res_str
# #
# #
#
# money = input('money=')
# res = dollars_cents(money)
# if res:
#     dollars, cents = res
#     print(dollars, cents)
#     money = transform_nimber_to_str(money)
#     print(money)
#     # res = number_0_999_to_str(dollars)
#     # print(res)
#     #


# def dollars_cent(dollars: str):
#     moneу.split(".")
#     if len(moneу) == 0:
#         return moneу[0], '00'
#     if len(moneу) == 2:
#         return moneу[0], moneу[1]
#
#     return None
#
# def number_0_999_to_str(number: str):
#     numbers = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
#                 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'eighteen',
#                 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
#
#
# if 0 <= int(number) <= 19:
#     return numbers[int(number)]
#
# if 20 <= int(number) <= 99:
#     tens, units = number
#     tens, units = int(tens) * 10, int(units)
#     return f'{numbers[tens]} {numbers[units]}'
# if 100 <= int(number) <= 999:
#     hundreds, tens, units = number
#     hundreds, tens, units = int(hundreds), int(tens) * 10, int(units)
#     return f'{numbers[hundreds]} hundreds {numbers[tens]} {numbers[units]}'
#
# return None
#
# # if 0 <= int(number) <= 19:
# #     return numbers[int(number)]
# # if 20 <= int(number) <= 99:
# #     return tens, units = number
# #     tens, units = int(tens) * 10, int(units)
# #     return f"{numbers[tens] {numbers[units]}"
# # if 100 <= int(namber) <= 999:
# #     hundereds, tens, units = number
# #     hundereds, tens, units = int(hundereds), int(tens) * 10, int(units)
# #     return f"{numbers[hundereds]} hundreds {numbers[tens]} {numbers[tens]}"
# #
# # return None
#
# def get_triads(number):
#     triads = []
#     triads.append(number[-3:])
#     number = number[:-3]
#     return triads
#
# def transform_nimber_to_str(number):
#     numbers = ['', 'thousands', 'millions', 'billions']
#     triads = get_triads(number)
#     res = list(zip(triads, numbers[-len(numbers):]))
#     res_str = " "
#     for item in reversed(res):
#         res_str += f"{number_0_999_to_str(item[0])} {item[1]} "
#
#     return res_str
#
#
# moneу = str(123.34)
# res = dollars_cent(moneу)
# if res:
#     dollars, cents = res
#     print(dollars, cents)
#     money = transform_nimber_to_str(number)
#     print(money)
#


# def transform_number_0_999_to_str(number):
#
#     numbers = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
#                9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
#                17: 'seventeen', 18: 'eighteen', 19: 'eighteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
#                60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
#
#     if 0 <= int(number) <= 20:
#         return numbers(int(number))
#     if 20 <= int(number) <= 100:
#         tens, ones = int(number[0]) * 10, int(number[1])
#         ones = "" if ones == 0 else numbers[ones]
#         return f"{numbers[tens]} {number[ones]}"
#
#     if 100 <= int(number) <= 1000:
#         hundrens, tens, ones = int(number[0]), int(number[1]) * 10, int(number[2])
#         ones = "" if ones == 0 else numbers[ones]
#         return f"{numbers[hundrens]} handrens {numbers[tens]} {number[ones]}"
#
#
#
#
# def number_to_triads(number: str):
#     res = []
#     while number:
#         res.append(number [-3:])
#         number = number[:-3]
#     return res[::-1]
#
# def number_to_dollars_cents(number: str):
#     number = number.split(",")
#     if len(number) == 1:
#         return number[0], "00"
#     if len(number) == 2:
#         return number[0], number[1]
#     raise ValueError()
#
#
# def transform_in_to_mani(number):
#     dollars, cent = number_to_dollars_cents(number)
#     dollars = number_to_triads(number)
#     res = " "
#     for item in dollars:
#         res += transform_number_0_999_to_str(item)
#
#     return res
#
#
#
# number = input('price = ').strip()
# print(transform_in_to_mani(number))
#

# Домашка цикли
# ____________________________________________________________________________________
# Задача 5
# x = [0, 5, 2, 4, 7, 1, 3, 19]
# n = 0
# for i in x:
#     if i % 2 == 0:
#         continue
#     else:
#         if i % 2 != 0:
#             n += 1
# print("Не парних чисел ", n)
#
# # Задача 5, варівнт 2
# x = [0, 5, 2, 4, 7, 1, 3, 19]
# d = [i for i in x if i % 2]
# x = len(d)
# print("Не парних чисел ", x)


# ____________________________________________________________________________________
# Задача 1
#  Написати Python-скрипт, який виводить на екран усі числа в діапазоні від 1 до 100 кратні 7.

# z = [i for i in range(1, 101,) if i % 7 == 0]
# print(z)

# З лекції
# z = [i for i in range(7, 101, 7) if not i % 7]
# print(z)

# ____________________________________________________________________________________
# Задача 2
# Написати Python-скрипт, який обчислює за допомогою циклу факторіал числа n (n вводиться з клавіатури).


# n = int(input("Введіть число  "))
# res = 1
# for i in range()


# ____________________________________________________________________________________
# Задача 3
# Записати Python - скрипт, який виводить на екран таблицю множення на 5. Переважно друкувати
# 1 x 5 = 5, 2 x 5 = 10, а не просто 5, 10, ...


# a = 5
# for i in range(1, 11):
#     z = 0
#     while z < 1:
#         s = a * i
#         z += 1
#         print(f"{a} * {i} = {s} ")


# з Лекції
# for i in range(1, 11):
#     print(f'{i} * 5 = { i * 5 } ')
# ____________________________________________________________________________________
# # Задача 4
# Написати Python - скрипт, який виводить на екран прямокутник із '*'.Висота і ширина прямокутника
# вводяться з клавіатури.Наприклад, нижче представлений прямокутник з висотою 4 та шириною 5.


# a = int(input("Введіть висоту "))
# b = int(input("Введіть ширину "))
#
#
# res = f"{'*' * a}\n" + f"*{' ' * (b - 2)}*\n" * (a - 2) + f"{'*' * b}\n"
# print(res)

# print(f"{'*' * b}")
# for i in range(a - 2):
#     print(f"*{' ' * (b - 2)}*")
# print(f"{'*' * b}")

# ____________________________________________________________________________________
# # Задача 5
# Є список [0,5,2,4,7,1,3,19]. Написати Python-скрипт для підрахунку непарних цифр у ньому.

# n = [0, 5, 2, 4, 7, 1, 3, 19]
# res = [i for i in n if i % 2]
# print(len(res))

# ____________________________________________________________________________________
# Задача 6

# Створіть список випадкових чисел (розміром 4 елементи). Створіть другий список у два рази більше першого,
# де перші 4 елементи повинні дорівнювати елементам першого списку,
# а решта елементів - подвоєним значенням початкових.

# import random
# n = [random.randint(1, 10) for _ in range(4)]
# s = []
# v = s + n
# for i in n:
#     s = i * 2
#     v.append(s)
# print(n)
# print(v)

# f = [s.append(n), i * 2 for i in s]
#  print(f)
# намагався записати в один рядок


# x =
# ____________________________________________________________________________________
# # Задача 7

# Створіть список із 12 елементів. Кожен елемент цього списку є зарплатою робітника за місяць.
# Виведіть цей список на екран та обчисліть середньомісячну зарплату цього робітника.

# import random
#
# b = [x for x in random.randint(7500, 12800)]
# s = sum(b)/12
#
# print(b)
# print(s)
#


# ____________________________________________________________________________________
# Задача 8

# s = 0
# x = [[1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]]
#
# for row in x:
#     print("\t".join(map(str, row)))
#     s += sum(row)
# print(s)


# ____________________________________________________________________________________
# Задача 9

# n = int(input("Введіть довжину списку  "))
# my_list = []
# for i in range(n + 1):
#     my_list.append(i)
# print(my_list)
# print(my_list.reverse())


# _____________________________________________________________________________________
#
# Задача 10


# for n in range(2, 101):
#
#     for i in range(2, n):
#         if not n % i:
#             break
#     else:
#         print("Чсисло ", n, 'просте')


# _____________________________________________________________________________________

# Задача 11

# v_list = []
# n = int(input("n = "))
#
#
#
# spaice = 0
# for stars in range(n, 0, -2):
#     v_list.append(f"{' ' * spaice }{ '*' * stars}")
#     spaice += 1
# v_list += v_list[-2::-1]
# print("\n".join(v_list))

# ---------------------------------------------------------------------------------------------------------------


# Домашка Словники та Множини

# _____________________________________________________________________________________________
# Задача 1
# day = int(input("Введіть число  "))
# namber = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Saturday"}
#
# print(namber.get(day, "Error Input"))

# _____________________________________________________________________________________________
# Задача 2

# dict_cat = {"name":"Васька", "age": 5, "color": "blak"}
# print(dict_cat)


# _____________________________________________________________________________________________
# Задача 3
# text = input("text = ")
# #
# x = {}
# for item in set(text):
#     x[item] = text.count(item)
# print(x)

# _____________________________________________________________________________________________
# Задача 4

# text = set(input("Введіть текст  "))
# text_2 = set(input("Введіть текст  "))
# text.intersection(text_2)
# # x.intersection_update(x_2)
# print(text)
#

# _____________________________________________________________________________________________
# Задача 5


# x = [s for s in range(3, 100) if s % 3 == 0]
# z = [b for b in range(5, 100) if b % 5 == 0]

# print(z)
# print(len(z))
# print(x)
# print(len(x))

# _____________________________________________________________________________________________
# Задача 6

# x = [s for s in range(3, 30) if s % 3 == 0]
# z = [b for b in range(5, 40) if b % 5 == 0]
# print(x)
# print(z)
# f = set(x) & set(z)
# # f.sort()
#
# print(f)

# Варіант 2

# x = set([s for s in range(3, 30) if s % 3 == 0])
# z = set([b for b in range(5, 30) if b % 5 == 0])
# x.update(z)
# print(x)


# text = input("Введіть речення ")
# # bed = {"*", "**", "***"}
# # if set(text.split()) & bed:
# #     print("no")
# # else:
# #     print("ok")


# def func(name, lang="uk"):
#     if lang =='uk':
#         return f'Привіт, {name}'
#
#     if lang =='en':
#         return f'Hello , {name}'
#
#     return None
#
# print(func('Oleh', lang ='en'))
#
