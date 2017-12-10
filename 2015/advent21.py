#!/usr/bin/python


class Item(object):
  def __init__(self, cost, damage, defense):
    self.cost = cost
    self.damage = damage
    self.defense = defense

  def __repr__(self):
    return '%s: damage: %d, defense: %d, cost: %d' % (
        self.__class__.__name__, self.damage, self.defense, self.cost)

class Weapon(Item):
  def __init__(self, cost, damage):
    super(Weapon, self).__init__(cost, damage, 0)

class Armor(Item):
  def __init__(self, cost, defense):
    super(Armor, self).__init__(cost, 0, defense)

class Ring(Item):
  def __init__(self, cost, damage, defense):
    super(Ring, self).__init__(cost, damage, defense)

class Character(object):
  def __init__(self, damage, defense, hitpoints):
    self.damage = damage
    self.defense = defense
    self.hitpoints = hitpoints

  def __repr__(self):
    return '%s %s %s' % (self.damage, self.defense, self.hitpoints)


def fight(you, boss):
  attacker = you
  defender = boss

  while you.hitpoints > 0 and boss.hitpoints > 0:
    defender.hitpoints -= max((attacker.damage - defender.defense), 1)

    tmp = attacker
    attacker = defender
    defender = tmp
  if you.hitpoints <= 0 and boss.hitpoints > 0:
    return False
  if you.hitpoints > 0 and boss.hitpoints <= 0:
    return True
  raise Exception('you at %d boss at %d' % (you.hitpoints, boss.hitpoints))

def main():
  weapons = []
  rings = []
  armors = []
  weapons.append(Weapon(8, 4))
  weapons.append(Weapon(10, 5))
  weapons.append(Weapon(25, 6))
  weapons.append(Weapon(40, 7))
  weapons.append(Weapon(74, 8))

  rings.append(Ring(25, 1, 0))
  rings.append(Ring(50, 2, 0))
  rings.append(Ring(100, 3, 0))
  rings.append(Ring(20, 0, 1))
  rings.append(Ring(40, 0, 2))
  rings.append(Ring(80, 0, 3))

  armors.append(Armor(0, 0))
  armors.append(Armor(13, 1))
  armors.append(Armor(31, 2))
  armors.append(Armor(53, 3))
  armors.append(Armor(75, 4))
  armors.append(Armor(102, 5))

  rings_combinations = []

  # Build all rings combinations
  rings_combinations.append([])  # no rings
  for r in rings:  # one ring
    rings_combinations.append([r])

  for left in rings:
    for right in rings:
      if left != right:
        rings_combinations.append([left, right])

  min_gold = -1
  max_gold = 0
  # Try all combasts
  for w in weapons:
    for a in armors:
      for equipped_rings in rings_combinations:
        you = None
        gold = 0

        you = Character(w.damage, a.defense, 100)
        boss = Character(9, 2, 103)
        gold += w.cost + a.cost

        for r in equipped_rings:
          you.damage += r.damage
          you.defense += r.defense
          gold += r.cost

        if min_gold < 0 or gold < min_gold:
          if fight(you, boss):
            print 'Win'
            print w
            print a
            print equipped_rings
            min_gold = gold

        if gold > max_gold:
          if not fight(you, boss):
            print 'Die'
            print w
            print a
            print equipped_rings
            max_gold = gold

  print 'Min gold %d' % min_gold
  print 'Max gold %d' % max_gold

  return

if __name__ == '__main__':
  main()
