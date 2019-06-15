from django.shortcuts import render
from django.http import HttpResponse
from marmeladenladen.models import Ingredients
from django.views import generic
from django.views import View

class MyView(View):
    def get(self, request):
        frucht = 'Banana'
        fruit1 = Ingredients.object.filter(Name = frucht).values()[0]
        fruit2 = Ingredients.object.filter(Name = 'Apple').values()[0]
        fruit3 = Ingredients.object.filter(Name = 'Strawberry').values()[0]
        spice = Ingredients.object.filter(Name = 'Honey').values()[0]

        # Save the name of the fruit into a variable
        name_fruit1 = fruit1["Name"].lower()
        name_fruit2 = fruit2["Name"].lower()
        name_fruit3 = fruit3["Name"].lower()
        name_spice = spice["Name"].lower()



        context = {
            'name_fruit1': name_fruit1,
            'name_fruit2': name_fruit2,
            'name_fruit3': name_fruit3,
            'name_spice': name_spice
        }
        return render(request, 'index_b.html', context=context)

def index(request):
    # Get every tupel with certain name and change the QuerySet into a Dictionary

    list_ingredients= ['Banana', 'Apple', 'Strawberry', 'Honey']
    fruit1 = Ingredients.object.filter(Name = list_ingredients[0]).values()[0]
    fruit2 = Ingredients.object.filter(Name = list_ingredients[1]).values()[0]
    fruit3 = Ingredients.object.filter(Name = list_ingredients[2]).values()[0]
    spice = Ingredients.object.filter(Name = list_ingredients[3]).values()[0]

    # Save the name of the fruit into a variable
    name_fruit1 = fruit1["Name"].lower()
    name_fruit2 = fruit2["Name"].lower()
    name_fruit3 = fruit3["Name"].lower()
    name_spice = spice["Name"].lower()

    #context variable with data of database
    context = {
        'name_fruit1': name_fruit1,
        'name_fruit2': name_fruit2,
        'name_fruit3': name_fruit3,
        'name_spice': name_spice
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
