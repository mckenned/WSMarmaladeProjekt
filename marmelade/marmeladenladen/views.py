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

def start(request):
    return render(request, 'Frontpage.html')

def index(request):
    return render(request, 'index.html', context=context)
