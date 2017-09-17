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
		
		self.assertEqual(util.get_html_content(u"ac", u"abc", True), u"a<span id='ins'>b</span>c")
		self.assertEqual(util.get_html_content(u"ac", u"abc", False), u"abc")
		self.assertEqual(util.get_html_content(u"abc", u"ac", True), u"a<span id='del'>b</span>c")
		self.assertEqual(util.get_html_content(u"abc", u"ac", False), u"ac")
		self.assertEqual(util.get_html_content(u"abc", u"abc", True), u"abc")
		self.assertEqual(util.get_html_content(u"abc", u"abc", False), u"abc")

	def test_html_content_special_characters(self):
		self.assertEqual(util.get_html_content(u"\n", u"\n", True), u"<BR/>")
		self.assertEqual(util.get_html_content(u"\n", u"\n", False), u"<BR/>")
		self.assertEqual(util.get_html_content(u"ė", u"ė", True), u"&#275;")
		self.assertEqual(util.get_html_content(u"ė", u"ė", False), u"&#275;")
		self.assertEqual(util.get_html_content(u"Ė", u"Ė", True), u"&#274;")
		self.assertEqual(util.get_html_content(u"Ė", u"Ė", False), u"&#274;")
		self.assertEqual(util.get_html_content(u'"', u'"', True), u"&quot;")
		self.assertEqual(util.get_html_content(u'"', u'"', False), u"&quot;")
		
												
if __name__ == '__main__':
	unittest.main()

