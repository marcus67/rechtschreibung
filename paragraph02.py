#coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

"""
This module contains the sentences of the second paragraph of the text.
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
	u"Der grundlegende Unterschied ist ganz einfach: Casimir hat in seiner Jugend "
	u"die damals aktuelle Rechtschreibung kennengelernt und hat sich an sie gewöhnt.")
def sentence001():
	return der(c=C_BOS)+space()+g()+r()+u()+n()+d()+l()+e()+g()+e()+n()+d()+e()+space()+u(c=C_NOUN)+n()+t()+er()+sch()+ie()+d(m=VOICELESS)+space()+ist()+space()+g()+a()+n()+z()+space()+ei()+n()+f()+a()+ch()+colon()+space()+casimir(c=C_BOS_AC)+space()+hat()+space()+i()+n()+space()+s()+ei()+n()+er()+space()+j(c=C_NOUN)+u()+g()+end()+space()+die()+space()+d()+a()+m()+a()+l()+s()+space()+a()+k()+t()+u()+e()+ll()+e()+space()+r(c=C_NOUN)+e()+ch()+t()+sch()+r()+ei()+b()+u()+n()+g()+space()+k()+e()+nn()+e()+n()+g()+e()+l()+e()+r()+n()+t()+space()+und()+space()+hat()+space()+sich()+space()+a()+n()+space()+sie()+space()+g()+e()+w()+oumlh()+n()+t()+fs()	

sentence002_content = (
	u"Er hat die Regeln verinnerlicht und denkt heute nicht mehr über ihre Sinnhaftigkeit nach.")
def sentence002():
	return e(c=C_BOS)+r()+space()+hat()+space()+die()+space()+r(c=C_NOUN)+e()+g()+e()+l()+n()+space()+v()+e()+r()+i()+nn()+e()+r()+l()+i()+ch()+t()+space()+und()+space()+d()+e()+n()+k()+t()+space()+h()+eu()+t()+e()+space()+n()+i()+ch()+t()+space()+m()+eh()+r()+space()+uuml()+b()+e()+r()+space()+ih()+r()+e()+space()+s(c=C_NOUN)+i()+nn()+h()+a()+f()+t()+i()+g()+k()+ei()+t()+space()+n()+a()+ch()+fs()	
	
sentence003_content = (
	u"Zwar sind viele der Regeln durchaus logisch und nachvollziehbar.")
def sentence003():
	return z(c=C_BOS)+w()+a()+r()+space()+sind()+space()+v()+ie()+l()+e()+space()+der()+space()+r(c=C_NOUN)+e()+g()+e()+l()+n()+space()+d()+u()+r()+ch()+au()+s()+space()+l()+o()+g()+i()+sch()+space()+und()+space()+n()+a()+ch()+v()+o()+ll()+z()+ie()+h(m=MUTE)+b()+a()+r()+fs()
	
sentence004_content = (
	u"Es gibt jedoch Gegenbeispiele, die schon aus damaliger Sicht unlogisch waren.")
def sentence004():
	return e(c=C_BOS)+s()+space()+g()+i()+b()+t()+space()+j()+e()+d()+o()+ch()+space()+g(c=C_NOUN)+e()+g()+e()+n()+b()+ei()+sp()+ie()+l()+e()+comma_sc()+space()+die()+space()+sch()+o()+n()+space()+aus()+space()+d()+a()+m()+a()+l()+i()+g()+er()+space()+s(c=C_NOUN)+i()+ch()+t()+space()+u()+n()+l()+o()+g()+i()+sch()+space()+w()+a()+r()+e()+n()+fs()	
	
sentence005_content = (
	u"Besonders störend sind dabei die Fälle, bei denen sich die Aussprache von Worten "
	u"nicht aus dem Schriftbild ableiten lässt.")
def sentence005():
	return b(c=C_BOS)+e()+s()+o()+n()+d()+e()+r()+s()+space()+st()+ouml()+r()+end()+space()+sind()+space()+d()+a()+b()+ei()+space()+die()+space()+f(c=C_NOUN)+auml()+ll()+e()+comma_sc()+space()+bei()+space()+den()+e()+n()+space()+sich()+space()+die()+space()+a(c=C_NOUN)+u()+s()+sp()+r()+a()+ch()+e()+space()+von()+space()+w(c=C_NOUN)+o()+r()+t()+e()+n()+space()+n()+i()+ch()+t()+space()+aus()+space()+dem()+space()+sch(c=C_NOUN)+r()+i()+f()+t()+b()+i()+l()+d(m=VOICELESS)+space()+a()+b()+l()+ei()+t()+e()+n()+space()+l()+auml()+ss()+t()+fs()

sentence006_content = (
	u"Casimir möchte dennoch diesen althergebrachten Regelsatz erhalten und damit das "
	u"Schriftbild, das ihm aus fast der gesamten heute verfügbaren Literatur vertraut ist.")	
def sentence006():
	return casimir(c=C_BOS)+space()+m()+ouml()+ch()+t()+e()+space()+d()+e()+nn()+o()+ch()+space()+d()+ie()+s()+e()+n()+space()+a()+l()+t()+h()+e()+r()+g()+e()+b()+r()+a()+ch()+t()+e()+n()+space()+r(c=C_NOUN)+e()+g()+e()+l()+s()+a()+t()+z()+space()+e()+r()+h()+a()+l()+t()+e()+n()+space()+und()+space()+d()+a()+mit()+space()+das()+space()+sch(c=C_NOUN)+r()+i()+f()+t()+b()+i()+l()+d()+comma_sc()+space()+das()+space()+ih()+m()+space()+aus()+space()+f()+a()+s()+t()+space()+der()+space()+g()+e()+s()+a()+m()+t()+e()+n()+space()+h()+eu()+t()+e()+space()+v()+e()+r()+f()+uuml()+g()+b()+a()+r()+e()+n()+space()+l(c=C_NOUN)+i()+t()+e()+r()+a()+t()+u()+r()+space()+v()+e()+r()+t()+r()+a()+u()+t()+space()+ist()+fs()
	
def paragraph():
	return (
		sentence001() + space() +
		sentence002() + space() +
		sentence003() + space() +
		sentence004() + space() +
		sentence005() + space() +
		sentence006() + para())
