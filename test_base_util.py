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
										
if __name__ == '__main__':
	unittest.main()
