#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    # batches = 0
    # go=True
    # while go:
    #   go = False
    #   for k, v in ingredients.items():
    #     if ingredients[k] > recipe[k]: 
    #       ingredients[k] = ingredients[k] - recipe[k]
    #       batches += 1
    #       go = True
    batches = 0
    arr = []

    for k ,v in recipe.items():
      if len(ingredients) != len(recipe) or recipe[k] > ingredients[k]:
        return batches
      else:
        josh = ingredients[k] // recipe[k]
        arr.append(josh)
      batches = min(arr)

    return batches


  

# takes input of recipe and ingredients objects/dictonary

# one object will contain the recipe with the needed amounts of the ingredients

# one object will contain the current available amounts of the needed ingredients

# we needd to compare the current availble amounts of ingredients against the desired amounts
# to see how many batches can be produced

# use a while loop?

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))