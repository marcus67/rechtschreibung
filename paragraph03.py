#coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

"""
This module contains the sentences of the third paragraph of the text.
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
	u"Wendy hat einen anderen Ansatz.")
def sentence001():
	return wendy(c=C_BOS)+space()+h()+a()+t()+space()+ein()+e()+n()+space()+a()+n()+d()+e()+r()+e()+n()+space()+a(c=C_NOUN)+n()+s()+a()+t()+z()+fs()
	
sentence002_content = (
	u"Sie möchte, dass die Rechtschreibung in erster Linie dem Lesenden und Schreibenden "
	u"hilft, einen Text möglichst einfach zu lesen bzw. zu erstellen.")
def sentence002():
	return sie(c=C_BOS)+space()+m()+ouml()+ch()+t()+e()+comma_sc()+space()+dass()+space()+die()+space()+r(c=C_NOUN)+e()+ch()+t()+sch()+r()+ei()+b()+u()+n()+g()+space()+i()+n()+space()+e()+r()+s()+t()+er()+space()+l(c=C_NOUN)+i()+n()+i()+e()+space()+dem()+space()+l(c=C_NOUN)+e()+s()+e()+n()+d()+e()+n()+space()+und()+space()+sch(c=C_NOUN)+r()+ei()+b()+e()+n()+d()+e()+n()+space()+h()+i()+l()+f()+t()+comma_sc()+space()+ein()+e()+n()+space()+t(c=C_NOUN)+e()+x()+t()+space()+m()+ouml()+g()+l()+i()+ch()+s()+t()+space()+ei()+n()+f()+a()+ch()+space()+z()+u()+space()+l()+e()+s()+e()+n()+space()+b()+z()+w()+dot_abbr()+space()+z()+u()+space()+e()+r()+st()+e()+ll()+e()+n()+fs()
		
sentence003_content = (
	u"Einfach bedeutet dabei mit möglichst einfachen, nachvollziehbaren Regeln.")
def sentence003():
	return ei(c=C_BOS)+n()+f()+a()+ch()+space()+b()+e()+d()+eu()+t()+e()+t()+space()+d()+a()+b()+ei()+space()+mit()+space()+m()+ouml()+g()+l()+i()+ch()+s()+t()+space()+ei()+n()+f()+a()+ch()+e()+n()+comma_sc()+space()+n()+a()+ch()+v()+o()+ll()+z()+ie()+h()+b()+a()+r()+e()+n()+space()+r(c=C_NOUN)+e()+g()+e()+l()+n()+fs()
		
sentence004_content = (
	u"Auch möchte sie die Anzahl der Regeln so weit wie möglich reduzieren.")
def sentence004():
	return au(c=C_BOS)+ch()+space()+m()+ouml()+ch()+t()+e()+space()+sie()+space()+die()+space()+a(c=C_NOUN)+n()+z()+ah()+l()+space()+der()+space()+r(c=C_NOUN)+e()+g()+e()+l()+n()+space()+s()+o()+space()+w()+ei()+t()+space()+wie()+space()+m()+ouml()+g()+l()+i()+ch()+space()+r()+e()+d()+u()+z()+ie()+r()+e()+n()+fs()	
sentence005_content = (
	u"Die Überarbeitung des Regelsatzes hätte offensichtlich die zum Teil drastische "
	u"Änderung des Schriftbildes zur Folge.")
def sentence005():
	return die(c=C_BOS)+space()+uuml(c=C_NOUN)+b()+er()+a()+r()+b()+ei()+t()+u()+n()+g()+space()+d()+e()+s()+space()+r(c=C_NOUN)+e()+g()+e()+l()+s()+a()+t()+z()+e()+s()+space()+h()+auml()+tt()+e()+space()+o()+ff()+e()+n()+s()+i()+ch()+t()+l()+i()+ch()+space()+die()+space()+z()+u()+m()+space()+t(c=C_NOUN)+ei()+l()+space()+d()+r()+a()+s()+t()+i()+sch()+e()+space()+auml(c=C_NOUN)+n()+d()+e()+r()+u()+n()+g()+space()+d()+e()+s()+space()+sch(c=C_NOUN)+r()+i()+f()+t()+b()+i()+l()+d()+e()+s()+space()+z()+u()+r()+space()+f(c=C_NOUN)+o()+l()+g()+e()+fs()
	
sentence006_content = (
	u"Kein Satz würde mehr so aussehen wie vorher.")	
def sentence006():
	return k(c=C_BOS)+ei()+n()+space()+s(c=C_NOUN)+a()+t()+z()+space()+w()+uuml()+r()+d()+e()+space()+m()+eh()+r()+space()+s()+o()+space()+au()+s()+s()+e()+h()+e()+n()+space()+w()+ie()+space()+v()+o()+r()+h()+e()+r()+fs()
	
sentence007_content = (
	u"Alle Werke der Literatur müssten angepasst werden.")	
def sentence007():
	return a(c=C_BOS)+ll()+e()+space()+w(c=C_NOUN)+e()+r()+k()+e()+space()+der()+space()+l(c=C_NOUN)+i()+t()+e()+r()+a()+t()+u()+r()+space()+m()+uuml()+ss()+t()+e()+n()+space()+a()+n()+g()+e()+p()+a()+ss()+t()+space()+w()+e()+r()+d()+e()+n()+fs()

sentence008_content = (
	u"Alle Menschen müssten umlernen.")	
def sentence008():
	return a(c=C_BOS)+ll()+e()+space()+m(c=C_NOUN)+e()+n()+sch()+e()+n()+space()+m()+uuml()+ss()+t()+e()+n()+space()+u()+m()+l()+e()+r()+n()+e()+n()+fs()
	
sentence009_content = (
	u"Andererseits könnten sich Kinder schneller das Lesen und Schreiben aneignen, "
	u"weil sie weniger Zeit mit dem Lernen überflüssiger und inkonsistenter Regeln "
	u"verschwenden würden.")	
def sentence009():
	return a(c=C_BOS)+n()+d()+e()+r()+er()+s()+ei()+t()+s()+space()+k()+ouml()+nn()+t()+e()+n()+space()+s()+i()+ch()+space()+k(c=C_NOUN)+i()+n()+d()+er()+space()+sch()+n()+e()+ll()+er()+space()+das()+space()+l(c=C_NOUN)+e()+s()+e()+n()+space()+und()+space()+sch(c=C_NOUN)+r()+ei()+b()+e()+n()+space()+a()+n()+ei()+g()+n()+e()+n()+comma_sc()+space()+w()+ei()+l()+space()+sie()+space()+w()+e()+n()+i()+g()+e()+r()+space()+z(c=C_NOUN)+ei()+t()+space()+mit()+space()+dem()+space()+l(c=C_NOUN)+e()+r()+n()+e()+n()+space()+uuml()+b()+er()+f()+l()+uuml()+ss()+i()+g()+er()+space()+und()+space()+i()+n()+k()+o()+n()+s()+i()+s()+t()+e()+n()+t()+er()+space()+r(c=C_NOUN)+e()+g()+e()+l()+n()+space()+v()+e()+r()+sch()+w()+e()+n()+d()+e()+n()+space()+w()+uuml()+r()+d()+e()+n()+fs()
		
sentence010_content = (
	u"Auch Nichtmuttersprachler würden davon profitieren.")
def sentence010():
	return au(c=C_NOUN)+ch()+space()+n(c=C_NOUN)+i()+ch()+t()+m()+u()+tt()+er()+sp()+r()+a()+ch()+l()+e()+r()+space()+w()+uuml()+r()+d()+e()+n()+space()+d()+a()+v()+o()+n()+space()+p()+r()+o()+f()+i()+t()+ie()+r()+e()+n()+fs()	
	
def paragraph():
	return (
		sentence001() + space() +
		sentence002() + space() +
		sentence003() + space() +
		sentence004() + space() +
		sentence005() + space() +
		sentence006() + space() +
		sentence007() + space() +
		sentence008() + space() +
		sentence009() + space() +
		sentence010() + para())
