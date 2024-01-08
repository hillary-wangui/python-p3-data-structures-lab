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

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    return([food for food in spicy_foods if food.get("heat_level", 0) > 5])
    
print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get("name")
        cuisine = food.get("cuisine")
        heat_level = food.get("heat_level")
        emoji = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {emoji}")

print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if (food.get("cuisine").lower() == cuisine.lower()):
            return food
    
print(get_spicy_food_by_cuisine(spicy_foods, "thai"))

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name=food.get("name")
        cuisine=food.get("cuisine")
        heat_level=food.get("heat_level")
        emoji= "🌶" * heat_level
        if(food.get("heat_level") > 5):
            print(f"{name} ({cuisine}) | Heat Level: {emoji}")

print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food.get("heat_level", 0) for food in spicy_foods)
    number_spice = len(spicy_foods)
    if number_spice == 0:
        return 0
    else:
        return total_heat_level // number_spice

print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_food_copy = spicy_foods.copy()
    spicy_food_copy.append(spicy_food)
    return spicy_food_copy

new_food= {'name': 'Griot','cuisine': 'Haitian','heat_level': 10,}

print(create_spicy_food(spicy_foods, new_food))

