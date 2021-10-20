from itertools import count
from math import factorial
def fact():
    for i in count(1):
        yield factorial(i)
gen = fact()
n = 0
for i in gen:
    if n < 6:
        print(i)
        n += 1
    else:
        break