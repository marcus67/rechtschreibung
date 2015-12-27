#coding: utf-8
import spelling_mode

reload(spelling_mode)

def get_predefined_modes():
  
  modes = []
    
  mode = spelling_mode.spelling_mode()
  mode.name = u"Vor Rechtschreibreform"
  mode.comment = "Rechtschreibregeln wie sie vor der Reform am XXXXX gültig waren."
  mode.isImmutable = True
  mode.switch_legacy_sz = True
  modes.append(mode)

  mode = spelling_mode.spelling_mode()
  mode.name = u"Aktuelle Rechtschreibung"
  mode.isImmutable = True
  mode.isReference = True
  modes.append(mode)

  return modes

