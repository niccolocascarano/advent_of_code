#!/usr/bin/python

import copy
import time

lights = []

def show(l):
  count = 0
  for x in range(100):
    line = []
    for y in range(100):
      count += l[x][y]
      if not l[x][y]:
        line.append('.')
      else:
        line.append('#')
    print ''.join(line)

  print
  return count



def count_on(cur, x, y):
  count = 0
  for xx in range(x-1, x+2):
    for yy in range(y-1, y+2):
      if xx == x and yy == y:
        continue
      if xx < 0 or xx >= len(lights[0]) or yy < 0 or yy >= len(lights[0]):
        continue
      count += cur[xx][yy]

  return count


def life(stuck):
  for i in range(100):
    if stuck:
      lights[0][0] = 1
      lights[0][99] = 1
      lights[99][99] = 1
      lights[99][0] = 1

    cur = copy.deepcopy(lights)
    show(cur)
    for x in range(100):
      for y in range(100):
        count = count_on(cur, x, y)
        if lights[x][y] == 1 and count != 2 and count != 3:
          lights[x][y] = 0
        if lights[x][y] == 0 and count == 3:
          lights[x][y] = 1

  if stuck:
    lights[0][0] = 1
    lights[0][99] = 1
    lights[99][99] = 1
    lights[99][0] = 1

def init():
  del lights[:]
  for i in range(100):
    lights.append([])
    for k in range(100):
      lights[i].append(0)

  i = open('advent18')
  x = 0
  for line in i:
    y = 0
    line = line.strip()
    for c in line:
      if c == '#':
        lights[x][y] = 1
      y += 1
    x += 1

def main():
  init()
  life(False)

  print 'Total on is %d' % show(lights)
  time.sleep(2)
        
  init()
  life(True)

  print 'Total on is %d' % show(lights)


if __name__ == '__main__':
  main()
