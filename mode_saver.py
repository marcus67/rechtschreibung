# coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import ui
import console
import copy
import six

import log
import defaults
import ui_util
import spelling_mode
import mode_manager

if six.PY3:
	from importlib import reload
	
reload(log)
reload(defaults)
reload(ui_util)
reload(spelling_mode)
reload(mode_manager)

global logger
logger = log.open_logging(__name__)


class SpellingModeSaver(ui_util.ViewController):

	def __init__(self, parent_vc=None):
	
		super(SpellingModeSaver, self).__init__(parent_vc)
		self.load('mode_saver')
		
		self.text_field_mode_name = self.find_subview_by_name('textfield_mode_name')
		self.text_field_mode_name.delegate = ui_util.TextFieldDelegate(self, 'textfield_mode_name')
		self.text_field_mode_name.action = self.handle_action
		
		self.text_view_comment = self.find_subview_by_name('textview_comment')
		self.button_view_cancel = self.find_subview_by_name('button_cancel')
		self.button_view_save = self.find_subview_by_name('button_save')
		self.tableview_mode_selector = self.find_subview_by_name('tableview_mode_selector')
		
		self.selected_index = None
		self.listDataSource = None
		
	def is_my_action(self, sender):
	
		return sender == self
		
	def select(self, modes, current_mode, cancel_label='Abbrechen', save_label='Speichern', overwrite_label='Überschreiben', style='sheet'):
	
		global logger
		
		self.cancel_label = cancel_label
		self.save_label = save_label
		self.overwrite_label = overwrite_label
		self.current_mode = copy.copy(current_mode)
		self.modes = modes
		items = []
		
		for mode in modes:
		
			logger.debug("add mode '%s' to list" % mode.control.name)
			entry_map = { 'title' : mode.control.name }
			
			items.append(entry_map)
			
		self.list_data_source = ui.ListDataSource(items)
		self.list_data_source.highlight_color = defaults.COLOR_LIGHT_GREEN
		self.tableview_mode_selector.data_source = self.list_data_source
		
		self.set_model(self.current_mode.control)
		self.update_controls()
		
		self.present(style, orientations=('portrait', ))
		
		if not self.parent_vc:
			self.view.wait_modal()
			
	def get_selected_mode(self):
		return self.current_mode
		
	def handle_list_data_source_action(self, sender):
		self.selected_index = sender.selected_row
		self.fill_model(self.modes[self.selected_index])
		
	def handle_button_action(self, name, sender):
		if sender.name == 'button_cancel':
			self.current_mode = None
			
		elif sender.name == 'button_save':
			self.current_mode.control.comment = self.text_view_comment.text
			self.current_mode.control.name = self.text_field_mode_name.text
			
		else:
			super(SpellingModeSaver, self).handle_button_action(name, sender)
			
		self.view.close()
		self.handle_named_action('save_mode_finish')
		
	def handle_textfield_action(self, sender):
		if sender.name == 'textfield_mode_name' and sender.action == 'textfield_did_change':
			self.update_controls()
		else:
			super(SpellingModeSaver, self).handle_textfield_action(sender)
			
	def update_controls(self):
		index = 0
		found = False
		for aMode in self.modes:
		
			if self.text_field_mode_name.text == aMode.control.name:
				found = True
				break
			index = index + 1
			
		self.button_view_cancel.title = self.cancel_label
		
		if found:
			self.button_view_save.title = self.overwrite_label
			self.button_view_save.background_color = defaults.COLOR_LIGHT_RED
			self.list_data_source.selected_row = index
			
		else:
			self.button_view_save.title = self.save_label
			self.button_view_save.background_color = defaults.COLOR_GREY
			self.list_data_source.selected_row = -1
			
	def fill_model(self, mode):
		self.text_view_comment.text = mode.control.comment
		self.text_field_mode_name.text = mode.control.name
		self.update_controls()
		
		
def test():

	global logger
	
	logger.info("Test started")
	saver = SpellingModeSaver()
	
	current_mode = spelling_mode.spelling_mode()
	saver.select(mode_manager.get_available_modes(False), current_mode)
	result = saver.get_selected_mode()
	
	if result:
		logger.info("selected_mode='%s' comment='%s'" % (result.control.name, result.control.comment))
	else:
		logger.info("selection cancelled")
	logger.info("Test finished")
	
if __name__ == '__main__':
	test()

