from django.http import HttpResponse
from django.shortcuts import render, Http404


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def recipe_view(request, dish_name):
    # Finding the recipe
    recipe = DATA.get(dish_name)
    if recipe is None:
        raise Http404 (f"Рецепт «{dish_name}» не найден")
    
     # Read servings, default 1
    servings_str = request.GET.get('servings', '1')
    try:
        servings = int(servings_str)
        if servings < 1:
            servings = 1
    except ValueError:
        servings = 1

     # Multiply each quantity by servings
    scaled_recipe = {}
    for ingredient, qty in recipe.items():
        scaled_recipe[ingredient] = qty * servings

     # Generate the context and render the template
    context = {
        'recipe': scaled_recipe
    }
    return render(request, 'calculator/index.html', context)


