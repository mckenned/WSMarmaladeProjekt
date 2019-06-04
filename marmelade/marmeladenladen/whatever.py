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
    fruit1 = Ingredients.object.filter(Name = 'Banana').values()[0]
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
