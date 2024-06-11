# Colors (C) 2024 by Mikael O. Bonnier, Lund, Sweden. License: GPLv3+.
# python3 colors_Cs.py
# snek colors_Cs.py
from atco_s import *

def prco(fg,bg):
  global i
  c=i
  if c==127:
    c=32
  print(end="%s%c"%(co(fg,bg),c))
  i+=1
  if i>127:
    i=32

print(end="%s%s"%(co(0,7),cls()))
i=32
for bg in range(0,16):
  for fg in range(0,16):
    prco(fg,bg)
  if bg%2: print()
while True:
  a=input("%s%sEsc code? \\033%s"%(co(0,7),at(8,0),cll()))
  if a=="-1":
    break
  print(end="%sX\x1B%s"%(at(5,24),a))
