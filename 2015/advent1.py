#!/usr/bin/python

f = open('input')
input = f.read()

final_floor = 0
pos = 1
for c in input:
  if c == '(':
    final_floor+=1
  if c == ')':
    final_floor-=1
  if final_floor == -1:
    print 'entered basement at %d' % pos
  pos+=1

print 'final floor %d' % final_floor
