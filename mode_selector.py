# coding: utf-8

import ui
import log

import ui_util
import predefined_modes

reload(ui_util)
reload(predefined_modes)

global logger
logger = log.open_logging()

class MyTableViewDelegate (object):
  
  def __init__(self, parent_view_controller):
    
    self.parent_view_controller = parent_view_controller
    
  def tableview_did_select(self, tableview, section, row):
    # Called when a row was selected.
    print "SELECT!"
    pass

  def tableview_did_deselect(self, tableview, section, row):
    # Called when a row was de-selected (in multiple selection mode).
    pass

  def tableview_title_for_delete_button(self, tableview, section, row):
    # Return the title for the 'swipe-to-***' button.
    return 'Delete'

  def tableview_accessory_button_tapped(self, tableview, section, row):
    
    global logger
    print "hallo!"
    logger.debug("tableview_accessory_button_tapped: tableview='%s' row='%s'" % ( str(tableview), str(row) ))


class spelling_mode_selector(ui_util.view_controller):
  
  def __init__(self, parent_vc=None):
    
    super(spelling_mode_selector, self).__init__(parent_vc)
#    ui_util.view_controller.__init__(self, parent_vc)

    self.selectedIndex = None
    self.load('mode_selector')
         
  def get_selected_mode(self):
    
    if self.selectedIndex == None:
      return None
    else:
      return self.modes[self.selectedIndex]

  def is_my_action(self, sender):
    
    return sender == self
    
  def select(self, modes):

    global logger
        
    self.modes = modes
    items = []

    for mode in modes:
     
      logger.debug("add mode '%s' to list" % mode.name)
      entryMap = { 'title' : mode.name }
      if mode.isImmutable: 
        entryMap['image'] = 'ionicons-ios7-locked-outline-32'
        logger.debug("add image for mode '%s'" % mode.name)
      if len(mode.comment) > 0:
        entryMap['accessory_type'] = 'detail_button'
        logger.debug("add accessory for mode '%s'" % mode.name)
        
      
      items.append(entryMap)
      
    self.listDataSource = ui.ListDataSource(items)
    #self.listDataSource.delegate = MyTableViewDelegate(self)
    self.listDataSource.tableview_accessory_button_tapped = lambda tableview, section, row:self.tableview_accessory_button_tapped(row)
    self.selectedIndex = None
    self.view['tableview_spelling_mode_selector'].data_source = self.listDataSource

    self.present()
    
    if not self.parent_view:
      self.view.wait_modal()
    
    
  def tableview_accessory_button_tapped(self, row):
    
    print str(row)
    
  def handle_action(self, sender):
    
    global logger
    
    close = False
    if type(sender).__name__ == 'ListDataSource':
      self.selectedIndex = sender.selected_row
      logger.debug("handle_action from ListDataSource: selectedIndex=%d" % self.selectedIndex)
      close = True
        
    elif sender.name == 'button_cancel':
      logger.debug("handle_action from cancel button")
      close =True
      
    if close:
      self.view.close()
      if self.parent_view:
        self.parent_view.handle_action(self)

    
def test():
  
  global logger
  
  logger.info("Test started")
  selector = spelling_mode_selector()
  
  selector.select(predefined_modes.get_predefined_modes())
  result = selector.get_selected_mode()
  
  if result:
    logger.info("selected_mode='%s'" % result.name)
  else:
    logger.info("selection cancelled")
  logger.info("Test finished")
    
if __name__ == '__main__':
  test()
    
    
    
