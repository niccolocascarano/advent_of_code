#!/usr/bin/python

def inc_str(s):
  sr = list(s[::-1])
  final = []
  carry = 1
  i = 0

  while carry > 0 and i < len(sr):
    c = ord(sr[i]) + carry
    carry = 0
    if c > ord('z'):
      carry = 1
      c = ord('a')
    sr[i] = chr(c)
    i += 1

  if carry > 0:
    sr.append('a')
  sr = ''.join(sr[::-1])

  return sr


def consecutive(s):
  prev = '_'
  count = 1
  for c in s:
    if ord(c) == ord(prev) + 1:
      count+=1
    else:
      count = 1
    if count == 3:
      return True
    prev = c
  return False

def ban(s):
  for c in ['iol']:
    if c in s:
      return False
  return True

def pair(s):
  prev = '.'
  count = 0
  for c in s:
    if c == prev:
      count += 1
      prev = '.'
    else:
      prev = c
    if count == 2:
      return True
  return False


def check(s):
  if not consecutive(s):
    return False
  if not ban(s):
    return False
  if not pair(s):
    return False
  return True

def main():
  s = 'hepxcrrq'
  count = 0
  while count < 2:
    s = inc_str(s)
    if check(s):
      print 'New pwd: %s' % s
      count += 1


if __name__ == '__main__':
  main()
