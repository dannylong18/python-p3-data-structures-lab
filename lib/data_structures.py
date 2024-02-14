spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]
names = []

def get_names(spicy_foods):
    for dict in spicy_foods:
         names.append(dict['name'])
    return names

def get_spiciest_foods(spicy_foods):
    return [dict for dict in spicy_foods if dict['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    for dict in spicy_foods:
        strings = dict['name'] + " ("+ dict['cuisine'] + ") | Heat Level: " + "🌶" * dict['heat_level']
        print (strings)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for dict in spicy_foods:
        if cuisine == dict['cuisine']:
            return dict 

def print_spiciest_foods(spicy_foods):
    for dict in spicy_foods:
        if dict['heat_level'] > 5:
            strings = dict['name'] + " ("+ dict['cuisine'] + ") | Heat Level: " + "🌶" * dict['heat_level']
            print (strings)

def get_average_heat_level(spicy_foods):
    total = sum(food['heat_level'] for food in spicy_foods)
    return total / len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
