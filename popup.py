# coding: utf-8

import ui

import ui_util
import rulesets

reload(ui_util)
reload(rulesets)

from rulesets import *

DEFAULT_TITLE = 'Zusätzliche Info'
DEFAULT_BUTTON_LABEL = 'Schließen'

class popup_view_controller ( ui_util.view_controller ) :

  def __init__(self):
    
    #ui_util.view_controller.__init__(self, None)
    super(popup_view_controller, self).__init__(None)
    self.load('popup')
    self.info_text_view = self.view['textview_info_text']
    self.button_view = self.view['button_close']
    
    
  def handle_action(self, sender):
    
    if sender.name == 'button_close':
      
      self.view.close()
      
    else:
      print "WARNING: action '%s' not handled!" % sender.name
    return 0
    
  def show_info(self, info, mode = 'popover', title=DEFAULT_TITLE, button_label=DEFAULT_BUTTON_LABEL):
    
    self.info_text_view.text = info
    #self.view.Header = title
    self.button_view.title = button_label
    self.present(mode)
    
def test():
  
  my_popup = popup_view_controller()
  
  my_popup.show_info("Hallo!")    
    
if __name__ == '__main__':
  test()
