from decimal import Decimal
import math

#Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

shooping_list = ['milk', 'eggs', 'sugar', 'flour', 'baking_powder']
recipie_tuple = ('Sponge Cake Recipe', 'Ingredients', 'Process')
milk_float = 0.75 
sugar_integer = 300 
baking_powder_decimal = Decimal(1/7) 
process_dictionary = {
	'temperature': 180,
	'time': 40,
	'air_flow': 'none',
	'function': ('top', 'bottom', 'both')
}

#Exercise 2: Round your float up.
milk_float_rounded_up = math.ceil(milk_float)

#Exercise 3: Get the square root of your float.
milk_float_square_root = math.sqrt(milk_float)

#Exercise 4: Select the first element from your dictionary.
my_dictionary_first_element = process_dictionary['temperature']




