# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

n = int(input('Enter an integer : '))

my_list = [round((1+1/n)**n, 2) for n in range(1, n+1)]
print(my_list)
print(f'The sum is {round(sum(my_list), 2)}')