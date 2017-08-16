#coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import unittest

import rulesets
import paragraph04

class TestParagraph04(unittest.TestCase):
	
	def setUp(self):		
		rulesets.set_default_mode(rulesets.spelling_mode().combination)
	

	def test_sentence01(self):
		self.assertEqual(paragraph04.sentence001()[0], paragraph04.sentence001()[1])


	def test_sentence02(self):
		self.assertEqual(paragraph04.sentence002()[0], paragraph04.sentence002()[1])

				
	def test_sentence03(self):
		self.assertEqual(paragraph04.sentence003()[0], paragraph04.sentence003()[1])


	def test_sentence04(self):		
		self.assertEqual(paragraph04.sentence004()[0], paragraph04.sentence004()[1])

				
	def test_sentence05(self):		
		self.assertEqual(paragraph04.sentence005()[0], paragraph04.sentence005()[1])


	def test_sentence06(self):		
		self.assertEqual(paragraph04.sentence006()[0], paragraph04.sentence006()[1])


	def test_sentence07(self):		
		self.assertEqual(paragraph04.sentence007()[0], paragraph04.sentence007()[1])


	def test_sentence08(self):		
		self.assertEqual(paragraph04.sentence008()[0], paragraph04.sentence008()[1])

						
if __name__ == '__main__':
	unittest.main()
	
