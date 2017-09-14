# coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import os
import io
import re
import pickle
import six

import log
import util
import spelling_mode
import predefined_modes

if six.PY3:
	from importlib import reload
	
reload(log)
reload(util)
reload(spelling_mode)
reload(predefined_modes)

MODE_FILE_DIRECTORY = u'configurations'
MODE_FILE_EXTENSION = u'.mode.pickle'
MODE_FILE_EXTENSION_PATTERN = u'(.+)' + MODE_FILE_EXTENSION.replace(u'.', u'\.')

global logger

logger = log.open_logging(__name__)

def get_mode_filename(p_document_directory, modeName):

	return os.path.join(
		p_document_directory, MODE_FILE_DIRECTORY, 
		u"%s%s" % ( modeName, MODE_FILE_EXTENSION))
	
def read_mode(p_document_directory, modeName):

	global logger
	
	filename = get_mode_filename(p_document_directory, modeName)
	file = io.open(filename, "rb")
	logger.info("read mode file '%s'" % filename)
	mode = pickle.load(file)
	file.close()
	changes = util.add_missing_attributes(mode.combination, spelling_mode.spelling_mode().combination)
	mode.control.is_modified = False
	if changes > 0:
		logger.info("mode file '%s' is lacking %d attributes; filling up" % (filename, changes))
		write_mode(mode)
	return mode
	
def write_mode(p_document_directory, mode):

	global logger
	
	filename = get_mode_filename(p_document_directory, mode.control.name)
	
	directory = os.path.dirname(filename)
	if not os.path.exists(directory):
		os.makedirs(directory)
	
	logger.info("write mode file '%s'" % filename)
	file = io.open(filename, "wb")
	pickle.dump(mode, file, protocol=1)
	file.close()
	mode.control.is_modified = False
	
def get_available_modes(p_document_directory, includePredefinedModes = True):

	modes = []
	
	if includePredefinedModes:
		modes.extend(predefined_modes.get_predefined_modes())
		
	filePattern = re.compile(MODE_FILE_EXTENSION_PATTERN)
	
	for file in os.listdir(os.path.join(p_document_directory, MODE_FILE_DIRECTORY)):
		match = filePattern.match(file)
		
		if (match):
			modeName = match.group(1)
			mode = read_mode(p_document_directory, modeName)
			modes.append(mode)
			
	return modes
	
	
def test():

	modes = get_available_modes(".")
	for mode in modes:
		if mode.control.isImmutable:
			mode.control.name = mode.control.name + u' (pickled)'
			mode.control.isImmutable = False
			write_mode(".", mode)
			
if __name__ == '__main__':
	test()

