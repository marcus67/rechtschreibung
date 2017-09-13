# coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung
import six

import config

if six.PY3:
	from importlib import reload
	
reload(config)

# Enumeration for the different modes to temporarily highlight the differences in the text
# (before vs. after) when the ruleset changes.
HIGHLIGHT_OFF = 0        # do not highlight at all
HIGHLIGHT_DELTA = 1      # highlight the changes compared the state just before the change of rules
HIGHLIGHT_REFERENCE = 2  # hightight all changes compared to the initial reference ruleset

DEFAULT_RULE_SET_NAME = "Aktuelle Auswahl"

class RechtschreibungConfig(config.BaseConfig):

	def __init__(self):
		# delay before the first display of the text in the HTML page
		self.initial_update_sample_text_delay = 500 # [milliseconds]
		
		# time before highlighted changes are hidden again
		self.auto_hide_delay = 5 # [seconds]
		
		# time between attempts to save the app status to file
		self.save_interval = 1 # [seconds]
		
		# speed for speaking the text out loud
		self.speech_speed = 50 # [0 (slowest) through 100 (fastest)]
		
		# True if the app is running in full mode with all features enabled
		self.full_feature_mode = True
		
		# True if the app is running on the target iOS device. False if the app is running
		# in the Pythonista development environment.
		self.on_target_device = False
		
	def getIntAttributes(self):
		return [ 'initial_update_sample_text_delay', 
							'auto_hide_delay', 
							'speech_speed',
							'save_interval' ]
		
	def getBooleanAttributes(self):
		return [ 'full_feature_mode', 'on_target_device' ]
		
class StateConfig(config.BaseConfig):

	def __init__(self):
		
		# When 'auto_hide' is True the highlighted changes will be hidden after a certain time.
		# Otherwise they will be visible indefinitely.
		self.switch_auto_hide = False

		# Active highlighting mode. See HIGHLIGHT_* enumeration above
		self.highlighting_mode = HIGHLIGHT_DELTA
		
		# Name of the current rule set
		self.current_rule_set_name = DEFAULT_RULE_SET_NAME
				
	def getIntAttributes(self):
		return [ 'highlighting_mode' ]
		
	def getBooleanAttributes(self):
		return [ 'switch_auto_hide' ]
		
class AppConfig(config.BaseConfig):

	def __init__(self):
		self.rechtschreibung = RechtschreibungConfig()
		self.state = StateConfig()
		
