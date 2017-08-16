#coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import unittest

import rulesets
import paragraph02

class TestParagraph02(unittest.TestCase):
	
	def setUp(self):		
		rulesets.set_default_mode(rulesets.spelling_mode().combination)
	

	def test_sentence01(self):
		self.assertEqual(paragraph02.sentence001(), paragraph02.sentence001_content)


	def test_sentence02(self):
		self.assertEqual(paragraph02.sentence002(), paragraph02.sentence002_content)

				
	def test_sentence03(self):
		self.assertEqual(paragraph02.sentence003(), paragraph02.sentence003_content)


	def test_sentence04(self):		
		self.assertEqual(paragraph02.sentence004(), paragraph02.sentence004_content)

				
	def test_sentence05(self):		
		self.assertEqual(paragraph02.sentence005(), paragraph02.sentence005_content)


	def test_sentence06(self):		
		self.assertEqual(paragraph02.sentence006(), paragraph02.sentence006_content)
				
if __name__ == '__main__':
	unittest.main()
