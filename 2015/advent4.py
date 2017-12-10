#!/usr/bin/python

import md5

i = 1
sol1 = False
sol2 = False

while True:
  h = md5.new('ckczppom%d' % i)
  if h.hexdigest().startswith('00000') and not sol1:
    print '%d: %s' % (i, h.hexdigest())
    sol1 = True
  if h.hexdigest().startswith('000000') and not sol2:
    print '%d: %s' % (i, h.hexdigest())
    sol2 = True

  if sol1 and sol2:
    break
  i+=1

