#!/usr/bin/python

divisions = 2
spaces = 4  # it is 3 for part 1

def give_combination(packets):
  total = 0
  groups = {}
  final_groups = {}
  weights = {1: 0, 2: 0}

  for p in packets:
    total += p
    groups[p] = 1
    weights[1] += p
    final_groups[p] = divisions

  total /= spaces
  min_packets = 0
  no_more_than = len(packets)/spaces
  print 'Even is %d' % total

  while groups != final_groups:
    for k, v in sorted(groups.iteritems()):
      if v == divisions:
        min_packets -= 1
      if v == 1:
        min_packets += 1

      weights[v] -= k
      groups[k] += 1
      if groups[k] == divisions + 1:
        groups[k] = 1
        weights[groups[k]] += k
      else:
        weights[groups[k]] += k
        break
    if min_packets > no_more_than:
      continue
    if weights[divisions] != total:
      continue
    if min_packets < no_more_than:
      no_more_than = min_packets
    yield dict(groups)


def main():
  packets = []
  i = open('advent24')
  for line in i:
    line = line.strip()
    packets.append(int(line))

  valid = []
  min_packet = -1
  min_qe = 0
  for g in give_combination(packets):
    count = 0
    qe = 1
    weight = 0
    packets = []
    for k, v in g.iteritems():
      if v == divisions:
        count += 1
        weight += k
        qe *= k
        packets.append(k)
    if count == min_packet and qe < min_qe:
      min_qe = qe
      print 'New min %d QE: %d, weight: %d - %s' % (min_packet, qe, weight,
          sorted(packets))
    if min_packet < 0 or count < min_packet:
      min_packet = count
      min_qe = qe
      print 'New min %d QE: %d, weight: %d - %s' % (min_packet, qe, weight,
          sorted(packets))


if __name__ == '__main__':
  main()
