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
		self.assertEqual(u"e(c=C_BOS)+fs()", sentence_parser.parse_string(u"E."))

	def test_capitalization_not_bos(self):
		self.assertEqual(u"e(c=C_BOS)+space()+e()+fs()", sentence_parser.parse_string(u"E e."))

	def test_capitalization_voiceless_1(self):
		self.assertEqual(u"e(c=C_BOS)+space()+e()+b(m=VOICELESS)+fs()", sentence_parser.parse_string(u"E eb."))

	def test_capitalization_voiceless_2(self):
		self.assertEqual(u"e(c=C_BOS)+space()+e()+d(m=VOICELESS)+fs()", sentence_parser.parse_string(u"E ed."))
		
	def test_german_special_characters(self):
		self.assertEqual(
			u"auml(c=C_BOS)+auml()+space()+ouml(c=C_NOUN)+ouml()+space()+"
			u"uuml(c=C_NOUN)+uuml()+space()+e()+sz()+fs()", 
			sentence_parser.parse_string(u"Ää Öö Üü eß."))

	def test_german_and_french_diphtongs(self):
		self.assertEqual(
			u"ai(c=C_BOS)+space()+au()+space()+"
			u"aumlu()+space()+ei()+space()+"
			u"eu()+space()+oi()+fs()", 
			sentence_parser.parse_string(u"ai au äu ei eu oi."))
	
	def test_word_seperation(self):
		self.assertEqual(
			u"sich(c=C_BOS)+space()+s()+i()+ch()+e()+space()+e()+s()+i()+ch()+space()+"
			u"b()+end()+space()+e()+n()+d()+e()+space()+"
			u"b()+ei()+n()+space()+ein()+e()+s()+fs()",
			sentence_parser.parse_string(u"sich siche esich bend ende bein eines."))
		

if __name__ == '__main__':
	unittest.main()
