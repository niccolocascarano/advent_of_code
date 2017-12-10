#!/usr/bin/python

class Sue(object):
  def __init__(self, num):
    self.num = num
    self.features = {}

  def __repr__(self):
    return '%d: %s' % (self.num, self.features)

  def match(self, features):
    for k, v in self.features.iteritems():
      if features[k] != v:
        return False
    return True

  def match2(self, features):
    for k, v in self.features.iteritems():
      if k == 'cats' or k == 'trees':
        if v <= features[k]:
          return False
      elif k == 'pomeranians' or k == 'goldfish':
        if v >= features[k]:
          return False
      elif features[k] != v:
        return False
    return True


def read_input(i):
  sues = []
  for line in i:
    line = line.strip()
    line = line.replace(', ', ': ')
    line = line.replace('Sue ', '')
    parts = line.split(': ')
    s = Sue(int(parts[0]))
    sues.append(s)

    parts = parts[1:]
    idx = 0
    while idx < len(parts):
      s.features[parts[idx]] = int(parts[idx+1])
      idx += 2

  return sues

def main():
  i = open('advent16')
  sues = read_input(i)
      
  features = {
      'children': 3,
      'cats': 7,
      'samoyeds': 2,
      'pomeranians': 3,
      'akitas': 0,
      'vizslas': 0,
      'goldfish': 5,
      'trees': 3,
      'cars': 2,
      'perfumes': 1,
      }

  for s in sues:
    if s.match(features):
      print 'Sue %d matches' % s.num
    if s.match2(features):
      print 'Sue %d matches corrected' % s.num


if __name__ == '__main__':
  main()
