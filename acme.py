#!/usr/bin/env python

import random 
a = 1000000
b = 9999999

class Product():
	""" This is the class for the product of Acme"""
			  
	def __init__(self,name, price=10, weight=20, 
			  			flammability = 0.5, identifier = random.randint(a,b)):
		""" Instantiates the Product"""
		self.name = name
		self.price = price
		self.weight = weight
		self.flammability = flammability
		self.identifier = identifier

	def stealability(self):
		"""Calculates the stealability ratio based on price and weight"""
		ratio = self.price*1.0/self.weight
		if ratio < 0.5:
			return "Not so stealable..."
		elif ratio > 1.0:
			return "Very stealable!"
		else:
			return "Kinda stealable."
	
	def explode(self):
		"""Calculates the explodability of the product based on flammability and weight"""
		expl_factor = self.flammability * self.weight
		if expl_factor < 10.0:
			return "...fizzle"
		elif expl_factor > 50.0:
			return "...BABOOM!!"
		else:
			return "...boom!"

class BoxingGlove(Product):
	""" This is the class for BoxingGlove which inherits from Product """

	def __init__(self, name, weight=10, price=10):
		"""Instantiates the Boxing Glove"""
		super().__init__(name,weight)  
		self.name = name
		self.weight = weight
		

	def punch(self):
		"""Calculates how much the glove hurts"""
		if self.weight < 5:
			return "That tickles."
		elif self.weight > 15:
			return "OUCH!"
		else:
			return "Hey that hurt!"

	def explode(self):
		"""This function overrides the parent method for boxing gloves"""
		return "...it's a glove."

