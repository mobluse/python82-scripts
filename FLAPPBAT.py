# Flappy Bat (C) 2024 by Mikael O. Bonnier, Lund, Sweden. License: GPLv3+.
from time import *
from random import *

def co(fg,bg):
  return "\x1B[%d;%dm"%(fg,bg)

def at(r,c):
  return "\x1B[%d;%dH"%(r,c)

def cls():
  return "\x1B[2J"

def cll():
  return "\x1B[K"

print("%sFlappy%s~%sBat%s"%(co(8,0),co(12,0),co(8,0),co(12,0)),end="~"*(22))
print(end=" "*(9*32))
print(co(8,12),end=" "*32)
print(end=co(8,0))
y=9
x1=31
m=True
p=0
t=monotonic()
seed(t)
h=randrange(1,9)
tot=0
while True:
  print(end="%sY"%at(int(y),6))
  if m:
    print(end=at(h,int(x1))+chr(130))
  sleep(.3)
  if m:
    print(end="\b ")
  a=input("%s %sr=%d  c=%d h=%d moths=%d/%d "%(at(int(y),6),at(9,0),int(10*y),int(10*x1),int(10*h),p,tot))
  ts=t
  t=monotonic()
  dt=(t-ts)
  y-=1-1.5*dt
  x1-=dt
  if m and int(x1)==6 and int(y)==h:
    m=False
    p+=1
  if x1<0:
    x1=31
    m=True
    h=randrange(1,9)
    tot+=1
  if y>10 or y<0:
    print(end="%s%sBat hit lava!"%(co(0,12),at(10,13)))
    break
