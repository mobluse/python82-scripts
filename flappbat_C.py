# Flappy Bat (C) 2024 by Mikael O. Bonnier, Lund, Sweden. License: GPLv3+.
# Run using:  python3 flappbat_C.py
import time
import random
import curses
from curses import wrapper

fgco=[30,91,32,93,94,95,96,97,92,37,90,31,33,35,34,36]
bgco=fgco[:]
for i in range(len(bgco)):
  bgco[i]+=10

def at(r,c):
  return "\x1B[%d;%dH"%(r+1,c+1)

def co(fg,bg):
  return "\x1B[%d;%dm"%(fgco[fg],bgco[bg])

def cls():
  return at(0,0)+"\x1B[2J"

def cll():
  return "\x1B[K"

def main(stdscr):
  curses.curs_set(False)
  stdscr.nodelay(False)
  curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
  #curses.color_pair(1) | curses.A_BOLD | curses.REVERSE
  curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
  curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_YELLOW)
  stdscr.addstr(0,0,"%s%s",curses.color_pair(1))
  stdscr.addstr(0,0,"Flappy Bat",curses.color_pair(1))
  stdscr.addstr(0,6,"~",curses.color_pair(2))
  stdscr.addstr(0,10,"~"*(22),curses.color_pair(2))
  stdscr.addstr(1,0," "*(9*32),curses.color_pair(1))
  stdscr.addstr(10,0," "*32,curses.color_pair(3))
  stdscr.addstr(0,0,"",curses.color_pair(1))
  y=9
  x1=31
  m=True
  p=0
  t=time.monotonic()
  h=random.randrange(8)+1
  s1="r=%d  c=%d h=%d moths=%d "
  s2=" Bat hit lava! "
  while True:
    stdscr.addstr(int(y),6,"Y")
    if m:
      stdscr.addstr(h,int(x1),"<")
    stdscr.refresh()
    time.sleep(.3)
    if m:
      stdscr.addstr(h,int(x1)," ")
    stdscr.addstr(int(y),6," ")
    stdscr.addstr(9,0,s1%(int(10*y),int(10*x1),int(10*h),p))
    stdscr.refresh()
    a=stdscr.getch()
    ts=t
    t=time.monotonic()
    dt=(t-ts)
    y-=1-1.5*dt
    x1-=dt
    if m and int(x1)==6 and int(y)==h:
      m=False
      p+=1
    if x1<0:
      x1=31
      m=True
      h=random.randrange(8)+1
    if y>10 or y<0:
      stdscr.addstr(10,12,s2,curses.color_pair(3)|curses.A_BOLD)
      stdscr.refresh()
      break
  stdscr.getch()
  curses.curs_set(True)
  curses.endwin()
  print()
  print(s1%(int(10*y),int(10*x1),int(10*h),p))
  print("%s%s"%(co(7,12),s2))

wrapper(main)
