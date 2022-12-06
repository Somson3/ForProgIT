# Exercise 1.
# print("Hello world")
#
# # Exercise 2._______________________________________________
#
# a = "I study programming"
# print(a)
# b = "Programming in Python is interesting"
# print(b)
# c = "The war is raging. Help."
# print(c)

# Exercise 4._____________________________________________

# a = int(input(" Enter an integer "))
# b = int(input(" Enter an integer "))
# c = a + b
# d = a * b
# i = a - b
# f = a / b
# print(f"sum {c}, product {d}, difference {i}, quotient {f}")


# Exercise 3._____________________________________________

# a = int(input(" Enter he width of the rectangle  "))
# b = int(input(" Enter the length of the rectangle  "))
# s = a * b
# print("Area of rectangle", s)


# Exercise 5._____________________________________________

# radius = int(input("Enter radius:"))
# Pi = 3.14159
# if radius > 0:
#     print("Длина окружности: ", 2*Pi*radius)
#     print("Площадь равна =  ", Pi*radius**2)
# else:
#     print("Введите положительное число")

# Домашнє завдання 2

# Exercise 1._____________________________________________

# a = "123"
# print(int(a))

# Exercise 2._____________________________________________

# a = 123
# print(float(a))
#
# Exercise 3._____________________________________________

# a = 12.345
# print(int(a))

# Exercise 4._____________________________________________

# bank_card = 2075_2580_3045_4560_8555
# print(bank_card % 10000)

# Exercise 5._____________________________________________

# a = input("Введіть число ")
# print(sum(map(int, a)))

# Exercise 6._____________________________________________

# a = int(input("Введіть число "))
# b = int(input("Введіть число "))
# c = int(input("Введіть число "))
#
# p = (a + b + c) / 2
# plosha = (p * (p - a)*(p - b)*(p - c) ** 0.5)
# print(plosha)

# Exercise 6_1._____________________________________________

# x = input("Введіть число  ")
# print(len(x))

# Exercise 6_2._____________________________________________

# x = input("Введіть число  ")
# print(x[::-1])


# Домашнє завдання 3

# Exercise 1._____________________________________________

# x = int(input("Введіть відємне число   "))
# if x < 0 and x != 0:
#     print(x)
# else:
#     print(" Ви не ввели відємне число")


# Exercise 2._____________________________________________

# a = int(input("Введіть число "))
# if a < 20 and a != 0:
#     print(f"Число {a} меньше  20 ")
# elif a == 0:
#     print(f"Число {a} меньше  20 ")
# elif a == 20:
#     print(f"Число {a} = 20 ")
# else:
#     print(f"Число {a} більше 20")

# Exercise 3._____________________________________________

# a = int(input("Введіть число  "))
# if a != 0:
#     print(f"Введе число {a} не дорівнює 0  ")
# elif a == 0:
#     print(f"Введе число {a} дорівнює 0  ")

# Exercise 4._____________________________________________

# a = int(input("Введіть число  "))
# if a % 2 == 0:
#     print("Число парне ")
# elif a % 2 != 0:
#     print("Число непарне ")

# Exercise 5._____________________________________________

# a = int(input("Введіть число  "))
# b = int(input("Введіть число  "))
# c = int(input("Введіть число  "))
#
# if a > b > c:
#     print(a)
# elif b > a > c:
#     print(b)
# elif c > b > a:
#     print(c)