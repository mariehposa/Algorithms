#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = [0] * len(recipe)
  i = 0

  for (key, value) in recipe.items():
    print(f"{key} : {value}")
    for i in recipe["value"]:
      batches[i] = ingredients.value[i] / recipe.value[i]
      i = i + 1
    for i in batches:
      if batches[i] > 0:
        batches = math.ceil(batches[0])
      else:
        batches = 0

  return batches   

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))