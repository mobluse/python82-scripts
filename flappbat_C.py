# Flappy Bat (C) 2024 by Mikael O. Bonnier, Lund, Sweden. License: GPLv3+.
# Run using: python3 flappbat_C.py
import time
import random
import curses
from curses import wrapper
from atco_s import *

def main(stdscr):
  curses.curs_set(False)
  stdscr.nodelay(False)
  curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
  # Example: curses.color_pair(1) | curses.A_BOLD | curses.REVERSE
  curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
  curses.init_pair(3,curses.COLOR_BLACK,curses.COLOR_YELLOW)
  stdscr.addstr(0,0,"Flappy Bat",curses.color_pair(1))
  stdscr.addstr(0,6,"~",curses.color_pair(2))
  stdscr.addstr(0,10,"~"*(22),curses.color_pair(2))
#  stdscr.addstr(1,0," "*(9*32),curses.color_pair(1))
  stdscr.addstr(10,0," "*32,curses.color_pair(3))
  stdscr.addstr(0,0,"",curses.color_pair(1))
  y=9
  x1=31
  m=True
  p=0
  t=time.monotonic()
  random.seed(t)
  h=random.randrange(8)+1
  tot=0
  s1="r=%d  c=%d h=%d moths=%d/%d "
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
    stdscr.addstr(9,0,s1%(int(10*y),int(10*x1),int(10*h),p,tot))
    stdscr.refresh()
    while stdscr.getch()!=10:
      pass
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
      tot+=1
    if y>10 or y<0:
      stdscr.addstr(10,12,s2,curses.color_pair(3))
      stdscr.refresh()
      break
  stdscr.getch()
  curses.curs_set(True)
  curses.endwin()
  print()
  print(s1%(int(10*y),int(10*x1),int(10*h),p,tot))
  print(co(0,12)+s2+co(9,0))

wrapper(main)
