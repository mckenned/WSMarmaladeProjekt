from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponse
from django.views import View
from django.views import generic
from django.views.generic.edit import FormView
from django.db.models import Q

from marmeladenladen.forms import SelectionForm
from marmeladenladen.models import Ingredients
from marmeladenladen.functionality import prepare_queryset, prepare_fruits, prepare_spices, prepare_message




'''
Example of recipe without user userinput
url --> /recipe/
'''

class Recipe(View):
    def get(self, request):

        context = {
            'name_fruit1': 'banana',
            'name_fruit2': 'apple',
            'name_fruit3': 'strawberry',
            'name_spice': 'honey',
            'message': 'This is a sample. Try to make your own recipe or just try this one.',
        }
        return render(request, 'recipeGenerator.html', context=context)




'''
Here starts the real magic:
Tadaaaa! Our incredible view to select our options
URL:            /fruitbasket/
Function GET:   Setting up the form for use. In this view you choose your ingredients and submit them. Simple as that.
Function POST:  Sending the userinput to the server without saving the data into a database (performance).
                We fetch the input from the request und set it into a list.
                From here on we use this list and the database "Ingredients" to refine the data for our context variable.
                Functionality happens within functionality.py to reduce the logic within the views.
                At the end we render a webpage with our context and the template 'recipeGenerator.html'
'''

class SelectionView(FormView):
    template_name = 'index.html'
    form_class = SelectionForm

    def post(self, request):    #totally magic. Fetching POST-data, pouff, ready page

        form = SelectionForm(request.POST)  #initialize form and fill the form with the date received from the post request
        if 'decision' in request.POST: print('true')   #test if checkbox is in POST-Request

        if form.is_valid(): #django forms are with built-in validation
            text1 = form.cleaned_data['decision']
            print(text1)

            queryset, myinput = prepare_queryset(request)
            context = prepare_fruits(queryset, myinput)
            context['name_spice'] = prepare_spices(queryset)
            context['message'] = prepare_message(queryset)
            context['form'] = form

        else:
            print('Fail! Your form is not valid.')
            context = {
                'name_fruit1': 'banana',
                'name_fruit2': 'apple',
                'name_fruit3': 'strawberry',
                'name_spice': 'honey',
                'message': 'Unfortunately you did not choose any fruits. Here is a sample. Try again to make your own recipe or just try this one.',
            }
            return render(request, 'recipeGenerator.html', context=context)

        '''
        render the website with following data:
        - the data of the request
        - decision which template will be rendered
        - context with all variables which are needed for filling the template
        '''
        return render(request, 'recipeGenerator.html', context)

    def get(self, request):
        #new instance of SelectionForm
        form = SelectionForm()
        #creating a dictionary for the return
        context = {'form': form}
        #render website with all needed data
        return render(request, self.template_name, {'form': form})





'''
Our absolut wonderful startsite
URL:    ''
'''

def index(request):
    return render(request, 'Frontpage.html')




'''
Testing the template and static files
URL:    '/test/'
'''

def fruitbasket(request):
    return render(request, 'index.html')
