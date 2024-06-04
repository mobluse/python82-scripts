# Colors (C) 2024 by Mikael O. Bonnier, Lund, Sweden. License: GPLv3+.
def at(r,c):
  return "\x1B[%d;%dH"%(r,c)

def co(fg,bg):
  return "\x1B[%d;%dm"%(fg,bg)

def cls():
  return "\x1B[2J"

def cll():
  return "\x1B[K"

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
while True:
  a=input("%s%sEsc code? \\033%s"%(co(0,7),at(8,0),cll()))
  if a=="-1":
    break
  print(end="%sX\x1B%s"%(at(5,24),a))
