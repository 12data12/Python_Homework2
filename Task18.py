# Реализуйте алгоритм перемешивания списка.

import random
x = list(range(0, 10))
print(f'List of 10 random numbers: {x}')
random.shuffle(x)
print (f'List in random order: {x}')