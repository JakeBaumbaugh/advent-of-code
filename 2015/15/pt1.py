import re

with open('input.txt', 'r') as file:
    lines = file.readlines()

ingredients = {}
for line in lines:
    match = re.search('(.+): capacity (-?\\d+), durability (-?\\d+), flavor (-?\\d+), texture (-?\\d+), calories (-?\\d+)', line)
    ingredients[match.group(1)] = {
        'capacity': int(match.group(2)),
        'durability': int(match.group(3)),
        'flavor': int(match.group(4)),
        'texture': int(match.group(5)),
        'calories': int(match.group(6))
    }
ingredient_order = [key for key in ingredients.keys()]

recipes = set()
recipes.add(tuple(0 for _ in range(len(ingredients))))
for recipe_size in range(100):
    print('generating recipe', recipe_size + 1)
    new_recipes = set()
    for recipe in recipes:
        for i in range(len(recipe)):
            new_recipe = tuple(recipe[j] + (1 if i == j else 0) for j in range(len(recipe)))
            new_recipes.add(new_recipe)
    recipes = new_recipes

def get_score(recipe):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    for index in range(len(recipe)):
        count = recipe[index]
        ingredient = ingredients[ingredient_order[index]]
        capacity += ingredient['capacity'] * count
        durability += ingredient['durability'] * count
        flavor += ingredient['flavor'] * count
        texture += ingredient['texture'] * count
    if capacity <= 0 or durability <= 0 or flavor <= 0 or texture <= 0:
        return 0
    return capacity * durability * flavor * texture

max_score = 0
for recipe in recipes:
    max_score = max(max_score, get_score(recipe))
print(max_score)