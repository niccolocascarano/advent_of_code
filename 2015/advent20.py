#!/usr/bin/python

import sys

target = 29000000
house = []
for i in range((target/10) + 1):
  house.append(0)

for elf in range(1, (target/10) + 1):
  for h in range(elf, (target/10) + 1, elf):
    house[h] += elf*10

for i in range(1, target/10):
  if house[i] >= target:
    print i
    break


# Second part
for i in range(target/10 + 1):
  house[i] = 0

for elf in range(1, target/10 + 1):
  for h in range(elf, min(elf*51, target/10 + 1), elf):
    house[h] += elf*11

for i in range(1, target/10):
  if house[i] >= target:
    print i
    break
