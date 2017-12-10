#!/usr/bin/python

class Reindeer(object):
  def __init__(self, name, speed, time, rest):
    self.name = name
    self.speed = int(speed)
    self.time = int(time)
    self.rest = int(rest)
    self.distance = 0
    self.score = 0
    
    self.remaining_running = self.time
  
  def run_one_sec(self):
    if self.remaining_running == 0:
      print '%s resting at %d, %d' % (self.name, self.distance,
          self.remaining_rest)
      self.remaining_rest -= 1
      if self.remaining_rest == 0:
        self.remaining_running = self.time
      return

    self.distance += self.speed
    self.remaining_running -= 1
    if self.remaining_running == 0:
      self.remaining_rest = self.rest
    print '%s running at %d, still has %d' % (self.name, self.distance,
        self.remaining_running)

  def run(self, current_time, max_time):
    running_time = self.time
    if (current_time + self.time) > max_time:
      running_time = max_time - current_time
      print 'Too big %d, stopping after %d' % (max_time - current_time,
          running_time)
    if running_time < 0:
      return (current_time + self.rest, self)
    self.distance += (self.speed * running_time)
    print '%s arrived at %d after %d' % (self.name, self.distance,
        current_time + running_time)
    return (current_time + self.time + self.rest, self)

  def __repr__(self):
    return self.name
  
  def __cmp__(self, o):
    return cmp(self.name, o.name)

class Race(object):
  def __init__(self):
    self.reindeer = {}
    self.events = []

  def read_input(self, i):
    for line in i:
      parts = line.strip().split(' ')
      r = Reindeer(parts[0], parts[3], parts[6], parts[13])
      self.reindeer[r.name] = r
      print r

  def race(self, max_time):
    time = 0
    for r in self.reindeer.values():
      run_again = r.run(time, max_time)
      self.events.append(run_again)

    while True:
      self.events = sorted(self.events, key=lambda i: i[0])
      time = self.events[0][0]
      if time >= max_time:
        break
      print 'Time at %d' % time
      self.events.append(self.events[0][1].run(time, max_time))
      self.events.pop(0)

    arrivals = sorted(self.reindeer.values(),
        key=lambda r: r.distance, reverse=True)
    print 'Winner is %s: %s' % (arrivals[0].name, arrivals[0].distance)

  def score_race(self, max_time):
    time = 0
    while time < max_time:
      time += 1
      for r in self.reindeer.values():
        r.run_one_sec()

      arrivals = sorted(self.reindeer.values(),
          key=lambda r: r.distance, reverse=True)
      arrivals[0].score += 1
      i = 1
      while i < len(arrivals) and arrivals[i].distance == arrivals[0].distance:
        arrivals[i].score += 1
        i += 1
      print 'vvvvvvvvvvvvvvv'
      for a in arrivals:
        print '%s dist: %s score: %s' % (a, a.distance, a.score)
      print '^^^^^^^^^^^^^^^'

    arrivals = sorted(self.reindeer.values(),
        key=lambda r: r.score, reverse=True)
    print 'Winner on score is %s: %s' % (arrivals[0].name, arrivals[0].score)


def main():
  print 'Discrete race'
  i = open('advent14')
  r = Race()
  r.read_input(i)
  w = r.race(2503)
  print '-----------\n'

  print 'Score race'
  i = open('advent14')
  r = Race()
  r.read_input(i)
  w = r.score_race(2503)
  

if __name__ == '__main__':
  main()
