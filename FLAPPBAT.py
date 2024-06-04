# Flappy Bat (C) 2024 by Mikael O. Bonnier, Lund, Sweden. License: GPLv3+.
# Flappy Bat
from time import *
from random import *
print("\033[8;mFlappy\033[12;m~\033[8;mBat\033[12;m",end="~"*(22))
print(end=" "*(9*32))
print("\033[8;12m",end=" "*32)
print(end="\033[8;m")
y=9
x1=31
m=True
p=0
t=monotonic()
h=randrange(1,9)
while True:
  print(end="\033[%d;6HY"%int(y))
  if m:
    print(end="\033[%d;%dH"%(h,int(x1))+chr(130))
  sleep(.3)
  if m:
    print(end="\b ")
  a=input("\033[%d;6H \033[9;Hy=%.1f  moths=%d "%(int(y),y,p))
  ts=t
  t=monotonic()
  dt=(t-ts)
  y-=1-1.5*dt
  x1-=(t-ts)
  if m and int(x1)==6 and int(y)==h:
    m=False
    p+=1
  if x1<0:
    x1=31
    m=True
    h=randrange(1,9)
  if y>10 or y<0:
    print(end="\033[0;12m\033[10;13HBat hit lava!")
    break
