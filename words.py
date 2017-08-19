# coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

"""
This module supplies shortcuts for frequently used words.
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

@RuleDecorator()		
def abbrechen(c=0):
	return a(c)+bb()+r()+e()+ch()+e()+n()
	
@RuleDecorator()		
def aus(c=0):
	return au(c)+s()
	
@RuleDecorator()		
def bei(c=0):
	return b(c)+ei()
	
@RuleDecorator()		
def casimir(c=0):
	return rulesets.c(c=C_NAME|c)+a()+s()+i()+m()+i()+r()
	
@RuleDecorator()		
def dass(c=0):
	return d(c)+a()+sz(m=EOW)
	
@RuleDecorator()		
def das(c=0):
	return d(c)+a()+s(m=ACTUALLY_SHORT)
	
@RuleDecorator()		
def dem(c=0):
	return d(c)+e(m=ACTUALLY_ELONGATED)+m()
	
@RuleDecorator()		
def den(c=0):
	return d(c)+e(m=ACTUALLY_ELONGATED)+n()
	
@RuleDecorator()		
def der(c=0):
	return d(c)+e()+r()
	
@RuleDecorator()		
def die(c=0):
	return d(c)+ie()
	
@RuleDecorator()		
def ein(c=0):
	return ei(c) + n()
	
@RuleDecorator()		
def eine(c=0):
	return ein(c) + e()
	
@RuleDecorator()		
def einen(c=0):
	return eine(c) + n()
	
@RuleDecorator()		
def end(c=0):
	return e(c)+n()+d(m=VOICELESS)
	
@RuleDecorator(p_pattern = "für")		
def fuer(c=0):
	return f()+uuml()+r()
	
@RuleDecorator()		
def ist(c=0):
	return i(c)+s()+t()
	
@RuleDecorator()		
def hat(c=0):
	return h(c)+a()+t()
	
#@RuleDecorator()		
def man(c=0):
	return m(c)+a()+n(m=ACTUALLY_SHORT)
	
@RuleDecorator()		
def mit(c=0):
	return m(c)+i()+t(m=ACTUALLY_SHORT)
	
@RuleDecorator(p_pattern = "schließen")
def schlieszen(c):
	return sch(c)+l()+ie()+sz()+e()+n()
	
@RuleDecorator(p_conditions = COND_SEPERATED_WORD)		
def sich(c=0):
	return s(c)+i()+ch()
	
@RuleDecorator()		
def sie(c=0):
	return s(c)+ie()
	
@RuleDecorator()		
def sind(c=0):
	return s(c)+i()+n()+d(m=VOICELESS)
	
@RuleDecorator()		
def speichern(c=0):
	return sp(c)+ei()+ch()+e()+r()+n()
	
@RuleDecorator(p_pattern = "überschreiben")
def ueberschreiben(c=0):
	return uuml(c)+b()+er()+sch()+r()+ei()+b()+e()+n()
	
@RuleDecorator()		
def und(c=0):
	return u(c)+n()+d(m=VOICELESS)
	
@RuleDecorator()		
def viel(c=0):
	return v(c, m=VOICELESS)+ie()+l()
	
@RuleDecorator()		
def von(c=0):
	return v(c, m=VOICELESS)+o()+n()
	
@RuleDecorator()		
def wie(c=0):
	return w(c)+ie()
	
@RuleDecorator()		
def wendy(c=0):
	return w(c=C_NAME|c)+e()+n()+d()+y(m=Y_I)
	
def test():
	rulesets.set_default_mode(rulesets.spelling_mode().combination)
	print (casimir()+das()+der()+die()+ist()+sind()+und()+wendy())
	
if __name__ == '__main__':
	test()

