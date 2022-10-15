# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = input('Enter a real number: ')
sum = 0 

for i in num:
    if i != '.' and i != ',':
        sum += int(i)
print(f'The sum of the elements of the entered numbers is {sum}')