#coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import six

import spelling_mode
import rulesets
import paragraph01
import paragraph02
import paragraph03
import paragraph04
import sentences

if six.PY3:
	from importlib import reload
	
reload(spelling_mode)
reload(rulesets)
reload(sentences)
reload(paragraph01)
reload(paragraph02)
reload(paragraph03)
reload(paragraph04)

from rulesets import *

def get_sample_text():
	return (
		paragraph01.paragraph() +
		paragraph02.paragraph() +
		paragraph03.paragraph() + 
		paragraph04.paragraph() + 
		para() + para() + 
		sentences.sentence1() + sentences.sentence2() + sentences.sentence3() + para() + 
		sentences.sentence4() + para() + 
		sentences.sentence5() + para() + 
		sentences.sentence6())
	
def test():
	rulesets.set_default_mode(rulesets.spelling_mode().combination)
	sample_text = get_sample_text()
	print (sample_text)
	
	with open("doc/sample_text.txt", "w", encoding="utf-8") as file:
		file.write(sample_text)
		
if __name__ == '__main__':
	test()

