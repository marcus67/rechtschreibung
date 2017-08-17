#coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import inspect
import importlib

import rule_decorator

RULE_MODULE_NAMES = ( 'rulesets', 'words')

SPECIAL_CHARS = [
	( ',', 'comma_sc()' ),
	( 'ä', 'auml()' ),
	( 'ü', 'uuml()' ),
	( 'ö', 'ouml()' ),
	( 'Ä', 'auml(c=)' ),
	( 'Ö', 'ouml(c=)' ),
	( 'Ü', 'uuml(c=)' ),
	( 'ß', 'sz()')
	]

def read_rules():
	
	rules = []
	for module_name in RULE_MODULE_NAMES:
		module = importlib.import_module(module_name)

def print_rules():
	for rule in rule_decorator.get_rules():
		print (str(rule))

def parse_string(p_string):
	pass

if __name__ == '__main__':
	read_rules()
	print_rules()
