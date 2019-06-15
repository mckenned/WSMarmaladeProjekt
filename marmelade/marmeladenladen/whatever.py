def index(request):
    submitbutton= request.POST.get("submit")

    choosen_fruit1=''
    choosen_fruit2=''
    choosen_fruit3=''
    choosen_spice=''

    form= UserForm(request.POST or None)
    if form.is_valid():
        choosen_fruit1= form.cleaned_data.get("f_decision1")
        choosen_fruit2= form.cleaned_data.get("f_decision2")
        choosen_fruit3= form.cleaned_data.get("f_decision3")
        choosen_spice= from.cleaned_data.get("s_decision")

def generator(request):
    # Get every tupel with certain name and change the QuerySet into a Dictionary
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

    return render(request, 'generator.html', context=context)

#first try of modeling first function into class
    from django.db.models import Q
    '''
    class generator(generic.ListView):

        template_name = 'marmeladenladen/templates/index.html'
        context_object_name = 'ing_list'
        fruit1 = 'Banana'
        fruit2 = 'Apple'
        fruit3 = 'Strawberry'
        spice = 'Honey'
        list_ing = Ingredients.object.filter(Q(Name = fruit1) | Q(Name = fruit2) | Q(Name = fruit3) | Q(Name = spice))
        # another form of "queryset = Publisher.objects.all()"
        model = Ingredients

        def get_queryset(self):
            fruit1 = 'Banana'
            fruit2 = 'Apple'
            fruit3 = 'Strawberry'
            spice = 'Honey'
            list_ing = Ingredients.object.filter(Q(Name = fruit1) | Q(Name = fruit2) | Q(Name = fruit3) | Q(Name = spice))
            return list_ing

        def get_context_data(self, **kwargs):
            list_ing = self.list_ing.values()[0]
            name_fruit1 = self.list_ing[0]
            name_fruit2 = self.list_ing[1]
            name_fruit3 = self.list_ing[2]
            name_spice = self.list_ing[3]
            context = super(generator, self).get_context_data(**kwargs)
            context = {
                'name_fruit1': name_fruit1,
                'name_fruit2': name_fruit2,
                'name_fruit3': name_fruit3,
                'name_spice': name_spice
            }
            return context

        def lets_look(self, request, context):
            return render(request, 'generator.html', context=context)'''

# Function for easy db-fetching nad endering the template
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
