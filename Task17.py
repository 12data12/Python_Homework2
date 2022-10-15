# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на введенных пользователем позициях.

n = int(input('Enter an integer: '))
numbers = []
for i in range (-n, n+1):
    numbers.append(i)
print(numbers)

index1 = int(input('Enter the first element index: '))
index2 = int(input('Enter the second element index: '))

print(f'First element is {numbers[index1 - 1]}')
print(f'Second element is {numbers[index2 - 1]}')
print(f'the product of the element is {(numbers[index1-1])*(numbers[index2-1])}')