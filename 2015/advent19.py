#!/usr/bin/python

import random

class Machine(object):
  def __init__(self):
    self.molecules = {}
    self.medicine = ''
    self.all_repl = set()

  def boot(self, i):
    for line in i:
      line = line.strip()
      if not line:
        continue
      if not '=>' in line:
        self.medicine = line
        print self.medicine
        continue
      name, repl = line.split(' => ')
      mol = self.molecules.get(name)
      if not mol:
        mol = Molecule(name)
        self.molecules[name] = mol
      mol.replacements.append(repl)
    print self.molecules
    print '-------------- Boot completed ---------------'

  def replace_one(self, molecule, start):
    used = set()
    for i, _ in enumerate(start):
      pre = start[:max(0, i)]
      post = start[i+len(molecule.name):]

      part = start[i:i+len(molecule.name)]
      if part == molecule.name:
        assert len(pre) + len(part) + len(post) == len(start)
        for r in molecule.replacements:
          used.add(''.join([pre, r, post]))
          self.all_repl |= used
    return used


  def calibrate(self):
    for m in self.molecules.values():
      self.replace_one(m, self.medicine)
    return self.all_repl

  def build(self, start):
    all_repl = []

    for m in self.molecules.values():
      for r in m.replacements:
        all_repl.append((r, m.name))

    total = 0
    while self.medicine != 'e':
      replaced = False
      random.shuffle(all_repl)
      for l, r in all_repl:
        if l in self.medicine:
          replaced = True
          print self.medicine
          self.medicine = self.medicine.replace(l, r, 1)
          total += 1
      if not replaced:
        raise Exception
    return total



class Molecule(object):
  def __init__(self, name):
    self.name = name
    self.replacements = []

  def __repr__(self):
    return '%s: %s' % (self.name, self.replacements)

  def __cmp__(self, other):
    return cmp(self.name, other.name)


def main():
  i = open('advent19')
  m = Machine()
  m.boot(i)
  print 'All repl: %d ' % len(m.calibrate())
  print '--------------- Calibration finished ----------------'
  print 'Min steps: %d ' % m.build('e')

    


if __name__ == '__main__':
  main()
