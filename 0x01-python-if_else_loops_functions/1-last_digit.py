#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Get the las digit of the number
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit
# Print the result
print("Last digit of {} is {}".format(number, last_digit), end=" ")
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
