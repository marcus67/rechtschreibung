#coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import string
import six

import spelling_mode
from rule_decorator import RuleDecorator

if six.PY3:
	from importlib import reload
	
reload(spelling_mode)

from spelling_mode import *

global default_mode

def set_default_mode(mymode):
	global default_mode
	default_mode = mymode
	
def get_default_mode():
	global default_mode
	return default_mode
	
def to_upper(l):
	if l == 'ü':
		return 'Ü'
	elif l == 'ä':
		return 'Ä'
	elif l == 'ö':
		return 'Ö'
	elif l == 'š':
		return 'Š'
	elif l == 'č':
		return 'Č'
	elif l == 'ā':
		return 'Ā'
	elif l == 'ė':
		return 'Ė'
	elif l == 'ī':
		return 'Ī'
	elif l == 'ō':
		return 'Ō'
	elif l == 'ū':
		return 'Ū'
	elif l == 'ß':
		return 'ß'
	else:
		return l.upper()
		
def capitalize(l, c=C_NONE):
	if default_mode.switch_capitalization_all_capital or(c & default_mode.bitswitch_capitalization):
		if l == 'ß':
			if default_mode.switch_capitalization_expand_sz:
				return 'SS'
			else:
				return 'ß'
		else:
			return to_upper(l)
	else:
		return l
		
@RuleDecorator(p_pattern = " ")		
def space(c=C_NONE):
	if default_mode.switch_layout_word_separation:
		return " "
	else:
		return ""

@RuleDecorator(p_pattern = ".")		
def fs():
	if default_mode.switch_punctuation_full_stop:
		return "."
	else:
		return ""
		
def para():
	if default_mode.switch_layout_paragraph_separation:
		return "\n"
	else:
		return space()
		
def double_consonant(l):
	if default_mode.switch_simplification_double_consonants:
		return capitalize(l)
	else:
		return capitalize(l+l)
		
@RuleDecorator(p_pattern = ",")		
def comma_sc():
	if default_mode.switch_punctuation_comma_sub_clause:
		return ","
	else:
		return ""
		
@RuleDecorator(p_pattern = ":")		
def colon():
	if default_mode.switch_punctuation_colon:
		return ":"
	else:
		return ""
		
@RuleDecorator(p_pattern = ".")		
def dot_abbr():
	if default_mode.switch_punctuation_dot_abbr:
		return "."
	else:
		return ""
		
@RuleDecorator(p_pattern = "-")		
def hyphen():
	return "-"
		
def elongation(l, c, m):
	default_elongation_mode = m & ELONGATION_MODE_MASK
	current_mode = default_mode.segmented_control_harmonization_elongation
	if current_mode == ELONGATION_MODE_NONE or (current_mode == ELONGATION_MODE_DEFAULT and default_elongation_mode == ELONGATION_MODE_NONE):
		return l(c)
	elif current_mode == ELONGATION_MODE_E or (current_mode == ELONGATION_MODE_DEFAULT and default_elongation_mode == ELONGATION_MODE_E):
		return l(c) + capitalize("e")
	elif current_mode == ELONGATION_MODE_H or (current_mode == ELONGATION_MODE_DEFAULT and default_elongation_mode == ELONGATION_MODE_H):
		return l(c) + capitalize("h")
	elif current_mode == ELONGATION_MODE_MACRON or (current_mode == ELONGATION_MODE_DEFAULT and default_elongation_mode == ELONGATION_MODE_MACRON):
		if (l == a):
			return capitalize("ā")
		elif (l == e):
			return capitalize("ė")
		elif (l == i):
			return capitalize("ī")
		elif (l == o):
			return capitalize("ō")
		elif (l == u):
			return capitalize("ū")
		else:
			return l(c) + l()
			
	else:
		return l(c) + l()
		
# ōūāī

@RuleDecorator()		
def a(c=C_NONE):
	return capitalize("a", c)
	
@RuleDecorator()		
def aa(c=C_NONE):
	return elongation(a, c, ELONGATION_MODE_DOUBLE)
	
@RuleDecorator()		
def ah(c=C_NONE):
	return elongation(a, c, ELONGATION_MODE_H)
	
@RuleDecorator()		
def au(c=C_NONE):
	return capitalize("a", c) + capitalize("u")
	
def _auml(c=C_NONE):
	return capitalize("ä", c)
	
@RuleDecorator(p_pattern = 'ä')		
def auml(c=C_NONE, m=0):
	if default_mode.switch_simplification_expand_umlaut:
		return capitalize("a", c) + capitalize("e")
	else:
		if (m & ACTUALLY_ELONGATED) > 0 and default_mode.switch_harmonization_homophony_elongated_vowels:
			return elongation(_auml, c, m & ELONGATION_MODE_MASK)
		else:
			return _auml(c)
			
@RuleDecorator(p_pattern = 'äu')		
def aumlu(c=C_NONE):
	if default_mode.switch_simplification_aumlu_oi:
		return o(c) + i()
	else:
		return capitalize("ä", c) + u()
		
@RuleDecorator()		
def b(c=C_NONE, m=VOICEFULL):
	if default_mode.switch_simplification_b_p and m == VOICELESS:
		return p(c)
	else:
		return capitalize("b", c)
	
@RuleDecorator()		
def bb():
	return double_consonant("b")
	
@RuleDecorator()		
def c(c=C_NONE, m=C_K):
	if default_mode.switch_simplification_c_kz:
		if m == C_K:
			return k(c)
		elif m == C_S:
			return s(c)
		elif m == C_TSCH:
			return tsch(c)
		else:
			return z(c)
	else:
		return capitalize("c", c)
		
@RuleDecorator()		
def ch(c=C_NONE, m=0):
	if default_mode.switch_simplification_ch_sch and m == CH_GREEK:
		return sch(c)
	elif default_mode.switch_simplification_ch_ck and m == CH_CK:
		return capitalize("c", c) + k()
	elif default_mode.switch_simplification_ch_k and m == CH_K:
		return k(c)
	else:
		return capitalize("c", c) + capitalize("h")
		
@RuleDecorator()		
def ck(c=C_NONE):
	if default_mode.switch_simplification_ck_kk:
		return double_consonant("k")
	else:
		return capitalize("c", c) + k()
		
@RuleDecorator()		
def d(c=C_NONE, m=VOICEFULL):
	if default_mode.switch_simplification_d_t and m == VOICELESS:
		return t(c)
	else:
		return capitalize("d", c)
		
@RuleDecorator()		
def dt(c=C_NONE, m=0):
	if default_mode.switch_simplification_dt_tt:
		if m == ACTUALLY_ELONGATED:
			return t(c)
		else:
			return tt()
	else:
		return d(c) + t()
		
@RuleDecorator()		
def e(c=C_NONE, m=0):
	if default_mode.switch_harmonization_homophony_elongated_vowels and (m & ACTUALLY_ELONGATED):
		return elongation(e, c, m & ~ACTUALLY_ELONGATED)
	elif default_mode.switch_misc_trema and (m & TREMA):
		return capitalize("ë", c)
	else:
		return capitalize("e", c)
		
@RuleDecorator()		
def ee(c=C_NONE):
	return elongation(e, c, ELONGATION_MODE_DOUBLE)
	
@RuleDecorator()		
def eh(c=C_NONE):
	return elongation(e, c, ELONGATION_MODE_H)
	
@RuleDecorator()		
def ei(c=C_NONE):
	if default_mode.switch_simplification_ei_ai:
		return a(c) + i()
	else:
		return e(c) + i()
		
@RuleDecorator()		
def er(c=C_NONE, m=UNSTRESSED):
	if default_mode.switch_simplification_er_a and (m == UNSTRESSED):
		return a(c)
	else:
		return e(c)+r()
		
@RuleDecorator()		
def eu(c=C_NONE):
	if default_mode.switch_simplification_eu_oi:
		return o(c) + i()
	else:
		return e(c) + u()
		
@RuleDecorator()		
def f(c=C_NONE):
	return capitalize("f", c)
	
@RuleDecorator()		
def ff():
	return double_consonant("f")
	
@RuleDecorator()		
def g(c=C_NONE):
	return capitalize("g", c)
	
@RuleDecorator()		
def h(c=C_NONE, m=0):
	if default_mode.switch_simplification_suppress_mute_h and m == MUTE:
		return ""
	else:
		return capitalize("h", c)
		
@RuleDecorator()		
def i(c=C_NONE, m=0):
	if default_mode.switch_misc_trema and (m & TREMA):
		return capitalize("ï", c)
	else:
		return capitalize("i", c)
		
@RuleDecorator()		
def ie(c=C_NONE):
	return elongation(i, c, ELONGATION_MODE_E)
	
@RuleDecorator()		
def ih(c=C_NONE):
	return elongation(i, c, ELONGATION_MODE_H)
	
@RuleDecorator()		
def j(c=C_NONE):
	return capitalize("j", c)
	
@RuleDecorator()		
def k(c=C_NONE):
	return capitalize("k", c)
	
@RuleDecorator()		
def l(c=C_NONE):
	return capitalize("l", c)
	
@RuleDecorator()		
def ll():
	return double_consonant("l")
	
@RuleDecorator()		
def m(c=C_NONE):
	return capitalize("m", c)
	
@RuleDecorator()		
def mm():
	return double_consonant("m")
	
@RuleDecorator()		
def n(c=C_NONE, m=0):
	if default_mode.switch_harmonization_homophony_terminating_consonants and (m == ACTUALLY_SHORT):
		return nn()
	else:
		return capitalize("n", c)
		
@RuleDecorator()		
def nn():
	return double_consonant("n")
	
@RuleDecorator()		
def o(c=C_NONE):
	return capitalize("o", c)
	
@RuleDecorator(p_pattern = 'ö')		
def ouml(c=C_NONE):
	if default_mode.switch_simplification_expand_umlaut:
		return capitalize("o", c) + capitalize("e")
	else:
		return capitalize("ö", c)
		
@RuleDecorator(p_pattern = 'öh')		
def oumlh(c=C_NONE):
	return elongation(ouml, c, ELONGATION_MODE_H)
	
@RuleDecorator()		
def p(c=C_NONE):
	return capitalize("p", c)
	
@RuleDecorator()		
def ph(c=C_NONE):
	if default_mode.switch_simplification_ph_f:
		return capitalize("f", c)
	else:
		return capitalize("p", c) + capitalize("h")
		
@RuleDecorator()		
def pp():
	return double_consonant("p")
	
@RuleDecorator()		
def qu(c=C_NONE):
	if default_mode.switch_simplification_qu_kw:
		return capitalize("k", c) + capitalize("w")
	else:
		return capitalize("q", c) + capitalize("u")
		
		
@RuleDecorator()		
def r(c=C_NONE):
	return capitalize("r", c)
	
@RuleDecorator()		
def s(c=C_NONE, m=0):
	if default_mode.switch_harmonization_homophony_terminating_consonants and (m == ACTUALLY_SHORT):
		return ss()
	else:
		return capitalize("s", c)
		
@RuleDecorator()		
def sp(c=C_NONE):
	if default_mode.switch_simplification_sch_s:
		return capitalize("š", c) + p()
	else:
		return s(c) + p()
		
@RuleDecorator()		
def ss(c=C_NONE):
	return double_consonant("s")
	
@RuleDecorator(p_pattern = 'ß')		
def sz(c=C_NONE, m=NEOW):
	if default_mode.switch_simplification_sz_ss or (m == EOW and not default_mode.switch_legacy_sz):
		return ss()
	else:
		return capitalize("ß", c)
		
@RuleDecorator()		
def sch(c=C_NONE):
	if default_mode.switch_simplification_sch_s:
		return capitalize("š", c)
	else:
		return s(c) + capitalize("c") + capitalize("h")
		
@RuleDecorator()		
def st(c=C_NONE):
	if default_mode.switch_simplification_sch_s:
		return capitalize("š", c) + t()
	else:
		return s(c) + t()
		
@RuleDecorator()		
def t(c=C_NONE, m=0):
	if default_mode.switch_harmonization_homophony_terminating_consonants and (m == ACTUALLY_SHORT):
		return tt()
	else:
		return capitalize("t", c)
		
@RuleDecorator()		
def tion(c=C_NONE):
	if default_mode.switch_simplification_tion_zion:
		return z(c)+i()+o()+n()
	else:
		return t(c)+i()+o()+n()
		
@RuleDecorator()		
def tsch(c=C_NONE):
	if default_mode.switch_simplification_tsch_c:
		return capitalize("č", c)
	else:
		return t(c) + sch()
		
@RuleDecorator()		
def th(c=C_NONE):
	if default_mode.switch_simplification_th_t:
		return capitalize("t", c)
	else:
		return capitalize("t", c) + capitalize("h")
		
@RuleDecorator()		
def tt():
	return double_consonant("t")
	
@RuleDecorator()		
def u(c=C_NONE):
	return capitalize("u", c)
	
@RuleDecorator(p_pattern = 'ü')		
def uuml(c=C_NONE):
	if default_mode.switch_simplification_expand_umlaut:
		return u(c) + e()
	else:
		return capitalize("ü", c)
		
@RuleDecorator(p_pattern = 'üh')		
def uumlh(c=C_NONE):
	return elongation(uuml, c, ELONGATION_MODE_H)
	
@RuleDecorator()		
def v(c=C_NONE, m=VOICELESS):
	if default_mode.switch_simplification_v_fw:
		if m == VOICELESS:
			return f(c)
		else:
			return w(c)
	else:
		return capitalize("v", c)
		
@RuleDecorator()		
def w(c=C_NONE):
	return capitalize("w", c)
	
@RuleDecorator()		
def x(c=C_NONE):
	if default_mode.switch_simplification_x_ks:
		return k(c) + s()
	else:
		return capitalize("x")
		
		
@RuleDecorator()		
def y(c=C_NONE, m=Y_UE):
	if default_mode.switch_simplification_y_uej:
		if m == Y_UE:
			return uuml(c)
		elif m == Y_I:
			return i(c)
		else:
			return j(c)
	else:
		return capitalize("y", c)
		
@RuleDecorator()		
def z(c=C_NONE):
	if default_mode.switch_simplification_z_ts:
		return t(c) + s()
	else:
		return capitalize("z", c)

