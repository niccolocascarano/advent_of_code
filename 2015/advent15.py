#!/usr/bin/python

class Ingredient(object):
  def __init__(self, name, capacity, durability, flavor, texture, calories):
    self.name = name
    self.capacity = capacity
    self.durability = durability
    self.flavor = flavor
    self.texture = texture
    self.calories = calories

  def score(self, k):
    return (k*self.capacity, k*self.durability, k*self.flavor, k*self.texture,
        k*self.calories)

class Cook(object):
  def __init__(self):
    self.ingredients = []
    self.ingredients.append(Ingredient('Frosting', 4, -2, 0, 0, 5))
    self.ingredients.append(Ingredient('Candy', 0, 5, -1, 0, 8))
    self.ingredients.append(Ingredient('Butterscotch', -1, 0, 5, 0, 6))
    self.ingredients.append(Ingredient('Sugar', 0, 0, -2, 2, 1))
    self.score = 0
    self.score_with_calories = 0

  def get_all_permutations(self):
    used = set()
    for a in range(101):
      for b in range(101):
        for c in range(101):
          if a+b+c > 100:
            continue
          d = 100 - (a+b+c)
          used.add((a,b,c,d))
    return used


  def part_score(self, p):
    score = [0, 0, 0, 0, 0]
    for i in range(4):
      part = self.ingredients[i].score(p[i])
      for j in range(5):
        score[j] += part[j]
    return score

  def cook(self, calories=0):
    used = self.get_all_permutations()

    for k in sorted(used):
      score = self.part_score(k)

      total = 1
      for i in range(4):
        if score[i] < 0:
          total = 0
          break
        total *= score[i]

      if total > self.score:
        self.score = total

      if total > self.score_with_calories and score[4] == calories:
        self.score_with_calories = total
    return (self.score, self.score_with_calories)

def main():
  c = Cook()
  a, b = c.cook(500)
  print 'Max score is %d' % a
  print 'Max score with 500 calories is %d' % b

if __name__ == '__main__':
  main()
