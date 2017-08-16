#coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import unittest

import rulesets
import paragraph01

class TestParagraph01(unittest.TestCase):
	
	def setUp(self):		
		rulesets.set_default_mode(rulesets.spelling_mode().combination)
	

	def test_sentence01(self):
		self.assertEqual(paragraph01.sentence001(), paragraph01.sentence001_content)


	def test_sentence02(self):
		self.assertEqual(paragraph01.sentence002(), paragraph01.sentence002_content)

				
	def test_sentence03(self):
		self.assertEqual(paragraph01.sentence003(), paragraph01.sentence003_content)


	def test_sentence04(self):		
		self.assertEqual(paragraph01.sentence004(), paragraph01.sentence004_content)

				
	def test_sentence05(self):		
		self.assertEqual(paragraph01.sentence005(), paragraph01.sentence005_content)
		
		
if __name__ == '__main__':
	unittest.main()
