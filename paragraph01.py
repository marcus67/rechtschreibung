#coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

"""
This module contains the sentences of the first paragraph of the text.
"""

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
	
sentence001_content = (
	u"Casimir und Wendy sind zwei durchschnittliche Deutsche.")
def sentence001():
	return (
		casimir(c=C_BOS)+space()+und()+space()+wendy()+space()+
		sind()+space()+z()+w()+ei()+space()+
		d()+u()+r()+ch()+sch()+n()+i()+tt()+l()+i()+ch()+e()+space()+
		d(c=C_NOUN)+eu()+t()+sch()+e()+fs())
		
	
sentence002_content = (
	u"Sie haben viel gemeinsam, unterscheiden sich aber durch "
	u"sehr stark abweichende Sichten auf die deutsche Rechtschreibung.")
def sentence002():
	return sie(c=C_BOS)+space()+h()+a()+b()+e()+n()+space()+v()+ie()+l()+space()+g()+e()+m()+ei()+n()+s()+a()+m()+comma_sc()+space()+u()+n()+t()+e()+r()+sch()+ei()+d()+e()+n()+space()+s()+i()+ch()+space()+a()+b()+er()+space()+d()+u()+r()+ch()+space()+s()+eh()+r()+space()+st()+a()+r()+k()+space()+a()+b()+w()+ei()+ch()+e()+n()+d()+e()+space()+s(c=C_NOUN)+i()+ch()+t()+e()+n()+space()+au()+f()+space()+die()+space()+d()+eu()+t()+sch()+e()+space()+r(c=C_NOUN)+e()+ch()+t()+sch()+r()+ei()+b()+u()+n()+g()+fs()
	
sentence003_content = (
	u"Casimir ist eher konservativ und möchte am liebsten den Status Quo "
	u"wiederherstellen, wie er vor der Rechtschreibreform im Jahre 1996 gültig war.")
def sentence003():
	return casimir(c=C_BOS)+space()+ist()+space()+e()+h()+er()+space()+k()+o()+n()+s()+e()+r()+v(m=VOICEFULL)+a()+t()+i()+v()+space()+und()+space()+m()+ouml()+ch()+t()+e()+space()+a()+m()+space()+l()+ie()+b()+s()+t()+e()+n()+space()+den()+space()+s(c=C_NOUN)+t()+a()+t()+u()+s()+space()+qu(c=C_NOUN)+o()+space()+w()+ie()+d()+er()+h()+e()+r()+s()+t()+e()+ll()+e()+n()+comma_sc()+space()+w()+ie()+space()+e()+r()+space()+v()+o()+r()+space()+der()+space()+r(c=C_NOUN)+e()+ch()+t()+sch()+r()+ei()+b()+r()+e()+f()+o()+r()+m()+space()+i()+m()+space()+j(c=C_NOUN)+ah()+r()+e()+space()+"1996"+space()+g()+uuml()+l()+t()+i()+g()+space()+w()+a()+r()+fs()
	
sentence004_content = (
	u"Wendy ist eher fortschrittlich und überlegt ständig, "
	u"wie man die Rechtschreibung verbessern und vereinfachen kann.")
def sentence004():
	return wendy(c=C_BOS)+space()+ist()+space()+e()+h()+er()+space()+f()+o()+r()+t()+sch()+r()+i()+tt()+l()+i()+ch()+space()+und()+space()+uuml()+b()+er()+l()+e()+g()+t()+space()+st()+auml()+n()+d()+i()+g()+comma_sc()+space()+wie()+space()+man()+space()+die()+space()+r(c=C_NOUN)+e()+ch()+t()+sch()+r()+ei()+b()+u()+n()+g()+space()+v()+e()+r()+b()+e()+ss()+e()+r()+n()+space()+und()+space()+v()+e()+r()+ei()+n()+f()+a()+ch()+e()+n()+space()+k()+a()+nn()+fs()
	
	
sentence005_content = (
	u"Diese unterschiedlichen Sichtweisen führen ständig zu Diskussionen und "
	u"Streitereien.")
def sentence005():
	return d(c=C_BOS)+ie()+s()+e()+space()+u()+n()+t()+er()+sch()+ie()+d()+l()+i()+ch()+e()+n()+space()+s(c=C_NOUN)+i()+ch()+t()+w()+ei()+s()+e()+n()+space()+f()+uumlh()+r()+e()+n()+space()+st()+auml()+n()+d()+i()+g()+space()+z()+u()+space()+d(c=C_NOUN)+i()+s()+k()+u()+ss()+i()+o()+n()+e()+n()+space()+und()+space()+st(c=C_NOUN)+r()+ei()+t()+e()+r()+ei()+e()+n()+fs()

def paragraph():
	return (
		sentence001() + space() +
		sentence002() + space() +
		sentence003() + space() +
		sentence004() + space() +
		sentence005() + para())
