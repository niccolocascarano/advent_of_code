#!/usr/bin/python


class Person(object):
  def __init__(self, name):
    self.peers = {}
    self.name = name

  def __repr__(self):
    return self.name

  def __hash__(self):
    return self.name

  def __cmp__(self, o):
    return cmp(self.name, o.name)

class Table(object):
  def __init__(self):
    self.persons = {}
    self._max_happiness = 0
    self.used = []

  def read_persons(self, f):
    for line in f:
      line = line.strip().replace('.', '')
      parts = line.split(' ')
      p = self.persons.get(parts[0], Person(parts[0]))
      points = int(parts[3])
      if parts[2] == 'lose':
        points = -points
      p.peers[parts[10]] = points
      self.persons[parts[0]] = p
    for p in self.persons.values():
      print p

  def max_happiness(self):
    self.recursive_happiness(self.persons.values()[0], 0)
    return self._max_happiness

  def print_solution(self):
    print 'Solution %s' % self.used
    happiness = 0
    for idx, p in enumerate(self.used):
      happiness += p.peers[self.used[idx-1].name]
      happiness += p.peers[self.used[(idx+1) % len(self.used)].name]
      print '%s <- %s: %d' % (p.name, self.used[idx-1].name,
        p.peers[self.used[idx-1].name])
      print '%s -> %s: %d' % (p.name, self.used[(idx+1) % len(self.used)].name,
        p.peers[self.used[(idx+1) % len(self.used)].name])
    print 'Total %d' % happiness
    return happiness

  def close_table(self):
    happiness = self.print_solution()
    if happiness > self._max_happiness:
      self._max_happiness = happiness

  def recursive_happiness(self, p, happiness):
    self.used.append(p)
    all_used = True

    for peer, points in p.peers.iteritems():
      if self.persons[peer] in self.used:
        continue
      all_used = False
      self.recursive_happiness(self.persons[peer], happiness)

    if all_used:
      self.close_table()

    self.used.pop()


def main():
  f = open('advent13')
  t = Table()
  t.read_persons(f)
  print 'Max happiness %d' % t.max_happiness()

  f = open('advent13-2')
  t = Table()
  t.read_persons(f)
  print 'Max happiness %d' % t.max_happiness()


if __name__ == '__main__':
  main()
