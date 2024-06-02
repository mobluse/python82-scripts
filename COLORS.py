print("\033[0;H",end="")
i=32
for bg in range(16):
  for fg in range(16):
    print("\033[%d;%dm%c"%(fg,bg,i),end="")
    i+=1
    if i>127:
      i=32
a=""
while True:
  a=input("\033[m\033[8;HEsc code? \\033\033[K")
  if a=="-1":
    break
  print("\033[5;24HX\033%s"%a,end="")