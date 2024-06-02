from sys import *

def getkey():
  s=stdin.read(1)
  if s=="\033":
    s=stdin.read(3)
  return s