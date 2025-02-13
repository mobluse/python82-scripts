# Flappy Bat (C) 2024 by Mikael O. Bonnier, Lund, Sweden. License: GPLv3+.
# Run using Snek version > 1.9: snek flappbat_s.py
from time import *
from random import *

fgco=[30,91,32,93,94,95,96,97,92,37,90,31,33,35,34,36]
bgco=fgco[:]
for i in range(len(bgco)):
  bgco[i]+=10

def co(fg,bg):
  return "\x1B[%d;%dm"%(fgco[fg],bgco[bg])

def at(r,c):
  return "\x1B[%d;%dH"%(r+1,c+1)

def cls():
  return at(0,0)+"\x1B[2J"

def cll():
  return "\x1B[K"

def shcu(on):
  if on:
    return "\x1B[?25h"
  else:
    return "\x1B[?25l"

print(end=shcu(False))
print(end=co(8,0)+cls())
print("%sFlappy%s~%sBat%s"%(co(8,0),co(12,0),co(8,0),co(12,0)),end="~"*(22))
#print(end=" "*(9*32))
print(co(8,12)+at(10,0),end=" "*32)
print(end=co(8,0))
y=9
x1=31
m=True
p=0
t=monotonic()
seed(t)
h=randrange(8)+1
tot=0
while True:
  print(end=at(int(y),6)+"Y")
  if m:
    print(end=at(h,int(x1))+"<")
  stdscr.refresh()
  sleep(.3)
  if m:
    print(end=at(h,int(x1))+" ")
  stdscr.refresh()
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
    h=randrange(8)+1
    tot+=1
  if y>10 or y<0:
    print(end="%s%sBat hit lava! "%(co(0,12),at(10,13)))
    break
print(end=shcu(True))
