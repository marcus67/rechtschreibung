# coding: utf-8

import ui
import console
import log
import copy

import ui_util
import spelling_mode
import mode_manager

reload(ui_util)
reload(spelling_mode)
reload(mode_manager)

global logger
logger = log.open_logging()

class spelling_mode_saver(ui_util.view_controller):
  
  def __init__(self, parent_vc=None):
    
    ui_util.view_controller.__init__(self, parent_vc)

    self.selectedIndex = None
    self.load('mode_saver')
         
  def is_my_action(self, sender):
    
    return sender == self
    
  def select(self, modes, currentMode):

    global logger
        
    self.currentMode = copy.copy(currentMode)
    self.modes = modes
    items = []

    for mode in modes:
      
      logger.debug("add mode '%s' to list" % mode.name)
      entryMap = { 'title' : mode.name }

      if len(mode.comment) > 0:
        entryMap['accessory_type'] = 'detail_button'
        logger.debug("add accessory for mode '%s'" % mode.name)
              
      items.append(entryMap)
      
    self.listDataSource = ui.ListDataSource(items)
    self.view['tableview_mode_selector'].data_source = self.listDataSource
    
    self.set_model(self.currentMode)

    self.present()
    
    if not self.parent_view:
      self.view.wait_modal()
      
  def get_selected_mode(self):
    
    return self.currentMode
        
  def handle_action(self, sender):
    
    global logger
    
    close = False
    save = False
    if type(sender).__name__ == 'ListDataSource':
      self.selectedIndex = sender.selected_row
      logger.debug("handle_action from ListDataSource: selectedIndex=%d" % self.selectedIndex)
      
      self.fill_model(self.modes[self.selectedIndex])
              
    elif sender.name == 'button_cancel':
      logger.debug("handle_action from cancel button")
      self.currentMode = None
      close =True
      
    elif sender.name == 'button_save':
      logger.debug("handle_action from save button")
      
      view = self.find_subview_by_name('textview_comment')
      self.currentMode.comment = view.text
      view = self.find_subview_by_name('textfield_mode_name')
      self.currentMode.name = view.text
      
      found = False
      for mode in self.modes:
        
        if mode.name == self.currentMode.name:
          found = True
          
      if found:
        
        try:
          
          pass
          close = True
          #result = console.alert("Bitte bestätigen", "Existierenden Regelsatz ersetzen?", button1="Überschreiben")
        
        except KeyboardInterrupt as i:
          
          pass

      else:
        
        close = True
    

    if close:
      self.view.close()
      if self.parent_view:
        self.parent_view.handle_action(self)

  def fill_model(self, mode):
    
    view = self.find_subview_by_name('textview_comment')
    view.text = mode.comment
    view = self.find_subview_by_name('textfield_mode_name')
    view.text = mode.name
    index = 0
    found = False
    for aMode in self.modes:
        
      if mode.name == self.aMode.name:
          found = True
          break
      index = index + 1
          
    if found:
      view = self.find_subview_by_name('tableview_mode_selector')
      view.selectedIndex = index
    
def test():
  
  global logger
  
  logger.info("Test started")
  saver = spelling_mode_saver()
  
  currentMode = spelling_mode.spelling_mode()
  saver.select(mode_manager.get_available_modes(False), currentMode)
  result = saver.get_selected_mode()
  
  if result:
    logger.info("selected_mode='%s' comment='%s'" % (result.name, result.comment))
  else:
    logger.info("selection cancelled")
  logger.info("Test finished")
    
if __name__ == '__main__':
  test()
    
    
    
