# Colors (C) 2024 by Mikael O. Bonnier, Lund, Sweden. License: GPLv3+.
print(end="\033[0;H")
i=32
for bg in range(16):
  for fg in range(16):
    print(end="\033[%d;%dm%c"%(fg,bg,i))
    i+=1
    if i>127:
      i=32
a=""
while True:
  a=input("\033[m\033[8;HEsc code? \\033\033[K")
  if a=="-1":
    break
  print(end="\033[5;24HX\033%s"%a)
