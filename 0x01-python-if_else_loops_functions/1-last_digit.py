#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numbers= str(number)
numberL=numbers[-1:]
number1=int(numberL)
if (numbers[0]=='-'):
    print(f'Last digit of {number} is -{number1} and is less than 6 and not 0')
else:
    if (number1>5):
        print(f'Last digit of {number} is {number1} and is greater than 5')
    elif(number1 == 0):
        print(f'Last digit of {number} is {number1} and is 0')
    else:
        print(f'Last digit of {number} is {number1} and is less than 6 and not 0')
