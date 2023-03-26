# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке
# возрастания все те числа,которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n = int(input("Введите колисество элементов множества n: "))
m = int(input("Введите колисество элементов множества m: "))
print("Введите целые числа множества n:")
firstSet = [int(input()) for i in range(n)]
print("Введите целые числа множества m:")
secondSet = [int(input()) for i in range(m)]
print(firstSet)
print(secondSet)
firstSet = set(firstSet)
secondSet = set(secondSet)
result = set()
for i in firstSet:
    for j in secondSet:
        if i == j:
            result.add(i)

print("Числа встречающиеся в обоих множествах: ")
print(result)


