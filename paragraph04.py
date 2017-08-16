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
		"Da Wendy sich mit Software-Entwicklung auskennt, hatte sie die Idee, "
		"eine Applikation zu entwickeln, mit der man verschiedene Regelsätze für die "
		"deutsche Rechtschreibung schnell ausprobieren kann.",
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
		"Es ist ein Unterschied, ob man über unterschiedliche Regelsätze nur redet oder "
		"ob man sich die Auswirkungen auf einen Text direkt konkret anschauen kann.",
		fs())

def sentence003():
	return (
		"Zu diesem Zweck haben sich beide einen Text überlegt, der viele der Phänomene "
		"enthält, an denen sich die Unterschiede leicht erkennen lassen.",
		fs())
		
def sentence004():
	return (
		"Mithilfe von Schaltern lassen sich Regeln individuell aktivieren bzw. deaktivieren.",
		fs())	
		
def sentence005():
	return (
		"Die daraus resultierende Schreibweise des gesamten Textes wird direkt in einem "
		"Fenster dargestellt.",
		fs())
		
def sentence006():
	return (
		"Außerdem werden auf Wunsch, Unterschiede zum Stand vor dem Umschalten farblich "
		"hervorgehoben.",
		fs())
		
def sentence007():
	return (
		"Wenn der Benutzer einen besonders interessanten Regelsatz gebaut hat, kann er "
		"diesen zum späteren Gebrauch unter einem sprechenden Namen abspeichern. ",
		fs())
		
def sentence008():
	return (
		"Casimir ist ganz begeistert von der Idee und trägt durch eigene Ideen zum "
		"Gelingen des Projektes bei.",
		fs())
		
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
