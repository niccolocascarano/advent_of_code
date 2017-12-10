#!/usr/bin/python

new = 33511524
row = 1
col = 6
size = 6

while row != 3010 or col != 3019:
  number = new
  new = (number * 252533) % 33554393

  if col == size:
    size += 1
    row = col + 1
    col = 1
  else:
    col += 1
    row -= 1

  if col == row:
    print '%d (%d, %d)' % (new, row, col)

print '%d (%d, %d)' % (new, row, col)
