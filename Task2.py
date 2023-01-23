# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 2, 2: 2,25, 3: 3,37, 4: 2,44, 5: 2,49, 6: 2,52}

# num = int(input("Введите число: "))
# my_dict1 = {}

# for i in range(1, num + 1):
#     my_dict1[i] = round(((1 + (1 / i)) ** i), 2)

# summ = 0
# for i in range(1, len(my_dict1) + 1):
#     summ += my_dict1[i]

# print(my_dict1)
# print(f"Сумма чисел в словаре равна {summ}")

# \\\\\\\\\\\\\\\\\\\\\\\\\\
# стало
# \\\\\\\\\\\\\\\\\\\\\\\\\\\

num = int(input("Введите число: "))
temp = list(i for i in range(1, num + 1))
my_dict = dict(enumerate(map(lambda i: round(((1 + (1 / i)) ** i), 2), temp), start=1))
print(my_dict)
print(f"Сумма чисел в словаре равна {sum(my_dict.values())}")