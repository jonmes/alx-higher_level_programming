#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if(number > 0):
    if(int(repr(number)[-1]) > 5):
        print(f"Last digit of {number} is {int(repr(number)[-1])}\
 and is greater than 5")
elif(int(repr(number)[-1]) == 0):
    print(f"Last digit of {number} is {int(repr(number)[-1])}\
 and is 0")
else:
    if(number < 0):
        print(f"Last digit of {number} is {-int(repr(number)[-1])}\
 and is less than 6 and not 0")
    if(number > 0):
        print(f"Last digit of {number} is {int(repr(number)[-1])}\
 and is less than 6 and not 0")
