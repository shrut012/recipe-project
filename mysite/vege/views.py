from django.shortcuts import render, redirect
from .models import Recipe


def add_recipe(request):
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')
        # print("Recipe Name:", recipe_name)
        # print("Recipe Description:", recipe_description)
        # print("Recipe Image:", recipe_image)

        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image
        )

        return redirect('/recipes')

    queryset = Recipe.objects.all()
    context = {'page': 'Add Recipe', 'recipes': queryset}
    return render(request, 'add_recipe.html', context)

def delete_recipe(request, id):
    print("called")
    queryset = Recipe.objects.get(id= id)
    queryset.delete()
    return redirect('/recipes')
