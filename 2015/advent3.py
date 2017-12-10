#!/usr/bin/python

file = open('input3')
houses = set()
houses2 = set()

houses.add((0,0))
houses2.add((0,0))
x = 0
xx = [0, 0]
y = 0
yy = [0, 0]
count = 0

for m in file.read():
  if m == 'v':
    y-=1
    yy[count%2]-=1
  if m == '^':
    y+=1
    yy[count%2]+=1
  if m == '<':
    x-=1
    xx[count%2]-=1
  if m== '>':
    x+=1
    xx[count%2]+=1

  houses.add((x,y))
  houses2.add((xx[count%2], yy[count%2]))
  count += 1

print 'Total houses: %d' % len(houses)
print 'Total houses2: %d' % len(houses2)
