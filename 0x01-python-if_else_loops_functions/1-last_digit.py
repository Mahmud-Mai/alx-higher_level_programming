#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dgit = int(repr(number)[-1])
if last_dgit > 5:
    print(f"The last digit of {number} is {last_dgit} and is greater than 5")
elif last_dgit == 0:
    print(f"The last digit of {number} is {last_dgit} and is 0")
elif last_dgit < 6 and last_dgit != 0:
    print(f"The last digit of {number} is {last_dgit} and is less than 6 and not 0")
