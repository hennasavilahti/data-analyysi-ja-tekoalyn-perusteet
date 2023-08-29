import random

a = random.randint(0, 100)
b = random.randint(0, 100)

print(f'a: {a}')
print(f'b: {b}')

if(a > b):
    print("Number A is bigger than B")

elif(b > a):
    print("Number B is bigger than A")

else:
    print("Numbers are equal")
