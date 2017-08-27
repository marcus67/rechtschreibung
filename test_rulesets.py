#coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import unittest

import rulesets

global logger

class TestRulesets(unittest.TestCase):
	
	def setUp(self):
		rulesets.set_default_mode(rulesets.spelling_mode().combination)
	
	def test_capitalize(self):
		
		self.assertEqual("e", rulesets.capitalize("e", c = rulesets.C_NONE))
		self.assertEqual("E", rulesets.capitalize("e", c = rulesets.C_ADDRESSING))
		self.assertEqual("E", rulesets.capitalize("e", c = rulesets.C_BOS))
		self.assertEqual("E", rulesets.capitalize("e", c = rulesets.C_NAME))
		self.assertEqual("E", rulesets.capitalize("e", c = rulesets.C_NOUN))
		
	def test_double_consonant(self):
		
		self.assertEqual("ll", rulesets.double_consonant("l"))
		modified_combination = rulesets.spelling_mode().combination
		modified_combination.switch_simplification_double_consonants = True
		rulesets.set_default_mode(modified_combination)
		self.assertEqual("l", rulesets.double_consonant("l"))

	def test_elongation(self):
		
		self.assertEqual("ie", rulesets.elongation(
			rulesets.i, c=rulesets.C_NONE, 
			m=rulesets.ELONGATION_MODE_E))

		self.assertEqual("ih", rulesets.elongation(
			rulesets.i, c=rulesets.C_NONE, 
			m=rulesets.ELONGATION_MODE_H))
			
		self.assertEqual("ii", rulesets.elongation(
			rulesets.i, c=rulesets.C_NONE, 
			m=rulesets.ELONGATION_MODE_DOUBLE))
						
		self.assertEqual("ī", rulesets.elongation(
			rulesets.i, c=rulesets.C_NONE, 
			m=rulesets.ELONGATION_MODE_MACRON))
		
		self.assertEqual("Ie", rulesets.elongation(
			rulesets.i, c=rulesets.C_NOUN, 
			m=rulesets.ELONGATION_MODE_E))

		self.assertEqual("Ih", rulesets.elongation(
			rulesets.i, c=rulesets.C_NOUN, 
			m=rulesets.ELONGATION_MODE_H))
			
		self.assertEqual("Ii", rulesets.elongation(
			rulesets.i, c=rulesets.C_NOUN, 
			m=rulesets.ELONGATION_MODE_DOUBLE))
						
		self.assertEqual("Ī", rulesets.elongation(
			rulesets.i, c=rulesets.C_NOUN, 
			m=rulesets.ELONGATION_MODE_MACRON))
				
		self.assertEqual("ā", rulesets.elongation(
			rulesets.a, c=rulesets.C_NONE, 
			m=rulesets.ELONGATION_MODE_MACRON))

		self.assertEqual("ė", rulesets.elongation(
			rulesets.e, c=rulesets.C_NONE, 
			m=rulesets.ELONGATION_MODE_MACRON))
			
		self.assertEqual("ō", rulesets.elongation(
			rulesets.o, c=rulesets.C_NONE, 
			m=rulesets.ELONGATION_MODE_MACRON))
					
		self.assertEqual("ū", rulesets.elongation(
			rulesets.u, c=rulesets.C_NONE, 
			m=rulesets.ELONGATION_MODE_MACRON))		
		
		
		
if __name__ == '__main__':
	unittest.main()
