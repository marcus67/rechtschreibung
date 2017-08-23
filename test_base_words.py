#coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import unittest

import words
import rulesets

global logger

class TestWords(unittest.TestCase):
	
	def setUp(self):
		rulesets.set_default_mode(rulesets.spelling_mode().combination)
	
	def test_word_abbrechen(self):
		self.assertEqual("abbrechen", words.abbrechen())

	def test_word_schlieszen(self):
		self.assertEqual("schließen", words.schlieszen())
		
	def test_word_speichern(self):
		self.assertEqual("speichern", words.speichern())
		
if __name__ == '__main__':
	unittest.main()
