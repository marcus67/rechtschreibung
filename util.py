#coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import difflib
import string
import six

PARAMETER_RUNNING_ON_TARGET_DEVICE = "--target-device"

DIFF_INSERT = u'i'
DIFF_DELETE = u'd'
DIFF_CHANGE = u'c'
DIFF_NONE = u' '

def compute_bit_value(state, old_value, state_bit):
	if state != bool(old_value & state_bit):
		return old_value ^ state_bit
	else:
		return old_value
		
def count_bits(value):
	count = 0
	
	while value > 0:
		if value & 1 > 0:
			count = count + 1
			
		value = value >> 1
		
	return count
		
def set_container_value(container, name, value):
	if getattr(container, name, None) != None:
		setattr(container, name, value)
		
	else:
		print ("ERROR: name '%s' not found in container '%s'" % (name, type(container).__name__))
		
def get_change_control_strings(oldString, newString):

	enhancedString = oldString # .encode("utf-8" )
	controlString = ( u" " * len(enhancedString) ) #.encode( "utf-8" )
	
	for i,s in enumerate(difflib.ndiff(oldString, newString)):
		if s[0] == u' ':
			continue
			
		elif s[0] == u'-':
			controlString = controlString[0:i] + DIFF_DELETE + controlString[i+1:]
			
		elif s[0] == u'+':
			enhancedString = enhancedString[0:i] + s[-1] + enhancedString[i:]
			controlString = controlString[0:i] + DIFF_INSERT + controlString[i:]
			
	return ( enhancedString, controlString )
	
	
def get_multi_token_change_control_strings(oldString, newString):

	oldTokens = oldString.split(u' ')
	newTokens = newString.split(u' ')
	if len(oldTokens) == len(newTokens):
		enhancedString = u''
		controlString = u''
		i = 0
		for oldToken in oldTokens:
			enhancedToken, tokenControlString = get_change_control_strings(oldToken,newTokens[i])
			if len(enhancedString) > 0:
				enhancedString = enhancedString + u' '
				controlString = controlString + u' '
			enhancedString = enhancedString + enhancedToken
			controlString = controlString + tokenControlString
			i = i + 1
		return (enhancedString, controlString)
	else:
		return get_change_control_strings(oldString, newString)
		
def get_html_content(oldString, newString, show_changes):

	if oldString and show_changes:
	
		enhancedNewString, controlString = get_multi_token_change_control_strings(oldString, newString)
		
		newString = u''
		i = 0
		
		for c in controlString:
			#print i, c
			if c == DIFF_NONE:
				newString = newString + enhancedNewString[i]
			elif c == DIFF_INSERT:
				newString = newString + u"<span id='ins'>" + enhancedNewString[i] + u'</span>'
			elif c == DIFF_DELETE:
				newString = newString + u"<span id='del'>" + enhancedNewString[i] + u'</span>'
			i = i + 1
			
	# do some final replacements:
	# -) replace the surrogate characters used for those not found on the Apple keyboard by their HTML codes
	# -) replace the double quote character '"' bei &quot; so that the resultsing string can be used in JS.
	return newString.replace(
		u"\n",u"<BR/>").replace(u"ė",u"&#275;").replace(u"Ė",u"&#274;").replace(u'"',u'&quot;')
	
	
def add_missing_attributes(object, template):

	changes = 0
	for attr in template.__dict__:
		if not attr in object.__dict__:
			setattr(object, attr, getattr(template, attr))
			changes = changes + 1
	return changes
	
def count_differences_in_dicts(dict1, dict2):
	common_keys = set(dict1.keys()).intersection(dict2.keys())
	return sum([1 if dict1[key] != dict2[key] else 0 for key in common_keys])
	
def is_running_on_target_device():
	return PARAMETER_RUNNING_ON_TARGET_DEVICE in sys.argv
