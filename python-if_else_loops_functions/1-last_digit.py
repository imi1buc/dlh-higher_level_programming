#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit = -1 * last_digit
else:
    last_digit
first_str = "Last digit of " + str(number) + " is " + str(last_digit) + " and is "
if last_digit > 5:
    print(first_str + "greater than 5")
elif last_digit == 0:
    print(first_str + "0")
else:
    print(first_str + "less than 6 and not 0")
