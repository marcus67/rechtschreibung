#coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import six

import rulesets
import words
import spelling_mode

if six.PY3:
	from importlib import reload
	
reload(rulesets)
reload(words)
reload(spelling_mode)

from rulesets import *
from words import *

# Biologie in Theorie und Praxis.
def sentence1():
	return b(c=C_NOUN|C_BOS)+i()+o()+l()+o()+g()+ie()+space()+b()+e()+i(m=TREMA)+n()+h()+a()+l()+t()+e()+t()+space()+th(c=C_NOUN)+e()+o()+r()+ie()+space()+u()+n()+d()+space()+p(c=C_NOUN)+r()+a()+x()+i()+s()+fs()+para()
	
# Physik ist schwer. Chemie ist dumm.
def sentence2():
	return ph(c=C_NOUN|C_BOS)+y()+s()+i()+k()+space()+i()+s()+t()+space()+sch()+w()+e()+r()+fs()+para()+ch(c=C_NOUN|C_BOS, m=CH_GREEK)+e()+m()+ie()+space()+i()+s()+t()+space()+d()+u()+mm()+fs()+para()
	
# Die kleine Nuss mit großer Masse liegt auf der Straße.
def sentence3():
	return d(c=C_BOS)+ie()+space()+k()+l()+ei()+n()+e()+space()+n(c=C_NOUN)+u()+sz(m=EOW)+space()+mit()+space()+g()+r()+o()+sz()+er()+space()+m(c=C_NOUN)+a()+ss()+e()+space()+l()+ie()+g()+t()+space()+au()+f()+space()+d()+e()+r()+space()+st(c=C_NOUN)+r()+a()+sz()+e()+fs()
	
# Viele Häuser sind Beute von kecken Dachsen.
def sentence4():
	return viel(c=C_BOS)+e()+space()+h(c=C_NOUN)+aumlu()+s()+er()+space()+sind()+space()+b(c=C_NOUN)+eu()+t()+e()+space()+von()+space()+k()+e()+ck()+e()+n()+space()+d(c=C_NOUN)+a()+ch(m=CH_CK)+s()+e()+n()+fs()
	
# Der Cellist begleitet den Chor für ein paar Cent im Casino bei 5 Grad Celcius.
def sentence5():
	return der(c=C_BOS)+space()+c(c=C_NOUN, m=C_TSCH)+e()+ll()+i()+s()+t()+space()+b()+e()+g()+l()+ei()+t()+e()+t()+space()+den()+space()+ch(m=CH_K, c=C_NOUN)+o()+r()+space()+fuer()+space()+ein()+space()+p()+aa()+r()+space()+c(c=C_NOUN, m=C_S)+e()+n()+t()+space()+i()+m()+space()+c(c=C_NOUN)+a()+s()+i()+n()+o()+space()+bei()+space()+"5"+space()+g(c=C_NOUN)+r()+a()+d(m=VOICELESS)+space()+c(c=C_NOUN, m=C_Z)+e()+l()+s()+i()+u()+s()+fs()
	
# Statt nur eine Stätte in einer Stadt eines Staates oder einer Nation sollte man viele Stätten in vielen Städten vieler Staaten oder vieler Nationen bauen.
def sentence6():
	return s(c=C_BOS)+t()+a()+tt()+space()+n()+u()+r()+space()+ei()+n()+e()+space()+s(c=C_NOUN)+t()+auml()+tt()+e()+space()+i()+n()+space()+ei()+n()+e()+r()+space()+s(c=C_NOUN)+t()+a()+dt()+space()+ei()+n()+e()+s()+space()+s(c=C_NOUN)+t()+aa()+t()+e()+s()+space()+o()+d()+e()+r()+space()+ei()+n()+e()+r()+space()+n(c=C_NOUN)+a()+tion()+space()+s()+o()+ll()+t()+e()+space()+man()+space()+v()+ie()+l()+e()+space()+s(c=C_NOUN)+t()+auml()+tt()+e()+n()+space()+i()+n()+space()+v()+ie()+l()+e()+n()+space()+s(c=C_NOUN)+t()+auml(m=ACTUALLY_ELONGATED|ELONGATION_MODE_H)+dt(m=ACTUALLY_ELONGATED)+e()+n()+space()+v()+ie()+l()+e()+r()+space()+s(c=C_NOUN)+t()+aa()+t()+e()+n()+space()+o()+d()+e()+r()+space()+v()+ie()+l()+e()+r()+space()+n(c=C_NOUN)+a()+tion()+e()+n()+space()+b()+au()+e()+n()+fs()
		
def test():
	rulesets.set_default_mode(rulesets.spelling_mode().combination)
	print (sentence1() + space()+ sentence2() + space() + sentence3() + space() + sentence4() + space() + sentence5() + space() + sentence6())
	
if __name__ == '__main__':
	test()

