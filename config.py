# coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import copy
import string
import shutil
import os
import six

import log

if six.PY2:
	from ConfigParser import ConfigParser

else:
	from configparser import ConfigParser
	from importlib import reload
	
reload(log)

global logger

logger = log.open_logging(__name__)

class BaseConfig(object):

	def getIntAttributes(self):
		return list()
		
	def getBooleanAttributes(self):
		return list()
		
	def dump(self):
		self._dump(conf=self, parent_prefix=type(self).__name__ + '.')
		
	def _dump(self, conf, parent_prefix):
		global logger
		
		for (key, value) in conf.__dict__.items():
			attr_type = type(getattr(conf, key)).__name__
			name = parent_prefix + key
			#print attr_type
			if attr_type in ('int', 'bool', 'str'):
				logger.debug('%s=%s' % (name, str(value)))
				
			elif attr_type == 'NoneType':
				logger.debug('%s=<NONE>' % name)
				
			else:
				self._dump(value, name + '.')
				
class ConfigHandler(object):

	def __init__(self, config_template):
		self.config_template = config_template
		self._changed = False
		self._config_filename = None
		
	def scan_section(self, sectionName, model):
		for option in self.config_file.options(sectionName):
		
			print (sectionName, option)
			if not option in model.__dict__:
				fmt = "configuration file contains invalid option '%s' in section '%s'"
				raise Exception(fmt % (option, sectionName))
				
			if option in model.getBooleanAttributes():
				optionValue = self.config_file.get(sectionName, option).upper()
				
				if optionValue in '1 TRUE YES WAHR JA J'.split():
					setattr(model, option, True)
				
				elif optionValue in '0 FALSE NO FALSCH NEIN N'.split():
					setattr(model, option, False)
				
				else:
					fmt = "Invalid Boolean value '%s' in option '%s' of section '%s'"
					raise Exception(fmt % (self.config_file.get(sectionName, option), option, sectionName))
					
			elif option in model.getIntAttributes():
				try:
					intValue = int(self.config_file.get(sectionName, option))
					setattr(model, option, intValue)
					
				except Exception as e:
					fmt = "Invalid numeric value '%s' in option '%s' of section '%s'"
					raise Exception(fmt % (self.config_file.get(sectionName, option), option, sectionName))
					
			else:
				setattr(model, option, self.config_file.get(sectionName, option))
				
				
	def read_config_file(self, filename, sample_filename=None):
	
		global logger
		
		self.config_file = ConfigParser()
		self.config_file.optionxform = str # make options case sensitive
		self._config = copy.deepcopy(self.config_template)
		
		error_message = None
		
		try:
			if sample_filename != None and (not os.path.exists(filename)) and os.path.exists(sample_filename):
				logger.info("Copying sample configuration file '%s'" % sample_filename)
				shutil.copyfile(sample_filename, filename)
				
		except Exception as e:
			fmt = "Error '%s' while copying sample configuration file '%s'"
			error_message = fmt % (str(e), sample_filename )
			
		if not error_message:
			fmt = "reading configuration file '%s' for config '%s'"
			logger.info(fmt % (filename, type(self.config_template).__name__))
			
			try:
				files_read = self.config_file.read([filename])
				if len(files_read) != 1:
					error_message = "Error while reading configuration file '%s'" % filename
					
			except Exception as e:
				fmt = "Error '%s' while reading configuration file '%s'"
				error_message = fmt % (str(e), filename )
				
		if error_message:
			raise Exception(error_message)
			
		for section_name in self.config_file.sections():
		
			if section_name in self.config_template.__dict__:
				sub_config = getattr(self._config, section_name)
				self.scan_section(section_name, sub_config)
				
			else:
				raise Exception("Configuration file contains invalid section '%s'" % section_name)
		
		self._config_filename = filename		
		return self._config
	
	def mark_configuration_as_changed(self):
		self._changed = True
		
	def write_config_file(self):
		if self._changed:		
			
			for section_name in self.config_template.__dict__:
				sub_config = getattr(self._config, section_name)
				for attr_name in sub_config.__dict__:
					self.config_file.set(section_name, attr_name, str(getattr(sub_config, attr_name)))
			
			filename = self._config_filename # + ".test"
			file = open(filename, "w", encoding = "UTF-8")
			fmt = "Writing modified configuration to %s" % filename
			logger.info(fmt)
			self.config_file.write(file)
			file.close()
			self._changed = False
		
def test():
	pass
	
if __name__ == '__main__':
	test()

