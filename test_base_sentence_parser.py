#coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import unittest

import sentence_parser
import rulesets

global logger

class TestParser(unittest.TestCase):
	
	def setUp(self):
		sentence_parser.setup_logging()		
		rulesets.set_default_mode(rulesets.spelling_mode().combination)
	

	def test_capitalization_bos(self):
		self.assertEqual("e(c=C_BOS)+fs()", sentence_parser.parse_string("E."))

	def test_capitalization_not_bos(self):
		self.assertEqual("e(c=C_BOS)+space()+e()+fs()", sentence_parser.parse_string("E e."))

	def test_capitalization_voiceless_1(self):
		self.assertEqual("e(c=C_BOS)+space()+e()+b(m=VOICELESS)+fs()", sentence_parser.parse_string("E eb."))

	def test_capitalization_voiceless_2(self):
		self.assertEqual("e(c=C_BOS)+space()+e()+d(m=VOICELESS)+fs()", sentence_parser.parse_string("E ed."))
		
	def test_german_special_characters(self):
		self.assertEqual(
			"auml(c=C_BOS)+auml()+space()+ouml(c=C_NOUN)+ouml()+space()+"
				"uuml(c=C_NOUN)+uuml()+space()+e()+sz()+fs()", 
			sentence_parser.parse_string("Ää Öö Üü eß."))

if __name__ == '__main__':
	unittest.main()
