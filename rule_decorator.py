#coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

# Constants for OR'ing a condition holding for the current pattern being tested
COND_NONE = 0
COND_BOS = 1          # beginning of sentence
COND_BOW = 2          # beginning of word
COND_EOW = 4          # end of word
COND_EOS = 8          # end of sentence
COND_CAPITALIZED = 16 # compare string for pattern starts with a capital letter

COND_SEPERATED_WORD = COND_BOW | COND_EOW

global g_rules

g_rules = {}

def get_rules():
	global g_rules
	
	return sorted(g_rules.values(), key = lambda r:r.sort_key())

class Rule (object):
	
	def __init__(
			self, p_pattern, p_name, 
			p_seperates_words = False, p_conditions = COND_NONE,
			p_check_voicefullness = False):		
		self.pattern = p_pattern
		self.name = p_name
		self.condition = p_conditions
		self.seperates_words = p_seperates_words
		self.check_voicefullness = p_check_voicefullness
		
	def sort_key(self):
		return ( -len(self.pattern), self.pattern )
		
	def build_string(self, p_cond):
		
		params = []
		
		if p_cond & COND_BOS > 0:
			params.append(u"c=C_BOS")
		elif p_cond & COND_BOW > 0 and p_cond & COND_CAPITALIZED > 0 and not self.seperates_words:
			params.append(u"c=C_NOUN")
		if self.check_voicefullness and p_cond & COND_EOW > 0:
			params.append(u"m=VOICELESS")
		
		param_string = u", ".join(params)
		return u"%s(%s)" % ( self.name, param_string )
		
	def __str__(self):
		return u"rule '%s' for pattern '%s'" % ( self.name, self.pattern )
		
class RuleDecorator(object):
	
	def __init__(
			self, p_pattern = None, 
			p_seperates_words = False, p_conditions = COND_NONE,
			p_check_voicefullness = False,):	
		self._pattern = p_pattern
		self._seperates_words = p_seperates_words
		self._conditions = p_conditions
		self._check_voicefullness = p_check_voicefullness
		
	def __call__(self, f):
		global g_rules
		
		rulename = f.__name__
		
		if rulename not in g_rules:
			if self._pattern is not None:
				pattern = self._pattern
				
			else:
				pattern = rulename
				
			rule = Rule(
				p_pattern = pattern, 
				p_name = rulename, 
				p_seperates_words = self._seperates_words,
				p_conditions = self._conditions,
				p_check_voicefullness = self._check_voicefullness)
			g_rules[rulename] = rule
			
		# return the original function without modification
		return f

