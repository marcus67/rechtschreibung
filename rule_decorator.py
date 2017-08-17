#coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

global g_rules

g_rules = {}

def get_rules():
	
	global g_rules
	
	return sorted(g_rules.values(), key = lambda r:r.sort_key())

class RuleDecorator(object):
	
	def __init__(self, p_pattern = None):
		
		self._pattern = p_pattern
		
	def __call__(self, f):
		
		global g_rules
		
		rulename = f.__name__
		if rulename not in g_rules:
			if self._pattern is not None:
				pattern = self._pattern
			else:
				pattern = rulename
			rule = Rule(p_pattern = pattern, p_rulename = rulename)
			g_rules[rulename] = rule
			
		return f

class Rule (object):
	
	def __init__(self, p_pattern, p_rulename):		
		self._pattern = p_pattern
		self._rulename = p_rulename
		
	def sort_key(self):
		return ( -len(self._pattern), self._pattern )
		
	def __str__(self):
		return "rule '%s' for pattern '%s'" % ( self._rulename, self._pattern )
		

