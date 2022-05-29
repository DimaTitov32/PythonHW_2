# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input("Введите целое число n: "))
for i in range(1, n + 1):
    result = math.pow((1 + (1/i)), i)
    print(result)