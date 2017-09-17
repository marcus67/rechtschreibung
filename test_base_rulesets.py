#coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import unittest

import rulesets

global logger

class TestRulesets(unittest.TestCase):
	
	def setUp(self):
		rulesets.set_default_mode(rulesets.spelling_mode().combination)
	
	def test_capitalize(self):
		
		self.assertEqual(u"e", rulesets.capitalize(u"e", c = rulesets.C_NONE))
		self.assertEqual(u"E", rulesets.capitalize(u"e", c = rulesets.C_ADDRESSING))
		self.assertEqual(u"E", rulesets.capitalize(u"e", c = rulesets.C_BOS))
		self.assertEqual(u"E", rulesets.capitalize(u"e", c = rulesets.C_NAME))
		self.assertEqual(u"E", rulesets.capitalize(u"e", c = rulesets.C_NOUN))
		
	def test_double_consonant(self):
		
		self.assertEqual(u"ll", rulesets.double_consonant(u"l"))
		modified_combination = rulesets.spelling_mode().combination
		modified_combination.switch_simplification_double_consonants = True
		rulesets.set_default_mode(modified_combination)
		self.assertEqual(u"l", rulesets.double_consonant(u"l"))

	def test_elongation(self):
		
		self.assertEqual(u"ie", rulesets.elongation(
			rulesets.i, c=rulesets.C_NONE, 
			m=rulesets.ELONGATION_MODE_E))

		self.assertEqual(u"ih", rulesets.elongation(
			rulesets.i, c=rulesets.C_NONE, 
			m=rulesets.ELONGATION_MODE_H))
			
		self.assertEqual(u"ii", rulesets.elongation(
			rulesets.i, c=rulesets.C_NONE, 
			m=rulesets.ELONGATION_MODE_DOUBLE))
						
		self.assertEqual(u"ī", rulesets.elongation(
			rulesets.i, c=rulesets.C_NONE, 
			m=rulesets.ELONGATION_MODE_MACRON))
		
		self.assertEqual(u"Ie", rulesets.elongation(
			rulesets.i, c=rulesets.C_NOUN, 
			m=rulesets.ELONGATION_MODE_E))

		self.assertEqual(u"Ih", rulesets.elongation(
			rulesets.i, c=rulesets.C_NOUN, 
			m=rulesets.ELONGATION_MODE_H))
			
		self.assertEqual(u"Ii", rulesets.elongation(
			rulesets.i, c=rulesets.C_NOUN, 
			m=rulesets.ELONGATION_MODE_DOUBLE))
						
		self.assertEqual(u"Ī", rulesets.elongation(
			rulesets.i, c=rulesets.C_NOUN, 
			m=rulesets.ELONGATION_MODE_MACRON))
				
		self.assertEqual(u"ā", rulesets.elongation(
			rulesets.a, c=rulesets.C_NONE, 
			m=rulesets.ELONGATION_MODE_MACRON))

		self.assertEqual(u"ė", rulesets.elongation(
			rulesets.e, c=rulesets.C_NONE, 
			m=rulesets.ELONGATION_MODE_MACRON))
			
		self.assertEqual(u"ō", rulesets.elongation(
			rulesets.o, c=rulesets.C_NONE, 
			m=rulesets.ELONGATION_MODE_MACRON))
					
		self.assertEqual(u"ū", rulesets.elongation(
			rulesets.u, c=rulesets.C_NONE, 
			m=rulesets.ELONGATION_MODE_MACRON))		
		
		
		
if __name__ == '__main__':
	unittest.main()
	
