#coding: utf-8


#pycologne?

import string
import ui
import speech
import threading
import copy

import view_punctuation
import spelling_mode
import rulesets
import words
import sentences
import util
import ui_util
import sample_text
import popup
import infos
import log
import mode_manager
import mode_selector
import mode_saver

reload(ui_util)
reload(view_punctuation)
reload(spelling_mode)
reload(rulesets)
reload(words)
reload(sentences)
reload(util)
reload(sample_text)  
reload(popup)
reload(infos)
reload(log)
reload(mode_manager)
reload(mode_selector)
reload(mode_saver)

global logger

logger = log.open_logging()

HIGHLIGHT_OFF = 0
HIGHLIGHT_DELTA = 1
HIGHLIGHT_REFERENCE = 2

class main_view_controller ( ui_util.view_controller ) :

  def __init__(self):
    
    ui_util.view_controller.__init__(self)
    self.previousSampleText = None
    self.currentSampleText = None
    self.highlightingMode = HIGHLIGHT_DELTA
    self.autoHide = True
    self.autoHideSeconds = 3
    self.suppressShowChanges = False
    self.selectModeVC = mode_selector.spelling_mode_selector(self)
    self.selectModeForSaveVC = mode_saver.spelling_mode_saver(self)
    self.info_popup = popup.popup_view_controller()
    self.set_reference_mode(filter(lambda m:m.isReference, mode_manager.get_available_modes())[0])
    self.loadedMode = spelling_mode.spelling_mode()
    
  def handle_change_in_mode(self):
    self.previousSampleText = self.currentSampleText
    self.suppressShowChanges = False
    self.update_sample_text()

  def set_reference_mode(self, mode):
    
    self.referenceMode = mode
    tempStoreMode = rulesets.get_default_mode()
    rulesets.set_default_mode(self.referenceMode)
    self.referenceSampleText = sample_text.get_sample_text()
    rulesets.set_default_mode(tempStoreMode)
  
  def handle_action(self, sender):
    
    global logger
    
    BUTTON_PREFIX = 'button_'
    INFO_PREFIX = 'info_'
    
    #print "handle_action: %s" % sender.name
    
    if self.selectModeVC.is_my_action(sender):    
      self.load_mode_finish()  
    
    elif self.selectModeForSaveVC.is_my_action(sender):    
      self.save_mode_finish()  
      
    elif sender.name == 'button_start_speech':
      speech.say(sample_text.get_sample_text(), 'de', 0.15)
      
    elif sender.name == 'button_stop_speech':
      speech.stop()
    
    elif sender.name == 'button_load_mode':
      self.load_mode_start()
    
    elif sender.name == 'button_save_mode':
      self.save_mode_start()
    
    elif sender.name == 'segmented_control_highlighting_mode':
      self.highlightingMode = sender.selected_index
      self.update_sample_text()
    
    elif sender.name == 'switch_auto_hide':
      self.autoHide = sender.value

    elif sender.name.startswith(BUTTON_PREFIX):
      view_name = sender.name[len(BUTTON_PREFIX):]
      child_view = self.find_subview_by_name(view_name)
      #child_view = self.view['top_navigation_view'][view_name]
      if child_view != None:
        self.view['top_navigation_view'].push_view(child_view)
        return 1
      else:
        logger.warning("cannot find subview '%s" % view_name)
      
    elif sender.name.startswith(INFO_PREFIX):
      info_name = sender.name[len(INFO_PREFIX):]
      info_messages = infos.get_info_messages()
      if info_name in info_messages:
        self.info_popup.show_info(info_messages[info_name], button_label=words.schlieszen(c=rulesets.C_BOS))
      else:
        print "ERROR: cannot find info text for %s" % info_name
      
    elif ui_util.store_in_model(sender, self.model):
      self.handle_change_in_mode()
      return 1
      
    else:
      print "WARNING: action '%s' not handled!" % sender.name
      
    return 0
    
  def activate_hide_timer(self):
    #print "activate timer"
    self.hideTimer = threading.Timer(self.autoHideSeconds, lambda x:x.handle_hide_timer(), [ self ] )
    self.hideTimer.start()
    
  def handle_hide_timer(self):
    #print "in handle timer"
    self.suppressShowChanges = True
    self.update_sample_text()
    
  def update_sample_text(self):
    #print "update_sample_text"
      
    self.currentSampleText = sample_text.get_sample_text()
    webview = self.view['webview_text_view']
    if self.highlightingMode == HIGHLIGHT_DELTA:
      compareText = self.previousSampleText
    else:
      compareText = self.referenceSampleText
    html_text = util.get_html_body(compareText, self.currentSampleText, self.highlightingMode and not self.suppressShowChanges)
    webview.load_html(html_text)
    if self.autoHide and self.highlightingMode and not self.suppressShowChanges:
      self.activate_hide_timer()
    self.update_views()
    
  def update_views(self):
    
    global logger

    view = self.find_subview_by_name('segmented_control_highlighting_mode')
    view.selected_index = self.highlightingMode
    
    view = self.find_subview_by_name('textfield_reference_mode_name')
    view.enabled = False
    view.text = self.referenceMode.name
    
    view = self.find_subview_by_name('textfield_current_mode_name')
    view.enabled = False
    view.text = self.loadedMode.name
#    logger.info("loadedMode = %s" & str(self.loadedMode))
#    logger.info("model = %s" & str(model))
    if self.loadedMode == self.model:
      view.text_color = '#000000'
    else:
      view.text_color = '#A0A0A0'
    
  def load_mode_start(self):
    
    self.selectModeVC.select(mode_manager.get_available_modes())
    
    
  def load_mode_finish(self):
    
    selectedMode = self.selectModeVC.get_selected_mode()
    if selectedMode != None:
      logger.info("Set mode '%s'" % selectedMode.name)
      self.set_model(selectedMode)
      rulesets.set_default_mode(selectedMode)
      self.loadedMode = copy.copy(selectedMode)
      self.handle_change_in_mode()
    
  def save_mode_start(self):
    
    self.selectModeForSaveVC.select(mode_manager.get_available_modes(), self.model)
    
    
  def save_mode_finish(self):
    
    selectedMode = self.selectModeForSaveVC.get_selected_mode()
    if selectedMode != None:
      mode_manager.write_mode(selectedMode)
      self.loadedMode = copy.copy(selectedMode)
      self.handle_change_in_mode()

##### MAIN ######################
    
def main():
    
  default_mode = spelling_mode.spelling_mode()
  rulesets.set_default_mode(default_mode)
  
  my_main_view_controller = main_view_controller()
  my_main_view_controller.load('rechtschreibung')
  
  view = my_main_view_controller.find_subview_by_name('segmented_control_highlighting_mode')
  view.action = my_main_view_controller.handle_action
  

  view_controller_capitalization = ui_util.view_controller(my_main_view_controller)
  view_controller_capitalization.load('view_capitalization')
  
  view_controller_harmonization = ui_util.view_controller(my_main_view_controller)
  view_controller_harmonization.load('view_harmonization')
  view = my_main_view_controller.find_subview_by_name('segmented_control_harmonization_elongation')
  view.action = my_main_view_controller.handle_action
  
  view_controller_combinations_simplification = ui_util.view_controller(my_main_view_controller)
  view_controller_combinations_simplification.load('view_combinations_simplification')
  
  view_controller_punctuation = ui_util.view_controller(my_main_view_controller) 
  view_controller_punctuation.load('view_punctuation')
  
  view_controller_legacy = ui_util.view_controller(my_main_view_controller) 
  view_controller_legacy.load('view_legacy')
  
  view_controller_layout = ui_util.view_controller(my_main_view_controller) 
  view_controller_layout.load('view_layout')

  my_main_view_controller.set_model(default_mode)
  
  my_main_view_controller.update_sample_text()
  my_main_view_controller.present('fullscreen')
    
if __name__ == '__main__':
  main()

