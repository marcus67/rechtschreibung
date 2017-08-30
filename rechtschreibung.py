# coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import string
import console
import ui
import speech
import threading
import copy
import os
import time
import webbrowser as wb
import six 

import log
import defaults
import view_punctuation
import spelling_mode
import rulesets
import words
import sentences
import util
import ui_util
import sample_text
import popup
import mode_manager
import mode_selector
import mode_saver
import statistics_view
import config
import app_config
import statistics
import rules_doc_manager

if six.PY3:
	from importlib import reload
	
reload(log)
reload(ui_util)
reload(view_punctuation)
reload(spelling_mode)
reload(rulesets)
reload(words)
reload(sentences)
reload(util)
reload(sample_text)
reload(popup)
reload(mode_manager)
reload(mode_selector)
reload(mode_saver)
reload(statistics_view)
reload(config)
reload(app_config)
reload(statistics)
reload(rules_doc_manager)

global logger

# Enumeration for the different modes to temporarily highlight the differences in the text
# (before vs. after) when the ruleset changes.
HIGHLIGHT_OFF = 0        # do not highlight at all
HIGHLIGHT_DELTA = 1      # highlight the changes compared the state just before the change of rules
HIGHLIGHT_REFERENCE = 2  # hightight all changes compared to the initial reference ruleset

# Location of the application global configuration file. This will be automatically updated after
# any change in the configuration.
CONFIG_FILE = 'etc/rechtschreibung_config.txt'

# Sample configuration file with default values for all settings. This file will be copied to
# the filename above if no configuration file is found (upon the first start of the application).
SAMPLE_CONFIG_FILE = 'etc/sample_rechtschreibung_config.txt'

NAME_NAVIGATION_VIEW = 'top_navigation_view'
NAME_NAVIGATION_VIEW_TOP_LEVEL = 'Regeln'

# Filename of the application icon
IMAGE_URL_RECHTSCHREIBUNG = 'lib/rechtschreibung_32.png'

# URL of the GitHub home of the source code
GITHUB_URL_RECHTSCHREIBUNG = 'https://github.com/marcus67/rechtschreibung'

# Enumeration of the two modes for the method 'load_mode_start':
LOAD_MODE_RULESET = 1    # load a current ruleset for 'testing' new variations
LOAD_MODE_REFERENCE = 2  # load a refernece ruleset for comparison with the current rule set

class MainViewController ( ui_util.ViewController ):

	"""
	The view controller handles the top view of the Rechtschreibing application.
	"""
	
	def __init__(self):
		"""
		Create an instance of the MainViewCntroller
		
		:param conf: instance of the application configuration class
		:type conf: app_config.AppConfig
		"""	
		
		super(MainViewController, self).__init__()
		
		# Store the text as it was before the most recent ruleset change. This text is used to derive
		# the changes between the previous ruleset settings and the current ones.
		self.previous_sample_text = None
		
		# Store the text as it right now according the currently active ruleset.
		self.current_sample_text = None
		
		# Active highlighting mode. See HIGHLIGHT_* enumeration above
		self.highlighting_mode = HIGHLIGHT_DELTA
		
		# Variable which is true after the specific time in which the changes are visible. So this
		# variable is only relevant for conf.state.switch_auto_hide=True.
		self.suppress_highlight_changes = False
		
		# Temporary variable to postpone the instant highlighting of changes in the ruleset.
		# When active the highlighting is delayed until the text becomes visible again. Note that
		# this setting is only relevant for the iPhone mode since in iPad mode the text is always
		# visible so changes can always be highlighted immediately.
		self.delay_highlight_changes = False
		
												# The rule_doc_manager can generate information texts for rules. They are used in popups which
												# which can be activated using the 'i' icons next to the rule switches.
		self.rule_doc_manager = rules_doc_manager.RulesDocManager(rules_doc_manager.RULE_DOC_FILE)
		
		# View controller for loading a spelling ruleset
		self.select_mode_vc = mode_selector.SpellingModeSelector(self)
		
		# View controller for saving a spelling ruleset
		self.select_mode_for_save_vc = mode_saver.SpellingModeSaver(self)
		
		# View controller for displaying the statistical diagrams of the spelling ruleset
		self.statistics_view_vc = statistics_view.StatisticsViewController(self)
		
		# View controller for displaying information on rules
		self.info_popup = popup.PopupViewController()
		
		# Current reference ruleset.  It will be used in highlighting mode HIGHLIGHT_REFERENCE to compare
		# the current ruleset. The reference rule set must never set directly but only by calling
		# method set_reference_ruleset.
		self.reference_mode = None
		
		# Set the first available ruleset reference as the default reference rule set
		#self.set_reference_mode(filter(lambda m:m.control.isReference, mode_manager.get_available_modes())[0])
		reference_rulesets = [ m for m in mode_manager.get_available_modes() if m.control.isReference ]
		self.set_reference_mode(reference_rulesets[0])
			
		# Ruleset that had been loaded most recently. Note that the current ruleset (see below) may have
		# been changed already since the last load. This ruleset is used to determine whether the current
		# ruleset is equivalent to the one most previously loaded. If they match the ruleset name in the view
		# will be displayed in black, otherwise it will be grayed out.
		self.loaded_mode = spelling_mode.spelling_mode()
		
		# Current ruleset as it is used to display the current text. This one represents the current
		# settings of the ruleset switches.
		self.current_mode = spelling_mode.spelling_mode()
		
		# This variable holds the selected load mode (see LOAD_MODE_* above) between calls to
		# methods load_mode_start and load_mode_finish
		self.load_mode_type = None
		
		# Adapt the orientation of the GUI to the format of the physical screen
		if ui_util.is_iphone():
			self.orientations = ( 'portrait', )
		else:
			self.orientations = ( 'landscape', )
			
	def load_config(self, p_config_handler):
		
		# Store the configuration instance
		self._config_handler = p_config_handler
		self.conf = self._config_handler.read_config_file(CONFIG_FILE, SAMPLE_CONFIG_FILE)
	
		self.retrieve_from_model(self.conf.state)
			
	def handle_change_in_mode(self):
		self.previous_sample_text = self.current_sample_text
		self.suppress_highlight_changes = False
		self.update_sample_text()
		
	def set_reference_mode(self, mode):
		self.reference_mode = mode
		tempStoreMode = rulesets.get_default_mode()
		rulesets.set_default_mode(self.reference_mode.combination)
		self.referenceSampleText = sample_text.get_sample_text()
		rulesets.set_default_mode(tempStoreMode)
		
	def handle_button_action(self, name, sender):
		BUTTON_PREFIX = 'button_'
		INFO_PREFIX = 'info_'
		
		if name == 'button_start_speech':
			speech.say(sample_text.get_sample_text(), 'de', 1.0 * self.conf.rechtschreibung.speech_speed / 100.0)
			
		elif name == 'button_stop_speech':
			speech.stop()
			
		elif name == 'button_load_mode':
			self.load_mode_start(LOAD_MODE_RULESET)
			
		elif name == 'button_load_reference_mode':
			self.load_mode_start(LOAD_MODE_REFERENCE)
			
		elif name == 'button_save_mode':
			self.save_mode_start()
			
		elif name == 'button_open_app_control_view':
			self.open_app_control_view()
			
		elif name == 'button_open_top_navigation_view':
			self.open_top_navigation_view()
			
		elif name == 'button_open_statistics_view':
			self.open_statistics_view()
			
		elif name == 'button_close_top_navigation_view':
			self.close_top_navigation_view()
			
		elif name == 'button_icon_rechtschreibung':
			self.button_icon_rechtschreibung()
			
		elif name.startswith(BUTTON_PREFIX):
			view_name = name[len(BUTTON_PREFIX):]
			child_view = self.find_subview_by_name(view_name)
			if child_view is not None:
				view = self.find_subview_by_name(NAME_NAVIGATION_VIEW)
				view.push_view(child_view)
				return 1
				
			else:
				logger.warning("cannot find subview '%s" % view_name)
				
		elif name.startswith(INFO_PREFIX):
			info_name = name[len(INFO_PREFIX):]
			rule_info = self.rule_doc_manager.get_rule_info_by_attr_name(info_name)
			
			if rule_info is not None:
				self.info_popup.present(rule_info, close_label=words.schlieszen(c=rulesets.C_BOS))
				
			else:
				logger.error("cannot find info text for %s" % info_name)
				
		else:
			super(MainViewController, self).handle_button_action(name, sender)
			
	def handle_switch_auto_hide(self, p_value):
		self.conf.state.switch_auto_hide = p_value
		self._config_handler.mark_configuration_as_changed()
		
		# TEMPORARY!
		self._config_handler.write_config_file()
		
		self.suppress_highlight_changes = self.conf.state.switch_auto_hide
		self.update_sample_text()
						
	def handle_switch_action(self, sender):
		if sender.name == 'switch_auto_hide':
			self.handle_switch_auto_hide(p_value=sender.value)
			
		elif ui_util.store_in_model(sender, self.model):
			self.handle_change_in_mode()
			
		else:
			super(MainViewController, self).handle_switch_action(sender)
			
	def handle_segmented_control_action(self, sender):
		if sender.name == 'segmented_control_highlighting_mode':
			self.highlighting_mode = sender.selected_index
			self.update_sample_text()
			
		elif ui_util.store_in_model(sender, self.model):
			self.handle_change_in_mode()
			
		else:
			super(MainViewController, self).handle_segmented_control_action(sender)
			
	def handle_named_action(self, name):
		if name == 'load_mode_finish':
			self.load_mode_finish()
			
		elif name == 'save_mode_finish':
			self.save_mode_finish()
			
		else:
			super(MainViewController, self).handle_named_action(name)
			
	def open_top_navigation_view(self):
		global logger
		
		view = self.find_subview_by_name(NAME_NAVIGATION_VIEW)
		
		if view is None:
			logger.warning("open_top_navigation_view: cannot find view %s" % NAME_NAVIGATION_VIEW)
			return
			
		self.delay_highlight_changes = True
		view.height = ui_util.PORTRAIT_SMALL_VIEW_HEIGHT + ui_util.NAVIGATION_VIEW_TITLE_HEIGHT
		view.present(style='sheet' , hide_title_bar=True, orientations=self.orientations)
		
	def close_top_navigation_view(self):
		view = self.find_subview_by_name(NAME_NAVIGATION_VIEW)
		view.close()
		self.delay_highlight_changes = False
		self.update_sample_text()
		
	def open_app_control_view(self):
		view = self.find_subview_by_name('App-Konfiguration')
		view.present(style='sheet', orientations=self.orientations)
		
	def open_statistics_view(self):
		self.statistics_view_vc.present(self.referenceSampleText, self.current_sample_text)
		
	def check_activate_hide_timer(self):
		if (self.conf.state.switch_auto_hide and self.highlighting_mode and not
		(self.suppress_highlight_changes or self.delay_highlight_changes)):
			self.activate_hide_timer()
			
	def activate_hide_timer(self):
		self.hideTimer = threading.Timer(
		self.conf.rechtschreibung.auto_hide_delay,
		lambda x:x.handle_hide_timer(), [ self ] )
		self.hideTimer.start()
		
	def handle_hide_timer(self):
		self.suppress_highlight_changes = True
		self.update_sample_text()
		
	def update_sample_text(self, p_initial_update = False):
		"""
		:type webview: ui.View
		"""
		# Wait for a fraction of a second so that load_url() above (which seems to be aynchronous)
		# has a chance to load the page before update_sample_text() below sets the initial content.
		time.sleep(1.0 * self.conf.rechtschreibung.initial_update_sample_text_delay / 1000.0)
		
		self.current_sample_text = sample_text.get_sample_text()
		webview = self.view['webview_text_view']
		if self.highlighting_mode == HIGHLIGHT_DELTA:
			compareText = self.previous_sample_text
		else:
			compareText = self.referenceSampleText
		html_content = util.get_html_content(
		compareText, self.current_sample_text,
		self.highlighting_mode and not self.suppress_highlight_changes)
		
		webview.eval_js('document.getElementById("content").innerHTML = "%s"' % html_content)
		webview.set_needs_display()
		
		self.check_activate_hide_timer()
		self.update_views()
		
	def update_views(self):
		global logger
		
		view = self.find_subview_by_name('segmented_control_highlighting_mode')
		view.selected_index = self.highlighting_mode
		
		view = self.find_subview_by_name('textfield_reference_mode_name')
		view.enabled = False
		view.text = self.reference_mode.control.name
		
		view = self.find_subview_by_name('textfield_current_mode_name')
		view.enabled = False
		view.text = self.loaded_mode.control.name
		
		if self.loaded_mode.combination == self.current_mode.combination:
			view.text_color = defaults.COLOR_BLACK
			
		else:
			view.text_color = defaults.COLOR_GREY
			
		difference_count_in_rules = util.count_differences_in_dicts(self.reference_mode.combination.__dict__, self.current_mode.combination.__dict__)
		view = self.find_subview_by_name('textview_mode_statistics')
		fmt = u"Regelabweichungen zur Referenz: %d\nAnzahl Zeichen:%d (Referenz:%d)\nAnzahl verschiedener Zeichen:%d (Referenz:%d)"
		reference_text = rulesets.to_upper(self.referenceSampleText)
		reference_letter_histogram = statistics.get_letter_histogram(reference_text)
		current_text = rulesets.to_upper(self.current_sample_text)
		current_letter_histogram = statistics.get_letter_histogram(current_text)
		view.text = fmt % ( difference_count_in_rules, len(current_text), len(reference_text), len(current_letter_histogram), len(reference_letter_histogram) )
		
	def load_mode_start(self, load_mode_type):
		self.load_mode_type = load_mode_type
		self.select_mode_vc.select(
		mode_manager.get_available_modes(), cancel_label=words.abbrechen(c=rulesets.C_BOS),
		close_label=words.schlieszen(c=rulesets.C_BOS),
		title = 'Regelsatz laden' if load_mode_type == LOAD_MODE_RULESET else 'Referenz laden')
		
		
	def load_mode_finish(self):
		selectedMode = self.select_mode_vc.get_selected_mode()
		
		if selectedMode is not None:
			if self.load_mode_type == LOAD_MODE_RULESET:
				logger.info("Set working mode '%s'" % selectedMode.control.name)
				rulesets.set_default_mode(selectedMode.combination)
				self.loaded_mode = copy.deepcopy(selectedMode)
				self.current_mode = copy.copy(selectedMode)
				self.set_model(self.current_mode.combination)
				rulesets.set_default_mode(self.current_mode.combination)
				self.handle_change_in_mode()
				
			else:
				logger.info("Set reference mode '%s'" % selectedMode.control.name)
				self.set_reference_mode(copy.deepcopy(selectedMode))
				self.update_sample_text()
				self.update_views()
				
		self.load_mode_type = None
		
	def save_mode_start(self):
		self.select_mode_for_save_vc.select(mode_manager.get_available_modes(), self.current_mode, cancel_label=words.abbrechen(c=rulesets.C_BOS), save_label=words.speichern(c=rulesets.C_BOS), overwrite_label=words.ueberschreiben(c=rulesets.C_BOS), style='sheet')
		
	def save_mode_finish(self):
		selectedMode = self.select_mode_for_save_vc.get_selected_mode()
		if selectedMode is not None:
			mode_manager.write_mode(selectedMode)
			self.loaded_mode = copy.copy(selectedMode)
			self.handle_change_in_mode()
			
	def button_icon_rechtschreibung(self):
		global logger
		
		logger.info("Opening URL %s" % GITHUB_URL_RECHTSCHREIBUNG)
		wb.open(GITHUB_URL_RECHTSCHREIBUNG, modal=True)
		
		
##### MAIN ######################

def main():

	global logger
	
	console.clear()
	logger = log.open_logging('rechtschreibung', reload=True)
	logger.info("Start application")
	default_mode = spelling_mode.spelling_mode()
	rulesets.set_default_mode(default_mode.combination)
	
	config_handler = config.ConfigHandler(app_config.AppConfig())
	
	image_rechtschreibung = ui.Image.named(IMAGE_URL_RECHTSCHREIBUNG).with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
	my_main_view_controller = MainViewController()
	
	top_navigation_vc = ui_util.ViewController(my_main_view_controller)
	navigation_vc = ui_util.ViewController(top_navigation_vc)
	navigation_vc.load('top_navigation')
	
	top_navigation_view = ui.NavigationView(navigation_vc.view, title_bar_color = defaults.COLOR_GREY)
	top_navigation_view.title_bar_color = defaults.COLOR_LIGHT_GREY
	top_navigation_vc.view = top_navigation_view
	my_main_view_controller.add_child_controller(NAME_NAVIGATION_VIEW, top_navigation_vc)
	top_navigation_view.name = NAME_NAVIGATION_VIEW
	
	if ui_util.is_iphone():
		my_main_view_controller.load('rechtschreibung_iphone')
		app_control_vc = ui_util.ViewController(my_main_view_controller)
		app_control_vc.load('rechtschreibung_app_control_iphone')
		my_main_view_controller.add_left_button_item(NAME_NAVIGATION_VIEW_TOP_LEVEL, 'button_close_top_navigation_view', ui.ButtonItem(image=ui.Image.named('iob:close_round_32')))
		
		button_item_list = [
		ui.ButtonItem(image=ui.Image.named('lib/ios7_toggle_32.png'), action=my_main_view_controller.handle_action, title='button_open_top_navigation_view'),
		ui.ButtonItem(image=ui.Image.named('ionicons-gear-a-32'), action=my_main_view_controller.handle_action, title='button_open_app_control_view'),
		ui.ButtonItem(image=image_rechtschreibung, action=my_main_view_controller.handle_action, title='button_icon_rechtschreibung'),
		]
		my_main_view_controller.set_right_button_item_list('Rechtschreibung', button_item_list)
		
	else:
		my_main_view_controller.load('rechtschreibung')
		my_main_view_controller.add_right_button_item('Rechtschreibung', 'button_icon_rechtschreibung', ui.ButtonItem(image=image_rechtschreibung))
		my_main_view_controller.add_subview('view_container_navigation', top_navigation_vc.view)
		
	view = my_main_view_controller.find_subview_by_name('segmented_control_highlighting_mode')
	view.action = my_main_view_controller.handle_action
	
	view_controller_capitalization = ui_util.ViewController(my_main_view_controller)
	view_controller_capitalization.load('view_capitalization')
	
	view_controller_harmonization = ui_util.ViewController(my_main_view_controller)
	view_controller_harmonization.load('view_harmonization')
	view = my_main_view_controller.find_subview_by_name('segmented_control_harmonization_elongation')
	view.action = my_main_view_controller.handle_action
	
	view_controller_combinations_simplification = ui_util.ViewController(my_main_view_controller)
	view_controller_combinations_simplification.load('view_combinations_simplification')
	
	view_controller_combinations_simplification_vowels = ui_util.ViewController(my_main_view_controller)
	view_controller_combinations_simplification_vowels.load('view_combinations_simplification_vowels')
	
	view_controller_punctuation = ui_util.ViewController(my_main_view_controller)
	view_controller_punctuation.load('view_punctuation')
	
	view_controller_legacy = ui_util.ViewController(my_main_view_controller)
	view_controller_legacy.load('view_legacy')
	
	view_controller_layout = ui_util.ViewController(my_main_view_controller)
	view_controller_layout.load('view_layout')
	
	view_controller_misc_rules = ui_util.ViewController(my_main_view_controller)
	view_controller_misc_rules.load('view_misc_rules')
	
	my_main_view_controller.set_model(default_mode.combination)
	
	my_main_view_controller.load_config(config_handler)
	
	# Set the empty html page for displaying the sample text. The actual content will be set in
	# method "update_sample_text". We use an absolute path to load the page so that the relative
	# path reference to the style sheet can be derrived by the browser.
	text_view = my_main_view_controller.find_subview_by_name('webview_text_view')
	absolute_page_path = 'file:' + os.path.abspath('etc/text_page.html')
	logger.info('Loading HTML page at %s' % absolute_page_path)
	text_view.load_url(absolute_page_path)
	
	my_main_view_controller.update_sample_text(p_initial_update = True)
	my_main_view_controller.present('fullscreen', title_bar_color=defaults.COLOR_GREY)
	speech.stop()
	logger.info("Terminate application")
	
if __name__ == '__main__':
	main()

