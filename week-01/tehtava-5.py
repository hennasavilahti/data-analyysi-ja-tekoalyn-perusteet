import random

count = 5
correct_answers = 0
multiplication = []

for i in range(0, count):
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    answer = a*b
    
    user_answer = int(input(f'{a} * {b} = '))
    
    if user_answer == answer:
        correct_answers += 1
        multiplication.append(f'Correct :-) {a} * {b} = {answer}')
    
    else:
        multiplication.append(f'Incorrect :-( Correct answer is: {a} * {b} = {answer}')
        
for i in multiplication:
    print(i)

print(f'You got {correct_answers} answers correct!')

