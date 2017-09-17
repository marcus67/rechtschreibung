#coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import inspect
import importlib
import words
import rulesets

import log
import rule_decorator
import util

global logger

def print_rules():
	for rule in rule_decorator.get_rules():
		print (str(rule))

def get_single_char_pattern_map(p_rules):
	global logger
	
	map = {}
	
	for rule in p_rules:
		if len(rule.pattern) == 1:
			existing_rule = map.get(rule.pattern)
			
			if existing_rule is not None and existing_rule.seperates_words != rule.seperates_words:
				fmt = "Pattern '%s' occors more than once! Ignoring %s." % ( rule.pattern, str(rule.name) )
				logger.warning(fmt)
				
			else:
				map[rule.pattern] = rule
				
	return map			
			
def parse_string(p_string):
	global logger
	
	s = p_string
	cond = rule_decorator.COND_BOS | rule_decorator.COND_BOW
	rules = rule_decorator.get_rules()
	single_char_pattern_map = get_single_char_pattern_map(rules)
	result = []
	
	while len(s) > 0:
		
		best_rule = None
		best_cond = None
		best_cond_count = -1
		last_pattern_length = None
		
		for rule in rules:
			current_pattern_length = len(rule.pattern)
			
			if current_pattern_length <= len(s):
			
				temp_cond = rule_decorator.COND_NONE
				if last_pattern_length is None or last_pattern_length != current_pattern_length:
					
					if best_rule is not None and last_pattern_length is not None:
						break
					
					if len(s) == current_pattern_length:
						temp_cond = temp_cond | rule_decorator.COND_EOS
						
					else:
						next_char = rulesets.to_lower(s[current_pattern_length])
						next_char_rule = single_char_pattern_map.get(next_char)
						
						if next_char_rule is None:
							fmt = "Character '%s' not found as pattern!" % next_char
							logger.warn(fmt)
							
						elif next_char_rule.seperates_words:
							temp_cond = temp_cond | rule_decorator.COND_EOW
					
				temp_cond = temp_cond | cond
				
				compare_s = s[0:current_pattern_length]
				first_letter = compare_s[0]
				
				if (rulesets.to_upper(first_letter) == first_letter and 
						rulesets.to_upper(first_letter) != rulesets.to_lower(first_letter)):
					temp_cond = temp_cond | rule_decorator.COND_CAPITALIZED
				
				compare_s = rulesets.string_to_lower(compare_s)
				
				logger.debug("compare %s to %s demanding %d with current condition %d" % (
					 compare_s, rule.pattern, rule.condition, temp_cond))
				
				condition_count = util.count_bits(rule.condition)
				if (compare_s == rule.pattern and 
						(rule.condition & temp_cond) == rule.condition and
						condition_count > best_cond_count):
					best_rule = rule
					best_cond = temp_cond
					best_cond_count = condition_count
		
		if best_rule is None:
			fmt = "No rule found for remaining string '%s'" % s
			logger.error(fmt)
			break
		
		else:
			result.append(best_rule.build_string(best_cond))	
						
			if best_rule.seperates_words:
				cond = cond | rule_decorator.COND_BOW
			
			else:
				cond = cond & ~rule_decorator.COND_BOW
								
			s = s[len(best_rule.pattern):]
		
		cond = cond & ~ rule_decorator.COND_BOS
		last_pattern_length = current_pattern_length
		
	return u"+".join(result)
	
def setup_logging():
	global logger
	
	logger = log.open_logging('parser', reload=True)	

def main():
	global logger
	
	setup_logging()
	logger.info("Start parser")
	sentence = input("Enter sentence:")
	print (parse_string(sentence))
	logger.info("End parser")
	
if __name__ == '__main__':
	main()
	
