#coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

"""
This module contains the sentences of the forth paragraph of the text.
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



def sentence001():
	return (
		u"Da Wendy sich mit Software-Entwicklung auskennt, hatte sie die Idee, "
		u"eine Applikation zu entwickeln, mit der man verschiedene Regelsätze für die "
		u"deutsche Rechtschreibung schnell ausprobieren kann.",
		d(c=C_BOS)+a()+space()+wendy()+space()+sich()+space()+mit()+space()+
		s(c=C_NOUN)+o()+f()+t()+w()+a()+r()+e()+hyphen()+
		e(c=C_NOUN)+n()+t()+w()+i()+ck()+l()+u()+n()+g()+space()+au()+s()+k()+e()+nn()+t()+comma_sc()+
		space()+h()+a()+tt()+e()+space()+sie()+space()+die()+space()+
		i(c=C_NOUN)+d()+ee()+comma_sc()+space()+eine()+space()+
		a(c=C_NOUN)+pp()+l()+i()+k()+a()+tion()+space()+z()+u()+space()+
		e()+n()+t()+w()+i()+ck()+e()+l()+n()+comma_sc()+space()+mit()+space()+der()+space()
		+man()+space()+v()+e()+r()+sch()+ie()+d()+e()+n()+e()+space()+
		r(c=C_NOUN)+e()+g()+e()+l()+s()+auml()+t()+z()+e()+space()+fuer()+space()+die()+space()+
		d()+eu()+t()+sch()+e()+space()+r(c=C_NOUN)+e()+ch()+t()+sch()+r()+ei()+b()+u()+n()+g()+space()+
		sch()+n()+e()+ll()+space()+au()+s()+p()+r()+o()+b()+ie()+r()+e()+n()+space()+k()+a()+nn()+fs())	

def sentence002():
	return (
		u"Es ist ein Unterschied, ob man über unterschiedliche Regelsätze nur redet oder "
		u"ob man sich die Auswirkungen auf einen Text direkt konkret anschauen kann.",
		e(c=C_BOS)+s()+space()+ist()+space()+ein()+space()+
		u(c=C_NOUN)+n()+t()+e()+r()+sch()+ie()+d()+comma_sc()+space()+
		o()+b(m=VOICELESS)+space()+man()+space()+uuml()+b()+e()+r()+space()+
		u()+n()+t()+e()+r()+sch()+ie()+d()+l()+i()+ch()+e()+space()+
		r(c=C_NOUN)+e()+g()+e()+l()+s()+auml()+t()+z()+e()+space()+n()+u()+r()+space()+
		r()+e()+d()+e()+t()+space()+o()+d()+e()+r()+space()+
		o()+b(m=VOICELESS)+space()+man()+space()+sich()+space()+die()+space()+
		au(c=C_NOUN)+s()+w()+i()+r()+k()+u()+n()+g()+e()+n()+space()+au()+f()+space()+
		einen()+space()+t(c=C_NOUN)+e()+x()+t()+space()+d()+i()+r()+e()+k()+t()+space()+
		k()+o()+n()+k()+r()+e()+t()+space()+a()+n()+sch()+au()+e()+n()+space()+k()+a()+nn()+fs()
		)

def sentence003():
	return (
		u"Zu diesem Zweck haben sich beide einen Text überlegt, der viele der Phänomene "
		u"enthält, an denen sich die Unterschiede leicht erkennen lassen.",
		z(c=C_BOS)+u()+space()+d()+ie()+s()+e()+m()+space()+z(c=C_NOUN)+w()+e()+ck()+space()+
		h()+a()+b()+e()+n()+space()+sich()+space()+bei()+d()+e()+space()+einen()+space()+
		t(c=C_NOUN)+e()+x()+t()+space()+uuml()+b()+er()+l()+e()+g()+t()+comma_sc()+space()+
		der()+space()+viel()+e()+space()+der()+space()+
		ph(c=C_NOUN)+auml()+n()+o()+m()+e()+n()+e()+space()+
		e()+n()+th()+auml()+l()+t()+comma_sc()+space()+a()+n()+space()+
		d()+e()+n()+e()+n()+space()+sich()+space()+die()+space()+
		u(c=C_NOUN)+n()+t()+er()+sch()+ie()+d()+e()+space()+
		l()+ei()+ch()+t()+space()+er()+k()+e()+nn()+e()+n()+space()+l()+a()+ss()+e()+n()+fs())
		
def sentence004():
	return (
		u"Mithilfe von Schaltern lassen sich Regeln individuell aktivieren bzw. deaktivieren.",
		mit(c=C_BOS)+h()+i()+l()+f()+e()+space()+von()+space()+
		sch(c=C_NOUN)+a()+l()+t()+er()+n()+space()+l()+a()+ss()+e()+n()+space()+
		sich()+space()+r(c=C_NOUN)+e()+g()+e()+l()+n()+space()+
		i()+n()+d()+i()+v()+i()+d()+u()+e()+ll()+space()+
		a()+k()+t()+i()+v()+ie()+r()+e()+n()+space()+
		b()+z()+w()+dot_abbr()+space()+d()+e()+a()+k()+t()+i()+v()+ie()+r()+e()+n()+fs())	
		
def sentence005():
	return (
		u"Die daraus resultierende Schreibweise des gesamten Textes wird direkt in einem "
		u"Fenster dargestellt.",
		die(c=C_BOS)+space()+d()+a()+r()+aus()+space()+
		r()+e()+s()+u()+l()+t()+ie()+r()+e()+n()+d()+e()+space()+
		sch(c=C_NOUN)+r()+ei()+b()+w()+ei()+s()+e()+space()+
		d()+e()+s()+space()+g()+e()+s()+a()+m()+t()+e()+n()+space()+
		t(c=C_NOUN)+e()+x()+t()+e()+s()+space()+w()+i()+r()+d(m=VOICELESS)+space()+
		d()+i()+r()+e()+k()+t()+space()+i()+n()+space()+
		ein()+e()+m()+space()+f(c=C_NOUN)+e()+n()+st()+er()+space()+
		d()+a()+r()+g()+e()+st()+e()+ll()+t()+fs())
		
def sentence006():
	return (
		u"Außerdem werden auf Wunsch, Unterschiede zum Stand vor dem Umschalten farblich "
		u"hervorgehoben.",
		au(c=C_BOS)+sz()+er()+dem()+space()+w()+er()+den()+space()+
		au()+f()+space()+w(c=C_NOUN)+u()+n()+sch()+comma_sc()+space()+
		u(c=C_NOUN)+n()+t()+er()+sch()+ie()+d()+e()+space()+
		z()+u()+m()+space()+st(c=C_NOUN)+a()+n()+d(m=VOICELESS)+space()+
		v()+o()+r()+space()+dem()+space()+
		u(c=C_NOUN)+m()+sch()+a()+l()+t()+e()+n()+space()+
		f()+a()+r()+b()+l()+i()+ch()+space()+
		h()+er()+v()+o()+r()+g()+eh()+o()+b()+e()+n()+fs())
		
def sentence007():
	return (
		u"Wenn der Benutzer einen besonders interessanten Regelsatz gebaut hat, kann er "
		u"diesen zum späteren Gebrauch unter einem sprechenden Namen abspeichern.",
		w(c=C_BOS)+e()+nn()+space()+der()+space()+
		b(c=C_NOUN)+e()+n()+u()+t()+z()+er()+space()+
		einen()+space()+b()+e()+s()+o()+n()+d()+er()+s()+space()+
		i()+n()+t()+er()+e()+ss()+a()+n()+t()+e()+n()+space()+
		r(c=C_NOUN)+e()+g()+e()+l()+s()+a()+t()+z()+space()+
		g()+e()+b()+au()+t()+space()+hat()+comma_sc()+space()+
		k()+a()+nn()+space()+er()+space()+d()+ie()+s()+e()+n()+space()+
		z()+u()+m()+space()+sp()+auml()+t()+er()+e()+n()+space()+
		g(c=C_NOUN)+e()+b()+r()+au()+ch()+space()+u()+n()+t()+er()+
		space()+ein()+e()+m()+space()+sp()+r()+e()+ch()+e()+n()+den()+space()+
		n(c=C_NOUN)+a()+m()+e()+n()+space()+a()+b()+speichern()+fs())
		
def sentence008():
	return (
		u"Casimir ist ganz begeistert von der Idee und trägt durch eigene Vorschläge zum "
		u"Gelingen des Projektes bei.",
		casimir(c=C_BOS|C_NAME)+space()+ist()+space()+g()+a()+n()+z()+space()+
		b()+e()+g()+ei()+st()+er()+t()+space()+von()+space()+
		der()+space()+i(c=C_NOUN)+d()+ee()+space()+und()+space()+
		t()+r()+auml()+g()+t()+space()+d()+u()+r()+ch()+space()+
		ei()+g()+e()+n()+e()+space()+v(c=C_NOUN)+o()+r()+sch()+l()+auml()+g()+e()+space()+
		z()+u()+m()+space()+g(c=C_NOUN)+e()+l()+i()+n()+g()+e()+n()+space()+
		d()+e()+s()+space()+p(c=C_NOUN)+r()+o()+j()+e()+k()+t()+e()+s()+space()+bei()+fs())
		
def paragraph():
	return (
		sentence001()[1] + space() +
		sentence002()[1] + space() +
		sentence003()[1] + space() +
		sentence004()[1] + space() +
		sentence005()[1] + space() +
		sentence006()[1] + space() +
		sentence007()[1] + space() +
		sentence008()[1] + para())
