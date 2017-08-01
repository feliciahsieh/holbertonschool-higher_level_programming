#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
text_last_digit = "Last digit of"
text_is = "is"
text_greater_5 = "and is greater than 5"
text_zero = "and is 0"
text_less_6 = "and is less than 6 and not 0"

if number < 0:
    last_digit = -((-1*number) % 10)
else:
    last_digit = number % 10

if last_digit > 5:
    print(text_last_digit, number, text_is, last_digit, text_greater_5)
elif last_digit == 0:
    print(text_last_digit, number, text_is, last_digit, text_zero)
else:
    print(text_last_digit, number, text_is, last_digit, text_less_6)
