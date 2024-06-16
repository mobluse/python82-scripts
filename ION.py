# Not by me and doesn't work now, but worked with an earlier version of the Python82 App
# Found on Jun 17 2024 https://tiplanet.org/forum/viewtopic.php?f=41&t=24977
from sys import *

def getkey():
  s=stdin.read(1)
  if s=="\033":
    s=stdin.read(3)
  return s
