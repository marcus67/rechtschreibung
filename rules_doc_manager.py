# coding: utf-8
import json

RULE_DOC_FILE = 'etc/rules.json'
MD_RULE_OVERVIEW_TEMPLATE_FILE = 'etc/rules_template.md'
MD_RULE_OVERVIEW_FILE = 'doc/rules.md'

TEMPLATE_TABLE_PATTERN = '[TABLE]'
TEMPLATE_NEWLINE_PATTERN = '<BR>'

class RulesDocManager(object):
  
  def __init__(self, rules_doc_file):
    self.repository = json.load(open(rules_doc_file))
    infos = filter(lambda entry : 'info' in entry, self.repository['rules'])
    self.infos_by_attr_name = dict( [ ( entry['attr'], entry['info'] ) for entry in infos])
    
  def generate_md_rule_overview(self, temlate_md_file, md_file):
    sorted_rules = sorted(self.repository['rules'], key=lambda entry : entry['type'] + entry['id'])
    lines = '\n'.join("\t<TR><TD>%s</TD><TD>%s</TD><TD>%s</TD></TR>" % (entry['type'], entry['id'], entry['desc']) for entry in sorted_rules)
    template = open(temlate_md_file).read()
    target = template.replace(TEMPLATE_TABLE_PATTERN, lines).replace(TEMPLATE_NEWLINE_PATTERN,'\n')
    with open(md_file, "w") as file:
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
  

