'''
from marmeladenladen.models import Ingredients
form django.db import connection

def just_trying(self):
    with connections['marmelade'].cursor() as cursor:
        fruit1 = cursor.execute('SELECT * FROM marmemalde WHERE name= "banana"')
        for fruit1.
    '''
    '''
    variable1 = 'banana'
    ingredients.objects.raw('SELECT * FROM marmelade WHERE name = %s', [variable1])
    '''
    '''try:
    ingredient = Ingredients.objects.get(Name='Banana')
    #except Entry.DoesNotExist as er:

    ingredient.append('Welcome to the marmelade lab! Choose your flavours wisely')
    return ingredient'''
