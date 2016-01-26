# coding: utf-8

import ui

import log
import defaults
import ui_util
import popup
import predefined_modes
import spelling_mode

reload(log)
reload(defaults)
reload(ui_util)
reload(popup)
reload(predefined_modes)
reload(spelling_mode)

global logger
logger = log.open_logging(__name__)

class SpellingModeSelector(ui_util.ViewController):
  
  def __init__(self, parent_vc=None):
    
    super(SpellingModeSelector, self).__init__(parent_vc)
    self.selected_index = None
    self.popup_vc = None
    self.load('mode_selector')
         
  def get_selected_mode(self):
    
    if self.selected_index == None:
      return None
      
    else:
      return self.modes[self.selected_index]

  def is_my_action(self, sender):
    
    return sender == self
    
  def select(self, modes, cancel_label=defaults.DEFAULT_CANCEL_LABEL, close_label=defaults.DEFAULT_CLOSE_LABEL, style='sheet'):

    global logger
        
    self.modes = sorted(modes, spelling_mode.compare_spelling_modes)
    self.cancel_label = cancel_label
    self.close_label = close_label
    
    items = []

    for mode in self.modes:
     
      logger.debug("add mode '%s' to list" % mode.name)
      entryMap = { 'title' : mode.name }

      if mode.isImmutable: 
        entryMap['image'] = 'ionicons-ios7-locked-32'
      else:
        entryMap['image'] = 'ionicons-ios7-unlocked-outline-32'
        
      if len(mode.comment) > 0:
        entryMap['accessory_type'] = 'detail_button'
        logger.debug("add accessory for mode '%s'" % mode.name)
        
      items.append(entryMap)
        
    self.list_data_source = ui.ListDataSource(items)
    self.list_data_source.highlight_color = defaults.COLOR_LIGHT_GREEN
#    self.list_data_source.tableview_accessory_button_tapped = lambda tableview, section, row:self.tableview_accessory_button_tapped(row)
    self.selected_index = None
    self.tableview_spelling_mode_selector = self.find_subview_by_name('tableview_spelling_mode_selector')
    self.tableview_spelling_mode_selector.data_source = self.list_data_source
    
    self.button_view_cancel = self.find_subview_by_name('button_cancel')
    self.button_view_cancel.title = self.cancel_label

    self.present(style)
    
    if not self.parent_view:
      self.view.wait_modal()
    
    
#  def tableview_accessory_button_tapped(self, row):
#    
#    print str(row)
    
  def handle_action(self, sender):
    
    global logger
    
    close = False
    if type(sender).__name__ == 'ListDataSource':
      self.selected_index = sender.selected_row
      logger.debug("handle_action from ListDataSource: selected_index=%d" % self.selected_index)
      close = True
        
    elif sender.name == 'button_cancel':
      logger.debug("handle_action from cancel button")
      close =True
      
    if close:
      self.view.close()
      if self.parent_view:
        self.parent_view.handle_action(self)
        
  def handle_accessory(self, sender):
    
    global logger
    
    logger.debug("handle_accessory row=%d" % sender.tapped_accessory_row)
    comment = self.modes[sender.tapped_accessory_row].comment
         
    if not self.popup_vc:
      self.popup_vc = popup.PopupViewController()

    self.popup_vc.present(comment, close_label=self.close_label)

    
def test():
  
  global logger
  
  logger.info("Test started")
  selector = SpellingModeSelector()
  
  selector.select(predefined_modes.get_predefined_modes())
  result = selector.get_selected_mode()
  
  if result:
    logger.info("selected_mode='%s'" % result.name)
  else:
    logger.info("selection cancelled")
  logger.info("Test finished")
    
if __name__ == '__main__':
  test()
    
    
    