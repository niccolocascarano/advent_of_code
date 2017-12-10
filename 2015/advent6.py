#!/usr/bin/python

i = open('advent6')
lights = []
lights2 = []

for x in range(1000):
  lights.append([])
  lights2.append([])
  for y in range(1000):
    lights[x].append(False)
    lights2[x].append(0)

for line in i:
  cmd = -1
  if line.startswith('turn on '):
    line = line[len('turn on '):]
    cmd = 1
  if line.startswith('turn off '):
    line = line[len('turn off '):]
    cmd = 0
  if line.startswith('toggle '):
    line = line[len('toggle '):]
    cmd = 2
  if cmd == -1:
    raise 'Wrong input'

  start, end = line.split(' through ')
  xs, ys = start.split(',')
  xs = int(xs)
  ys = int(ys)
  xe, ye = end.split(',')
  xe = int(xe)
  ye = int(ye)

  for x in range(xs, xe+1):
    for y in range(ys, ye+1):
      if cmd == 2:
        lights[x][y] = not lights[x][y]
        lights2[x][y] += 2
      if cmd == 1:
        lights[x][y] = True
        lights2[x][y] += 1
      if cmd == 0:
        lights[x][y] = False
        lights2[x][y] -= 1
        if lights2[x][y] < 0:
          lights2[x][y] = 0

on = 0
bright = 0
for x in range(0, 1000):
  for y in range(0, 1000):
    if lights[x][y]:
      on += 1
    bright += lights2[x][y]

print "lights on: %d" % on
print "brightness: %d" % bright
          

