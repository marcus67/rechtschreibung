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
		return ( 'initial_update_sample_text_delay', 'auto_hide_delay', 'speech_speed')
		
	def getBooleanAttributes(self):
		return list()
		
class AppConfig(config.BaseConfig):

	def __init__(self):
		self.rechtschreibung = RechtschreibungConfig()

