#!/usr/bin/python

banned = ['ab', 'cd', 'pq', 'xy']
vowels = 'aeiou'
file = open("advent5")

good = 0
good2 = 0
for line in file:
	repeat = False
	for idx, _ in enumerate(line):
		if idx+2 >= len(line):
			break
		
		if line[idx] == line[idx+2]:
			repeat = True
			break
		

	otherRepeat = False
	for idx, _ in enumerate(line):
		if idx+1 >= len(line):
			break
		
		s = line[idx:idx+2]
		i = line.find(s)
		if i > 0:
			j = line.find(s, i+2)
			if j > 0:
				otherRepeat = True
		
	if repeat and otherRepeat:
		good2+=1
	if not repeat or not otherRepeat:
		print line.strip()

	bad = False
	for b in banned:
		if line.find(b) > 0:
			bad = True
			break
	if bad:
		continue

	prev = '_'
	double = False
	vc = 0
	for c in line:
		if c == prev:
			double = True
		if c in vowels:
			vc+=1
		prev = c

	if not double:
		continue

	if vc < 3:
		continue
	good+=1

print "Good strings: %d" % good
print "Good strings2: %d" % good2

