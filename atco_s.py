# AtCo (C) 2024 by Mikael O. Bonnier, Lund, Sweden. License: GPLv3+.
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
