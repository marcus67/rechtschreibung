# coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import six

import spelling_mode
from rule_decorator import *

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
	if l == u'ü':
		return u'Ü'
	elif l == u'ä':
		return u'Ä'
	elif l == u'ö':
		return u'Ö'
	elif l == u'š':
		return u'Š'
	elif l == u'č':
		return u'Č'
	elif l == u'ā':
		return u'Ā'
	elif l == u'ė':
		return u'Ė'
	elif l == u'ī':
		return u'Ī'
	elif l == u'ō':
		return u'Ō'
	elif l == u'ū':
		return u'Ū'
	elif l == u'ß':
		return u'ß'
	else:
		return l.upper()


def to_lower(l):
	if l == u'Ü':
		return u'ü'
	elif l == u'Ä':
		return u'ä'
	elif l == u'Ö':
		return u'ö'
	elif l == u'Š':
		return u'š'
	elif l == u'Č':
		return u'č'
	elif l == u'Ā':
		return u'ā'
	elif l == u'Ė':
		return u'ė'
	elif l == u'Ī':
		return u'ī'
	elif l == u'Ō':
		return u'ō'
	elif l == u'Ū':
		return u'ū'
	elif l == u'ß':
		return u'ß'
	else:
		return l.lower()


def string_to_lower(s):
	return u"".join([to_lower(c) for c in s])
	
		
def capitalize(l, c=C_NONE):
	if (default_mode.switch_capitalization_all_capital or
				(c & default_mode.bitswitch_capitalization)):
		if l == u'ß':
			if default_mode.switch_capitalization_expand_sz:
				return u'SS'
			else:
				return u'ß'
		else:
			return to_upper(l)
	else:
		return l

				
def para():
	if default_mode.switch_layout_paragraph_separation:
		return u"\n"
	else:
		return space()


def double_consonant(l):
	if default_mode.switch_simplification_double_consonants:
		return capitalize(l)
	else:
		return capitalize(l+l)

				
def elongation(l, c, m):
	default_elongation_mode = m & ELONGATION_MODE_MASK
	current_mode = default_mode.segmented_control_harmonization_elongation
	if (current_mode == ELONGATION_MODE_NONE or
				(current_mode == ELONGATION_MODE_DEFAULT and
					default_elongation_mode == ELONGATION_MODE_NONE)):
		return l(c)
		
	elif (current_mode == ELONGATION_MODE_E or
					(current_mode == ELONGATION_MODE_DEFAULT and
						default_elongation_mode == ELONGATION_MODE_E)):
		return l(c) + capitalize(u"e")
		
	elif (current_mode == ELONGATION_MODE_H or
					(current_mode == ELONGATION_MODE_DEFAULT and
						default_elongation_mode == ELONGATION_MODE_H)):
		return l(c) + capitalize(u"h")
		
	elif (current_mode == ELONGATION_MODE_MACRON or
					(current_mode == ELONGATION_MODE_DEFAULT and
						default_elongation_mode == ELONGATION_MODE_MACRON)):
		if (l == a):
			return capitalize(u"ā", c=c)
		elif (l == e):
			return capitalize(u"ė", c=c)
		elif (l == i):
			return capitalize(u"ī", c=c)
		elif (l == o):
			return capitalize(u"ō", c=c)
		elif (l == u):
			return capitalize(u"ū", c=c)
		else:
			return l(c) + l()
			
	else:
		return l(c) + l()
				

@RuleDecorator(p_pattern=u" ", p_seperates_words=True)
def space(c=C_NONE):
	if default_mode.switch_layout_word_separation:
		return u" "
	else:
		return u""


@RuleDecorator(p_pattern=u".", p_seperates_words=True, p_conditions=COND_EOS)
def fs():
	if default_mode.switch_punctuation_full_stop:
		return u"."
	else:
		return u""


@RuleDecorator(p_pattern=u",", p_seperates_words=True)
def comma_sc():
	if default_mode.switch_punctuation_comma_sub_clause:
		return u","
	else:
		return u""

				
@RuleDecorator(p_pattern=u":", p_seperates_words=True)
def colon():
	if default_mode.switch_punctuation_colon:
		return u":"
	else:
		return u""
		

@RuleDecorator(p_pattern=u".", p_seperates_words=True)
def dot_abbr():
	if default_mode.switch_punctuation_dot_abbr:
		return u"."
	else:
		return u""

				
@RuleDecorator(p_pattern=u"-", p_seperates_words=True)
def hyphen():
	return u"-"
		

@RuleDecorator()
def a(c=C_NONE):
	return capitalize(u"a", c)
	

@RuleDecorator()
def aa(c=C_NONE):
	return elongation(a, c, ELONGATION_MODE_DOUBLE)
	

@RuleDecorator()
def ah(c=C_NONE):
	return elongation(a, c, ELONGATION_MODE_H)
	

@RuleDecorator()
def ai(c=C_NONE):
	return a(c) + i()
		

@RuleDecorator()
def au(c=C_NONE):
	return capitalize(u"a", c) + capitalize(u"u")


def _auml(c=C_NONE):
	return capitalize(u"ä", c)
	

@RuleDecorator(p_pattern=u'ä')
def auml(c=C_NONE, m=0):
	if default_mode.switch_simplification_expand_umlaut:
		return capitalize(u"a", c) + capitalize(u"e")
		
	else:
		if ((m & ACTUALLY_ELONGATED) > 0 and
					default_mode.switch_harmonization_homophony_elongated_vowels):
			return elongation(_auml, c, m & ELONGATION_MODE_MASK)
			
		else:
			return _auml(c)


@RuleDecorator(p_pattern=u'äu')
def aumlu(c=C_NONE):
	if default_mode.switch_simplification_aumlu_oi:
		return o(c) + i()
	else:
		return capitalize(u"ä", c) + u()
		

@RuleDecorator(p_check_voicefullness=True)
def b(c=C_NONE, m=VOICEFULL):
	if default_mode.switch_simplification_b_p and m == VOICELESS:
		return p(c)
	else:
		return capitalize(u"b", c)
	

@RuleDecorator()
def bb():
	return double_consonant(u"b")
	

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
		return capitalize(u"c", c)
		

@RuleDecorator()
def ch(c=C_NONE, m=0):
	if default_mode.switch_simplification_ch_sch and m == CH_GREEK:
		return sch(c)
	elif default_mode.switch_simplification_ch_ck and m == CH_CK:
		return capitalize(u"c", c) + k()
	elif default_mode.switch_simplification_ch_k and m == CH_K:
		return k(c)
	else:
		return capitalize(u"c", c) + capitalize(u"h")
		

@RuleDecorator()
def ck(c=C_NONE):
	if default_mode.switch_simplification_ck_kk:
		return double_consonant(u"k")
	else:
		return capitalize(u"c", c) + k()
		

@RuleDecorator(p_check_voicefullness=True)
def d(c=C_NONE, m=VOICEFULL):
	if default_mode.switch_simplification_d_t and m == VOICELESS:
		return t(c)
	else:
		return capitalize(u"d", c)
		

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
	if (default_mode.switch_harmonization_homophony_elongated_vowels and
				(m & ACTUALLY_ELONGATED)):
		return elongation(e, c, m & ~ACTUALLY_ELONGATED)

	elif default_mode.switch_misc_trema and (m & TREMA):
		return capitalize(u"ë", c)

	else:
		return capitalize(u"e", c)
		

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
	return capitalize(u"f", c)
	

@RuleDecorator()
def ff():
	return double_consonant(u"f")
	

@RuleDecorator()
def g(c=C_NONE):
	return capitalize(u"g", c)
	

@RuleDecorator()
def h(c=C_NONE, m=0):
	if default_mode.switch_simplification_suppress_mute_h and m == MUTE:
		return u""
		
	else:
		return capitalize(u"h", c)
		

@RuleDecorator()
def i(c=C_NONE, m=0):
	if default_mode.switch_misc_trema and (m & TREMA):
		return capitalize(u"ï", c)

	else:
		return capitalize(u"i", c)
		

@RuleDecorator()
def ie(c=C_NONE):
	return elongation(i, c, ELONGATION_MODE_E)
	

@RuleDecorator()
def ih(c=C_NONE):
	return elongation(i, c, ELONGATION_MODE_H)
	

@RuleDecorator()
def j(c=C_NONE):
	return capitalize(u"j", c)
	

@RuleDecorator()
def k(c=C_NONE):
	return capitalize(u"k", c)
	

@RuleDecorator()
def l(c=C_NONE):
	return capitalize(u"l", c)
	

@RuleDecorator()
def ll():
	return double_consonant(u"l")
	

@RuleDecorator()
def m(c=C_NONE):
	return capitalize(u"m", c)
	

@RuleDecorator()
def mm():
	return double_consonant(u"m")


@RuleDecorator()
def n(c=C_NONE, m=0):
	if (default_mode.switch_harmonization_homophony_terminating_consonants and
				(m == ACTUALLY_SHORT)):
		return nn()

	else:
		return capitalize(u"n", c)

				
@RuleDecorator()
def nn():
	return double_consonant(u"n")
	

@RuleDecorator()
def o(c=C_NONE):
	return capitalize(u"o", c)


@RuleDecorator()
def oi(c=C_NONE):
	if default_mode.switch_simplification_oi_oa:
		return o(c) + a()

	else:
		return o(c) + i()
		

@RuleDecorator(p_pattern=u'ö')
def ouml(c=C_NONE):
	if default_mode.switch_simplification_expand_umlaut:
		return capitalize(u"o", c) + capitalize(u"e")

	else:
		return capitalize(u"ö", c)
		

@RuleDecorator(p_pattern=u'öh')
def oumlh(c=C_NONE):
	return elongation(ouml, c, ELONGATION_MODE_H)
	

@RuleDecorator()
def p(c=C_NONE):
	return capitalize(u"p", c)


@RuleDecorator()
def ph(c=C_NONE):
	if default_mode.switch_simplification_ph_f:
		return capitalize(u"f", c)

	else:
		return capitalize(u"p", c) + capitalize(u"h")
		

@RuleDecorator()
def pp():
	return double_consonant(u"p")
	

@RuleDecorator()
def qu(c=C_NONE):
	if default_mode.switch_simplification_qu_kw:
		return capitalize(u"k", c) + capitalize(u"w")

	else:
		return capitalize(u"q", c) + capitalize(u"u")
		
		
@RuleDecorator()
def r(c=C_NONE):
	return capitalize(u"r", c)
	

@RuleDecorator()
def s(c=C_NONE, m=0):
	if (default_mode.switch_harmonization_homophony_terminating_consonants and
				(m == ACTUALLY_SHORT)):
		return ss()

	else:
		return capitalize(u"s", c)
		

@RuleDecorator()
def sp(c=C_NONE):
	if default_mode.switch_simplification_sch_s:
		return capitalize(u"š", c) + p()

	else:
		return s(c) + p()
		

@RuleDecorator()
def ss(c=C_NONE):
	return double_consonant(u"s")
	

@RuleDecorator(p_pattern=u'ß')
def sz(c=C_NONE, m=NEOW):
	if (default_mode.switch_simplification_sz_ss or
				(m == EOW and not default_mode.switch_legacy_sz)):
		return ss()

	else:
		return capitalize(u"ß", c)
		

@RuleDecorator()
def sch(c=C_NONE):
	if default_mode.switch_simplification_sch_s:
		return capitalize(u"š", c)

	else:
		return s(c) + capitalize(u"c") + capitalize(u"h")
		

@RuleDecorator()
def st(c=C_NONE):
	if default_mode.switch_simplification_sch_s:
		return capitalize(u"š", c) + t()

	else:
		return s(c) + t()

		
@RuleDecorator()
def t(c=C_NONE, m=0):
	if (default_mode.switch_harmonization_homophony_terminating_consonants and
				(m == ACTUALLY_SHORT)):
		return tt()

	else:
		return capitalize(u"t", c)


@RuleDecorator()
def tion(c=C_NONE):
	if default_mode.switch_simplification_tion_zion:
		return z(c)+i()+o()+n()

	else:
		return t(c)+i()+o()+n()


@RuleDecorator()
def tsch(c=C_NONE):
	if default_mode.switch_simplification_tsch_c:
		return capitalize(u"č", c)

	else:
		return t(c) + sch()


@RuleDecorator()
def th(c=C_NONE):
	if default_mode.switch_simplification_th_t:
		return capitalize(u"t", c)

	else:
		return capitalize(u"t", c) + capitalize(u"h")
		

@RuleDecorator()
def tt():
	return double_consonant(u"t")


@RuleDecorator()
def u(c=C_NONE):
	return capitalize(u"u", c)

		
@RuleDecorator(p_pattern=u'ü')
def uuml(c=C_NONE):
	if default_mode.switch_simplification_expand_umlaut:
		return u(c) + e()

	else:
		return capitalize(u"ü", c)
		

@RuleDecorator(p_pattern=u'üh')
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
		return capitalize(u"v", c)


@RuleDecorator()
def w(c=C_NONE):
	return capitalize(u"w", c)
	

@RuleDecorator()
def x(c=C_NONE):
	if default_mode.switch_simplification_x_ks:
		return k(c) + s()
	else:
		return capitalize(u"x")
		
		
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
		return capitalize(u"y", c)
		

@RuleDecorator()
def z(c=C_NONE):
	if default_mode.switch_simplification_z_ts:
		return t(c) + s()
	
	else:
		return capitalize(u"z", c)

