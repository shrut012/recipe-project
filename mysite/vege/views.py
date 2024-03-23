from django.shortcuts import render


def recipes(request):
    return render(request, 'recipes.html')
