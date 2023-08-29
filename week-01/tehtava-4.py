import random

a = random.randint(0, 10)
b = random.randint(0, 10)

def sum(a, b):
    return a + b

print(f'Number A: {a}')
print(f'Number B: {b}')
print(f'Sum of numbers {a} and {b} is {sum(a, b)}')
