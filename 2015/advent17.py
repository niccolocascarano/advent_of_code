#!/usr/bin/python

containers = {
    1: 33, 2: 14, 3: 18, 4: 20, 5: 45, 6: 35, 7: 16, 8: 35,
    9: 1, 10: 13, 11: 18, 12: 13, 13: 50, 14: 44, 15: 48, 16: 6, 17: 24,
    18: 41, 19: 30, 20: 42
    }

class Fridge(object):
  def __init__(self):
    self.containers = []
    self.solution = {}
    self.solutions = set()
    self.actual_solutions = []
    self.total = 0
    for c in sorted(containers.keys()):
      self.solution[c] = 0

  def pick(self, start, max_value):
    for k, c in containers.copy().iteritems():
      if k < start:
        continue
      del containers[k]
      self.total += c
      self.solution[k] += 1
      if self.total < max_value:
        self.pick(k, max_value)
      elif self.total == max_value:
        sol = sorted((v,k) for v,k in self.solution.iteritems())
        if str(sol) not in self.solutions:
          print 'Solution %s' % sol
          self.solutions.add(str(sol))
          self.actual_solutions.append(sol)

      self.total -= c
      self.solution[k] -= 1
      containers[k] = c

    return self.actual_solutions



def main():
  f = Fridge()
  total = f.pick(0, 150)
  print 'Total combo %d' % len(total)

  min_used = len(containers)
  min_count = 1
  for s in total:
    count = 0
    for _, v in s:
      count += v

    if count < min_used:
      print 'min is %d' % count
      min_used = count
      min_count = 1
    elif count == min_used:
      min_count += 1

  print 'Min combo %d' % min_count



if __name__ == '__main__':
  main()
