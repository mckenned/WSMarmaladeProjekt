
from unittest import TestCase
from marmeladenladen.models import Ingredients
from marmeladenladen.functionality import *
from marmeladenladen.models import Ingredients

class TestMarmelade(TestCase):
	"Jam tests"
	myInput0=[]
	myInput1=['1']
	myInput2=['1','2']
	myInput3=['1','2','3'] #banana, blueberry, strawberry
	myInput4=['1','2','3', '4']
	myInput5=['1','2','3', '4','5']
	myInputSpice=['50'] #vanilla
	'''
		Get the queryset from database based on the id's contained 
		in the list passed as an argument. For lists of length greater than,
		only retrieve the first 4 objects from the db.
		Any id from 1 to 51 is contained in the database
	'''
	def testPrepareQuerySetLength0(self):
		queryset = prepare_queryset(self.myInput0)
		self.assertEqual(0, len(queryset))

	def testPrepareQuerySetLength1(self):
		queryset = prepare_queryset(self.myInput1)
		self.assertEqual(1, len(queryset))
	
	def testPrepareQuerySetLength2(self):
		queryset = prepare_queryset(self.myInput2)
		self.assertEqual(2, len(queryset))

	def testPrepareQuerySetLength3(self):
		queryset = prepare_queryset(self.myInput3)
		self.assertEqual(3, len(queryset))

	def testPrepareQuerySetLength4(self):
		queryset = prepare_queryset(self.myInput4)
		self.assertEqual(4, len(queryset))

	def testPrepareQuerySetLength5(self):
		queryset = prepare_queryset(self.myInput5)
		self.assertEqual(4, len(queryset))

	'''
		Testing the method prepare_fruits, which returns a dictionary of length 4
		filled out with a combination of the fruit chosen and the default fruit,
		which are blueberries, cherries, and raspberries. All names are lower case.
	'''
	def testPrepareFruits0Fruit(self):
		queryset = prepare_queryset(self.myInput0)
		fruits = prepare_fruits(queryset, self.myInput0)
		self.assertEqual(fruits['name_fruit1'], 'blueberries')
		self.assertEqual(fruits['name_fruit2'], 'cherries')
		self.assertEqual(fruits['name_fruit3'], 'raspberries')

	def testPrepareFruits1Fruit(self):
		queryset = prepare_queryset(self.myInput1)
		fruits = prepare_fruits(queryset, self.myInput1)
		self.assertEqual(fruits['name_fruit1'], 'bananas')
		self.assertEqual(fruits['name_fruit2'], 'cherries')
		self.assertEqual(fruits['name_fruit3'], 'raspberries')

	def testPrepareFruits2Fruit(self):
		queryset = prepare_queryset(self.myInput2)
		fruits = prepare_fruits(queryset, self.myInput2)
		self.assertEqual(fruits['name_fruit1'], 'bananas')
		self.assertEqual(fruits['name_fruit2'], 'blueberries')
		self.assertEqual(fruits['name_fruit3'], 'cherries')
	
	def testPrepareFruits3Fruit(self):
		queryset = prepare_queryset(self.myInput3)
		fruits = prepare_fruits(queryset, self.myInput3)
		self.assertEqual(fruits['name_fruit1'], 'bananas')
		self.assertEqual(fruits['name_fruit2'], 'blueberries')
		self.assertEqual(fruits['name_fruit3'], 'strawberries')

	'''
		Testing the method prepare_spices. If a spice is defined, save as String in name_spice
		Otherwise if no spice is defined, set it to sugar.
	'''
	def testPrepareSpicesWithSpice(self):
		queryset = prepare_queryset(self.myInputSpice)
		name_spice = prepare_spices(queryset)
		self.assertEqual('vanilla',name_spice)

	def testPrepareSpicesWithoutSpice(self):
		queryset = prepare_queryset(self.myInput5)
		name_spice = prepare_spices(queryset)
		self.assertEqual('sugar', name_spice)

	def testPrepareMessageAddIngredients(self):
		'''
		If the list of ingredients has less than 4 elements, the message should 
		mention that ingredients have been added
		'''
		message=prepare_message([1])
		self.assertEqual('For a great experience and rich taste we added some ingredients', message)	

	def testPrepareMessageTooManyIngredients(self):
		'''
		If the list of ingredients has more than 4 elements, the message should 
		mention that ingredients have been taken out
		'''
		message=prepare_message([1,2,3,4,5])
		self.assertEqual('Unfortunately we could only use 4 ingredients. Therefore we have choosen your first three fruits and one spice.', message)

	def testPrepareMessageRightIngredients(self):
		'''
		Message for a list of 4 ingredients does not add or take out any ingredients.
		'''
		message=prepare_message([1,2,3,4])
		self.assertEqual('Great! Here is your special recipe.', message)
