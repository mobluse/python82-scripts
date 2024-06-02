# Not by me and doesn't work now, but worked with an earlier version of the Python82 App
from sys import *

def getkey():
  s=stdin.read(1)
  if s=="\033":
    s=stdin.read(3)
  return s
