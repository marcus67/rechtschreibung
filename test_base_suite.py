#coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import sys
import unittest

import test_base_rulesets
import test_base_words
import test_base_paragraph01
import test_base_paragraph02
import test_base_paragraph03
import test_base_paragraph04
import test_base_sentence_parser
import test_base_util

class TestBaseSuite(unittest.TestSuite):

	def __init__(self):
		
		super(TestBaseSuite, self).__init__()
		self.addTest(unittest.defaultTestLoader.loadTestsFromModule(test_base_rulesets))
		self.addTest(unittest.defaultTestLoader.loadTestsFromModule(test_base_words))
		self.addTest(unittest.defaultTestLoader.loadTestsFromModule(test_base_paragraph01))
		self.addTest(unittest.defaultTestLoader.loadTestsFromModule(test_base_paragraph02))
		self.addTest(unittest.defaultTestLoader.loadTestsFromModule(test_base_paragraph03))
		self.addTest(unittest.defaultTestLoader.loadTestsFromModule(test_base_paragraph04))
		self.addTest(unittest.defaultTestLoader.loadTestsFromModule(test_base_sentence_parser))
		self.addTest(unittest.defaultTestLoader.loadTestsFromModule(test_base_util))
		
								
if __name__ == '__main__':
	
	print ("Testing with python %s" % sys.version)
	test_suite = TestBaseSuite()
	test_result = unittest.TestResult()
	test_suite.run(test_result)
	print (test_result)
	return_code = 0
	for failure in test_result.failures:
		print(failure[0], failure[1])
		return_code = 1
		
	for error in test_result.errors:
		print(error[0], error[1])
		return_code = 1
		
	exit(return_code)
	
