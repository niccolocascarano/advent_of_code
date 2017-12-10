#!/usr/bin/python

input = open('input2')

total_paper = 0
total_ribbon = 0
for pack in input:
  a,b,c = pack.strip().split('x')
  h = int(a)
  w = int(b)
  l = int(c)
  side1 = h*w
  side2 = h*l
  side3 = w*l 
  p1 = 2*(h+w)
  p2 = 2*(h+l)
  p3 = 2*(w+l)
  total_ribbon += min(p1, p2, p3) + h*w*l
  total_paper += side1*2 + side2*2 + side3*2 + min(side1, side2, side3)

print 'Total paper %d' % total_paper
print 'Total ribbon %d' % total_ribbon
