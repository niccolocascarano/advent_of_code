#!/usr/bin/python

import random

class Spell(object):
  def __init__(self, cost, timer, damage, defense, recharge, heal):
    self.cost = cost
    self.timer = timer
    self.damage = damage
    self.defense = defense
    self.recharge = recharge
    self.heal = heal
    self.name = self.__class__.__name__

  def __repr__(self):
    return '%s: %d. Timer: %d' % (self.__class__.__name__, self.cost,
        self.timer)

  def __hash__(self):
    return hash(self.__class__.__name__)

  def __cmp__(self, other):
    return cmp(self.__class__.__name__, other.__class__.__name__)


class MagicMissile(Spell):
  def __init__(self):
    super(MagicMissile, self).__init__(53, 0, 4, 0, 0, 0)

class Drain(Spell):
  def __init__(self):
    super(Drain, self).__init__(73, 0, 2, 0, 0, 2)

class Shield(Spell):
  def __init__(self):
    super(Shield, self).__init__(113, 6, 0, 7, 0, 0)

class Poison(Spell):
  def __init__(self):
    super(Poison, self).__init__(173, 6, 3, 0, 0, 0)

class Recharge(Spell):
  def __init__(self):
    super(Recharge, self).__init__(229, 5, 0, 0, 101, 0)

class Character(object):
  def __init__(self, name, hp, mana, damage):
    self.name = name
    self.hp = hp
    self.mana = mana
    self.damage = damage
    self.defense = 0

  def __repr__(self):
    return '%s: hp: %d def: %d mana: %d ' % (self.name, self.hp, self.defense,
        self.mana)


class Fight(object):
  def __init__(self, you, boss, seq, min_mana, hard):
    self.you = you
    self.boss = boss
    self.attacker = you
    self.defender = boss
    self.seq = seq
    self.active_effects = set()
    self.used_mana = 0
    self.min_mana = min_mana
    self.hard = hard
    self.spells = [
        MagicMissile,
        Drain,
        Shield,
        Poison,
        Recharge,
        ]
    self.events = []

  def swap(self):
    tmp = self.attacker
    self.attacker = self.defender
    self.defender = tmp

  def check_winner(self):
    if self.boss.hp <= 0:
      return self.you
    if self.you.hp <= 0:
      return self.boss
    return None

  def launch_spell(self):
    while self.seq:
      num = self.seq.pop(0)
      spell = self.spells[num]()
      if spell in self.active_effects:
        continue
      if self.you.mana < spell.cost:
        continue

      self.events.append('Launch %s' % spell)
      self.you.mana -= spell.cost
      self.used_mana += spell.cost
      if self.used_mana > self.min_mana and self.min_mana > 0:
        return False
      if spell.timer:
        self.active_effects.add(spell)
        return True
      self.boss.hp -= spell.damage
      self.you.hp += spell.heal
      return True
    return False

  def do_round(self):
    self.events.append('Attacker %s' % self.attacker.name)

    if self.hard and self.attacker.name == 'you':
      self.you.hp -= 1
      if self.check_winner():
        return False

    for s in self.active_effects:
      s.timer -= 1
      self.events.append('Active %s' % s)
      self.boss.hp -= s.damage
      self.you.mana += s.recharge
      if s.name == 'Shield':
        self.you.defense = s.defense

    for s in self.active_effects.copy():
      if not s.timer:
        self.active_effects.remove(s)
        if s.name == 'Shield':
          self.you.defense = 0

    if self.check_winner():
      return False

    if self.attacker.damage > 0:
      self.defender.hp -= max(1, self.attacker.damage - self.defender.defense)
    else:
      if not self.launch_spell():
        self.you.hp = 0

    self.swap()

    self.events.append(str(self.you))
    self.events.append(str(self.boss))
    self.events.append('Total mana %d\n' % self.used_mana)

    if self.check_winner():
      return False

    return True

num_spells = 5

def make_seq(max_len):
  last = []
  final = []
  for i in range(max_len):
    last.append(0)

  for i in range(max_len):
    final.append(num_spells - 1)

  while last != final:
    carry = 1
    pos = 0
    while carry:
      last[pos] += 1
      carry = 0
      if last[pos] == num_spells:
        last[pos] = 0
        carry = 1
      pos += 1
    yield list(last)


def main():

  min_mana = -1

  for seq in make_seq(10):  # I bet it will take less than 10 rounds to win
    you = Character('you', 50, 500, -1)
    boss = Character('boss', 55, -1, 8)
    f = Fight(you, boss, list(seq), min_mana, True)
    while f.do_round():
      pass

    if f.check_winner().name == 'you' and (
        min_mana < 0 or f.used_mana <= min_mana):
      min_mana = f.used_mana
      print '\n'.join(f.events)
      print 'Min mana %d' % min_mana
      print 'Sequence was %s' % seq
      print '------------------------'

if __name__ == '__main__':
  main()

