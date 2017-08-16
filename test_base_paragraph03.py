#coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import unittest

import rulesets
import paragraph03

class TestParagraph03(unittest.TestCase):
	
	def setUp(self):		
		rulesets.set_default_mode(rulesets.spelling_mode().combination)
	

	def test_sentence01(self):
		self.assertEqual(paragraph03.sentence001(), paragraph03.sentence001_content)


	def test_sentence02(self):
		self.assertEqual(paragraph03.sentence002(), paragraph03.sentence002_content)

				
	def test_sentence03(self):
		self.assertEqual(paragraph03.sentence003(), paragraph03.sentence003_content)


	def test_sentence04(self):		
		self.assertEqual(paragraph03.sentence004(), paragraph03.sentence004_content)

				
	def test_sentence05(self):		
		self.assertEqual(paragraph03.sentence005(), paragraph03.sentence005_content)


	def test_sentence06(self):		
		self.assertEqual(paragraph03.sentence006(), paragraph03.sentence006_content)


	def test_sentence07(self):		
		self.assertEqual(paragraph03.sentence007(), paragraph03.sentence007_content)


	def test_sentence08(self):		
		self.assertEqual(paragraph03.sentence008(), paragraph03.sentence008_content)


	def test_sentence09(self):		
		self.assertEqual(paragraph03.sentence009(), paragraph03.sentence009_content)


	def test_sentence10(self):		
		self.assertEqual(paragraph03.sentence010(), paragraph03.sentence010_content)
						
if __name__ == '__main__':
	unittest.main()
	
