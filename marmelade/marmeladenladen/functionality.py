from django.db.models import Q
from marmeladenladen.models import Ingredients

def prepare_queryset(myinput):
    myinput_length = len(myinput)   #initialize a variable with the length of myinput

    #get the queryset from database depending on the length of myinput
    if myinput_length >= 4:
        queryset = Ingredients.object.filter(Q(id = myinput[0]) | Q(id = myinput[1]) | Q(id = myinput[2]) | Q(id = myinput[3])).values()
    elif myinput_length == 3:
        queryset = Ingredients.object.filter(Q(id = myinput[0]) | Q(id = myinput[1]) | Q(id = myinput[2])).values()
    elif myinput_length == 2:
        queryset = Ingredients.object.filter(Q(id = myinput[0]) | Q(id = myinput[1])).values()
    elif myinput_length == 1:
        queryset = Ingredients.object.filter(id = myinput[0]).values()
    elif myinput_length ==0:
        queryset = Ingredients.object.none()
    return queryset

def prepare_fruits(queryset, myinput):
    #filter queryset depending on type
    fruit_queryset = queryset.filter(Type= 'Fruit')

    # get fruits for context variable
    # depending on myinput_length set possible placeholder data for template
    number_fruits = len(fruit_queryset)
    if len(fruit_queryset) == 0:
        name_fruit1 = 'blueberries'
        name_fruit2 = 'cherries'
        name_fruit3 = 'raspberries'

    if len(fruit_queryset) == 1:
        fruit1 = fruit_queryset.filter(id = myinput[0]).values()[0]
        name_fruit1 = fruit1["Name"].lower()
        name_fruit2 = 'cherries'
        name_fruit3 = 'raspberries'

    if len(fruit_queryset) == 2:
        fruit1 = fruit_queryset.filter(id = myinput[0]).values()[0]
        fruit2 = fruit_queryset.filter(id = myinput[1]).values()[0]
        name_fruit1 = fruit1["Name"].lower()
        name_fruit2 = fruit2["Name"].lower()
        name_fruit3 = 'cherries'

    if len(fruit_queryset) >= 3:
        fruit1 = fruit_queryset.filter(id = myinput[0]).values()[0]
        fruit2 = fruit_queryset.filter(id = myinput[1]).values()[0]
        fruit3 = fruit_queryset.filter(id = myinput[2]).values()[0]
        name_fruit1 = fruit1["Name"].lower()
        name_fruit2 = fruit2["Name"].lower()
        name_fruit3 = fruit3["Name"].lower()

    # set context variable aka dictionary, which will be used for filling the template
    fruits = {
        'name_fruit1': name_fruit1,
        'name_fruit2': name_fruit2,
        'name_fruit3': name_fruit3,
    }

    return fruits

def prepare_spices(queryset):
    #filter queryset depending on type
    spice_queryset = queryset.filter(Type='Spice')

    #if spice is defined, set into name_spice for context variable
    if len(spice_queryset) >= 1:
        spice = spice_queryset.values()[0]
        name_spice = spice["Name"].lower()
    else: name_spice = 'sugar'  #if no spice is received set an placeholder with 'sugar'

    return name_spice

def prepare_message(queryset):

    myinput_length = len(queryset)

    #denpending on myinput_length set a message for the user
    if myinput_length < 4:
        message = 'For a great experience and rich taste we added some ingredients'
    elif myinput_length > 4:
        message = 'Unfortunately we could only use 4 ingredients. Therefore we have choosen your first three fruits and one spice.'
    else:
        message = 'Great! Here is your special recipe.'

    return message
