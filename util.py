#coding: utf-8
import difflib
import string

DIFF_INSERT = u'i'
DIFF_DELETE = u'd'
DIFF_CHANGE = u'c'
DIFF_NONE = u' '

def compute_bit_value(state, old_value, state_bit):
  if state != bool(old_value & state_bit):
    return old_value ^ state_bit
  else:
    return old_value
          
def set_container_value(container, name, value):
  if getattr(container, name, None) != None:
    setattr(container, name, value)
  else:
    print "ERROR: name '%s' not found in container '%s'" % (name, type(container).__name__)
    
    
def get_style_sheet():
  return '''
<style>
html {
      font-size: 120%;
}
span#ins {
    background-color: #C8FFD1;
}

span#del {
    background-color: #C0C0C0; text-decoration: line-through;
}

span#ch {
    bg-color: yellow;
}  
</style>
'''

def get_change_control_strings(oldString, newString):

    enhancedString = unicode( oldString )
    controlString = unicode( " " * len(enhancedString) )
    
    for i,s in enumerate(difflib.ndiff(unicode(oldString), unicode(newString))):
      if s[0]==' ': 
        continue
        
      elif s[0]=='-':
        controlString = controlString[0:i] + DIFF_DELETE + controlString[i+1:]
        
      elif s[0]=='+':
        enhancedString = enhancedString[0:i] + unicode( s[-1] ) + enhancedString[i:]
        controlString = controlString[0:i] + DIFF_INSERT + controlString[i:]

    return ( enhancedString, controlString )    
  
  
def get_multi_token_change_control_strings(oldString, newString):
  
  oldTokens = string.split(oldString, ' ')
  newTokens = string.split(newString, ' ')
  if len(oldTokens) == len(newTokens):
    enhancedString = ''
    controlString = ''
    i = 0
    for oldToken in oldTokens:
      enhancedToken, tokenControlString = get_change_control_strings(oldToken,newTokens[i])
      if len(enhancedString) > 0:
        enhancedString = enhancedString + ' '
        controlString = controlString + ' '  
      enhancedString = enhancedString + enhancedToken
      controlString = controlString + tokenControlString
      i = i + 1
    return (enhancedString, controlString)
  else:  
    return get_change_control_strings(oldString, newString)  
  
def get_html_body(oldString, newString, show_changes):
  
  if oldString and show_changes:
    
    enhancedNewString, controlString = get_multi_token_change_control_strings(oldString, newString)
    
    #print enhancedNewString
    #print controlString
    
    newString = u''
    i = 0
    
    for c in controlString:
      #print i, c
      if c == DIFF_NONE:
        newString = newString + enhancedNewString[i]
      elif c == DIFF_INSERT:
        newString = newString + '<span id="ins">' + enhancedNewString[i] + '</span>'
      elif c == DIFF_DELETE:
        newString = newString + '<span id="del">' + enhancedNewString[i] + '</span>'
      i = i + 1
  
  # '<link rel="stylesheet" type="text/css" href="file:styles.css">'
  # get_style_sheet()
  return '<html>' + get_style_sheet() + '<body>' + newString.replace("\n","<BR/>") + "</body></html>"
  
  
def add_missing_attributes(object, template):
  
  changes = 0
  for attr in template.__dict__:
    if not attr in object.__dict__:
      setattr(object, attr, getattr(template, attr))
      changes = changes + 1
  return changes
  
def test():
  print get_html_body("Zwei šBären","Eine Bäršin", True)
  
if __name__ == '__main__':
  test()
