#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
5	    print(f"{number} is positive")
6	elif number < 0:
7	    print(f"{number} is negative")
8	else:
9	    print(f"{number} is zero")
