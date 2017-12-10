#!/usr/bin/python

import json


def traverse(j, c):
  if type(j) == list:
    for o in j:
      c = traverse(o, c)
    return c
  if type(j) == dict:
    original = c
    for o, k in j.iteritems():
      if o == 'red' or k == 'red':
        return original
      c = traverse(o, c)
      c = traverse(k, c)
    return c
  if type(j) == unicode:
    return c
  if type(j) == int:
    return c + j
  raise Exception('Unknown type %s' % type(j))

def main():
  f = open('advent12')
  j = json.load(f)
  count = 0
  print 'Total sum is %d' % traverse(j, count)

if __name__ == '__main__':
  main()
