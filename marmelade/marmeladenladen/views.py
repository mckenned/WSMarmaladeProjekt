from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponse
from django.db.models import Q
from django.views import View
from django.views import generic
from django.views.generic.edit import FormView

from marmeladenladen.forms import SelectionForm
from marmeladenladen.models import Ingredients


class Recipe(View):
    def get(self, request):
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
        message = 'This is a sample. Try to make your own recipe or just try this one.'

        context = {
            'name_fruit1': name_fruit1,
            'name_fruit2': name_fruit2,
            'name_fruit3': name_fruit3,
            'name_spice': name_spice,
            'message': message,
        }
        return render(request, 'recipeGenerator.html', context=context)

class SelectionView(FormView):
    template_name = 'index.html'
    form_class = SelectionForm

    def post(self, request):
        form = SelectionForm(request.POST)  #initialize form and fill the form with the date received from the post request
        if 'decision' in request.POST: print('true')   #test if checkbox is in POST-Request
        #if 'decision2' in request.POST: print('true')
        if form.is_valid(): #django forms are with built-in validation
            text1 = form.cleaned_data['decision']
            #text2 = form.cleaned_data['decision2']
            print(text1)
            #print(text2)
            myinput = request.POST.getlist('decision') #get the received data as a list
            myinput_length = len(myinput)   #initialize a variable with the length of myinput
            print(myinput_length)   #console print of the myinput_length
            #get_my_context(some_var, list_length)

            #get the queryset from database depending on the length of myinput
            if myinput_length == 4:
                queryset = Ingredients.object.filter(Q(id = myinput[0]) | Q(id = myinput[1]) | Q(id = myinput[2]) | Q(id = myinput[3])).values()
            elif myinput_length == 3:
                queryset = Ingredients.object.filter(Q(id = myinput[0]) | Q(id = myinput[1]) | Q(id = myinput[2])).values()
            elif myinput_length == 2:
                queryset = Ingredients.object.filter(Q(id = myinput[0]) | Q(id = myinput[1])).values()
            elif myinput_length == 1:
                queryset = Ingredients.object.filter(id = myinput[0]).values()

            #filter queryset depending on type
            spice_queryset = queryset.filter(Type='Spice')
            fruit_queryset = queryset.filter(Type= 'Fruit')

            #if spice is definded, set into name_spice for context variable
            if len(spice_queryset) == 1:
                spice = spice_queryset.values()[0]
                name_spice = spice["Name"].lower()
            else: name_spice = 'honey'  #if no spice is received set an placeholder with 'honey'

            # get fruits for context variable
            # depending on myinput_length set possible placeholder data for template
            number_fruits = len(fruit_queryset)
            if len(fruit_queryset) == 1:
                fruit1 = fruit_queryset.filter(id = myinput[0]).values()[0]
                name_fruit1 = fruit1["Name"].lower()
                name_fruit2 = 'banana'
                name_fruit3 = 'strawberries'

            if len(fruit_queryset) == 2:
                fruit1 = fruit_queryset.filter(id = myinput[0]).values()[0]
                fruit2 = fruit_queryset.filter(id = myinput[1]).values()[0]
                name_fruit1 = fruit1["Name"].lower()
                name_fruit2 = fruit2["Name"].lower()
                name_fruit3 = 'banana'

            if len(fruit_queryset) == 3:
                fruit1 = fruit_queryset.filter(id = myinput[0]).values()[0]
                fruit2 = fruit_queryset.filter(id = myinput[1]).values()[0]
                fruit3 = fruit_queryset.filter(id = myinput[2]).values()[0]
                name_fruit1 = fruit1["Name"].lower()
                name_fruit2 = fruit2["Name"].lower()
                name_fruit3 = fruit3["Name"].lower()

            if len(fruit_queryset) > 3:
                fruit1 = fruit_queryset.filter(id = myinput[0]).values()[0]
                fruit2 = fruit_queryset.filter(id = myinput[1]).values()[0]
                fruit3 = fruit_queryset.filter(id = myinput[2]).values()[0]
                name_fruit1 = fruit1["Name"].lower()
                name_fruit2 = fruit2["Name"].lower()
                name_fruit3 = fruit3["Name"].lower()

            #denpending on myinput_length set a message for the user
            if myinput_length < 4:
                message = 'For a great experience and rich taste we added some ingredients'
            elif myinput_length > 4:
                message = 'Unfortunately we could only use 4 ingredients'
            else:
                message = 'Great! Here is your special recipe.'

            # set context variable aka dictionary, which will be used for filling the template
            context = {
                'form': form,
                'name_fruit1': name_fruit1,
                'name_fruit2': name_fruit2,
                'name_fruit3': name_fruit3,
                'name_spice': name_spice,
                'message': message,
                }
        else: print('Fail! Your form is not valid.')

        #render the website with following data:
        #the data of the request
        #decision which template will be rendered
        #context with all variables which are needed for filling the template
        return render(request, 'recipeGenerator.html', context)

    def get(self, request):
        #new instance of SelectionForm
        form = SelectionForm()
        #creating a dictionary for the return
        context = {'form': form}
        #render website with all needed data
        return render(request, self.template_name, {'form': form})



def index(request):
    return render(request, 'Frontpage.html')

def fruitbasket(request):
    return render(request, 'index.html')
