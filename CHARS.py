# Chars (C) 2024 by Mikael O. Bonnier, Lund, Sweden. License: GPLv3+.
def c(i,n=0):
  if n==0:
    return chr(i)
  else:
    return "%c"%i
nUb={3,8,9,10,13,14,15,20,23,25,27,28,29,30}
b={20,28,29}
n=nUb-b
for i in sorted(list(n)):
  print(i,"[%s]"%c(i))
for i in range(32):
  print(i//10,end="")
for i in range(32):
  print(i%10,end="")
def pc(j):
  for i in range(256):
    if i in n:
      print(end="n")
    elif i in b:
      print(end="b")
    else:
      print(end=c(i,j))
pc(0)
#pc(1)
