from time import *
c=input("Color? [0-15] ")
print("\x1B["+c+"m",end="")
t=monotonic()
print(t)
sleep(1)
print(monotonic()-t)
from random import *
#seed(1)
c=str(randint(1,15))
print("\x1B["+c+"m",end="")
print(random())
print(uniform(1,6))
print(randint(1,6))
print(choice(range(1,7)))
print(randrange(1,7))
print(getrandbits(4)) # undoc
print("\x1B[0m",end="")