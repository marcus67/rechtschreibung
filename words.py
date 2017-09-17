# coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

"""
This module supplies shortcuts for frequently used words. It's not really required anymore after
the introduction of the sentence_parser.py module but most of the existing sentence functions rely
on these shortcuts. It *may* eventually go away.
"""

import six

import rulesets
import spelling_mode
from rule_decorator import *

if six.PY3:
	from importlib import reload
	
reload(rulesets)
reload(spelling_mode)

from rulesets import *
from spelling_mode import *

@RuleDecorator(p_conditions = COND_SEPERATED_WORD)		
def abbrechen(c=0):
	return a(c)+b(m=VOICELESS)+b()+r()+e()+ch()+e()+n()
	
@RuleDecorator(p_conditions = COND_BOW)
def aus(c=0):
	return au(c)+s()
	
@RuleDecorator(p_conditions = COND_SEPERATED_WORD)
def bei(c=0):
	return b(c)+ei()
	
@RuleDecorator(p_conditions = COND_SEPERATED_WORD)		
def casimir(c=0):
	return rulesets.c(c=C_NAME|c)+a()+s()+i()+m()+i()+r()
	
@RuleDecorator(p_conditions = COND_SEPERATED_WORD)	
def dass(c=0):
	return d(c)+a()+sz(m=EOW)
	
@RuleDecorator(p_conditions = COND_SEPERATED_WORD)		
def das(c=0):
	return d(c)+a()+s(m=ACTUALLY_SHORT)
	
@RuleDecorator(p_conditions = COND_SEPERATED_WORD)		
def dem(c=0):
	return d(c)+e(m=ACTUALLY_ELONGATED)+m()
	
@RuleDecorator(p_conditions = COND_SEPERATED_WORD)
def den(c=0):
	return d(c)+e(m=ACTUALLY_ELONGATED)+n()
	
@RuleDecorator(p_conditions = COND_SEPERATED_WORD)
def der(c=0):
	return d(c)+e()+r()
	
@RuleDecorator(p_conditions = COND_SEPERATED_WORD)
def die(c=0):
	return d(c)+ie()
	
@RuleDecorator(p_conditions = COND_BOW)
def ein(c=0):
	return ei(c) + n()
	
@RuleDecorator(p_conditions = COND_SEPERATED_WORD)		
def eine(c=0):
	return ein(c) + e()
	
@RuleDecorator(p_conditions = COND_SEPERATED_WORD)
def einen(c=0):
	return eine(c) + n()
	
@RuleDecorator(p_conditions = COND_EOW)
def end(c=0):
	return e(c)+n()+d(m=VOICELESS)
	
@RuleDecorator(p_pattern = u"für", p_conditions = COND_SEPERATED_WORD)		
def fuer(c=0):
	return f()+uuml()+r()
	
@RuleDecorator(p_conditions = COND_SEPERATED_WORD)		
def ist(c=0):
	return i(c)+s()+t()
	
@RuleDecorator(p_conditions = COND_SEPERATED_WORD)
def hat(c=0):
	return h(c)+a()+t()
	
@RuleDecorator(p_conditions = COND_SEPERATED_WORD)		
def man(c=0):
	return m(c)+a()+n(m=ACTUALLY_SHORT)
	
@RuleDecorator(p_conditions = COND_BOW)
def mit(c=0):
	return m(c)+i()+t(m=ACTUALLY_SHORT)
	
@RuleDecorator(p_pattern = u"schließen", p_conditions = COND_EOW)
def schlieszen(c=0):
	return sch(c)+l()+ie()+sz()+e()+n()
	
@RuleDecorator(p_conditions = COND_SEPERATED_WORD)		
def sich(c=0):
	return s(c)+i()+ch()
	
@RuleDecorator(p_conditions = COND_SEPERATED_WORD)
def sie(c=0):
	return s(c)+ie()
	
@RuleDecorator(p_conditions = COND_SEPERATED_WORD)
def sind(c=0):
	return s(c)+i()+n()+d(m=VOICELESS)
	
@RuleDecorator(p_conditions = COND_EOW)
def speichern(c=0):
	return sp(c)+ei()+ch()+e()+r()+n()
	
@RuleDecorator(p_pattern = u"überschreiben", p_conditions = COND_SEPERATED_WORD)
def ueberschreiben(c=0):
	return uuml(c)+b()+er()+sch()+r()+ei()+b()+e()+n()
	
@RuleDecorator(p_conditions = COND_SEPERATED_WORD)
def und(c=0):
	return u(c)+n()+d(m=VOICELESS)
	
@RuleDecorator(p_conditions = COND_BOW)
def viel(c=0):
	return v(c, m=VOICELESS)+ie()+l()
	
@RuleDecorator(p_conditions = COND_SEPERATED_WORD)		
def von(c=0):
	return v(c, m=VOICELESS)+o()+n()
	
@RuleDecorator(p_conditions = COND_SEPERATED_WORD)
def wie(c=0):
	return w(c)+ie()
	
@RuleDecorator(p_conditions = COND_SEPERATED_WORD)	
def wendy(c=0):
	return w(c=C_NAME|c)+e()+n()+d()+y(m=Y_I)
	
def test():
	rulesets.set_default_mode(rulesets.spelling_mode().combination)
	print (casimir()+das()+der()+die()+ist()+sind()+und()+wendy())
	
if __name__ == '__main__':
	test()

