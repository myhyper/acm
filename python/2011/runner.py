import sys
import os
import random

while True:
  i = random.randint(1,12)
  st = ""
  for j in range(i):
    r = random.randint(0,9)
    st += str(r)
  #print(st)

  open('i.txt', 'w').write(st)
  a = os.popen("python3 ./sixth.py").read()
  b = os.popen("python3 ./gs.py").read()
  if a != b:
    print(st)
    print('my answer was =>', a, '<=')
    print('correct answer was =>', b, '<=')
    break