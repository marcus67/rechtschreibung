# coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import json
import codecs

RULE_DOC_FILE = 'etc/rules.json'
MD_RULE_OVERVIEW_TEMPLATE_FILE = 'etc/rules_template.html'
MD_RULE_OVERVIEW_FILE = 'doc/rules.html'

TEMPLATE_TABLE_PATTERN = '[TABLE]'
TEMPLATE_NEWLINE_PATTERN = '<BR>'

class RulesDocManager(object):

	def __init__(self, rules_doc_file):
		self.repository = json.load(codecs.open(rules_doc_file, "r", encoding="utf-8"))
		infos = filter(lambda entry : 'info' in entry, self.repository['rules'])
		self.infos_by_attr_name = dict( [ ( entry['attr'], entry['info'] ) for entry in infos])
		
	def generate_md_rule_overview(self, temlate_md_file, md_file):
		sorted_rules = sorted(self.repository['rules'], key=lambda entry : entry['type'] + entry['id'])
		lines = '\n'.join("\t<TR><TD>%s</TD><TD>%s</TD><TD>%s</TD><TD>%s</TD></TR>" % (entry['type'], entry['id'], entry['desc'], entry['info'] if 'info' in entry else '') for entry in sorted_rules)
		template = open(temlate_md_file, encoding="utf-8").read()
		target = template.replace(TEMPLATE_TABLE_PATTERN, lines).replace(TEMPLATE_NEWLINE_PATTERN,'\n')
		with open(md_file, "w", encoding="utf-8") as file:
			file.write(target)
			
	def get_rule_info_by_attr_name(self, attr):
		if attr in self.infos_by_attr_name:
			return self.infos_by_attr_name[attr].replace(TEMPLATE_NEWLINE_PATTERN,'\n')
		else:
			return None
			
def test():
	manager = RulesDocManager(RULE_DOC_FILE)
	manager.generate_md_rule_overview(MD_RULE_OVERVIEW_TEMPLATE_FILE, MD_RULE_OVERVIEW_FILE)
	
if __name__ == '__main__':
	test()

