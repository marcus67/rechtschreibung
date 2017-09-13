#coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import unittest

import util

global logger

class TestUtil(unittest.TestCase):
	
	def test_count_bits(self):
		self.assertEqual(0, util.count_bits(0))
		self.assertEqual(1, util.count_bits(1))
		self.assertEqual(1, util.count_bits(16))
		self.assertEqual(1, util.count_bits(65536))
		self.assertEqual(4, util.count_bits(15))
		
		
	def test_html_content_add_and_delete(self):
		
		self.assertEqual(util.get_html_content("ac", "abc", True), "a<span id='ins'>b</span>c")
		self.assertEqual(util.get_html_content("ac", "abc", False), "abc")
		self.assertEqual(util.get_html_content("abc", "ac", True), "a<span id='del'>b</span>c")
		self.assertEqual(util.get_html_content("abc", "ac", False), "ac")
		self.assertEqual(util.get_html_content("abc", "abc", True), "abc")
		self.assertEqual(util.get_html_content("abc", "abc", False), "abc")

	def test_html_content_special_characters(self):
		self.assertEqual(util.get_html_content("\n", "\n", True), "<BR/>")
		self.assertEqual(util.get_html_content("\n", "\n", False), "<BR/>")
		self.assertEqual(util.get_html_content("ė", "ė", True), "&#275;")
		self.assertEqual(util.get_html_content("ė", "ė", False), "&#275;")
		self.assertEqual(util.get_html_content("Ė", "Ė", True), "&#274;")
		self.assertEqual(util.get_html_content("Ė", "Ė", False), "&#274;")
		self.assertEqual(util.get_html_content('"', '"', True), "&quot;")
		self.assertEqual(util.get_html_content('"', '"', False), "&quot;")
		
												
if __name__ == '__main__':
	unittest.main()

