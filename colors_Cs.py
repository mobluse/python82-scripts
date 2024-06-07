# python3 colors_Cs.py
# snek colors_Cs.py
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
