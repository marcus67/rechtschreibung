# coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung
import six

import config
import client

if six.PY3:
	from importlib import reload
	
reload(config)
reload(client)


class RechtschreibungConfig(config.BaseConfig):

	def __init__(self):
		self.initial_update_sample_text_delay = 500 # [milliseconds]
		self.auto_hide_delay = 5 # [seconds]
		self.speech_speed = 50 # [0 (slowest) through 100 (fastest)]
		
	def getIntAttributes(self):
		return [ 'initial_update_sample_text_delay', 'auto_hide_delay', 'speech_speed' ]
		
	def getBooleanAttributes(self):
		return [ ]
		
class StateConfig(config.BaseConfig):

	def __init__(self):
		
		# When 'auto_hide' is True the highlighted changes will be hidden after a certain time.
		# Otherwise they will be visible indefinitely.
		self.switch_auto_hide = False
		
	def getIntAttributes(self):
		return [ ]
		
	def getBooleanAttributes(self):
		return [ 'switch_auto_hide' ]
		
class AppConfig(config.BaseConfig):

	def __init__(self):
		self.rechtschreibung = RechtschreibungConfig()
		self.state = StateConfig()
		
