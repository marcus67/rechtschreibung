# coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import logging
import logging.handlers
import logging.config
import sys
import os
import shutil
import json

import util

LOGGING_FILENAME = "etc/log_config.json"
LOGGING_TEMPLATE_FILENAME = "etc/log_config_template.json"
LOGGING_TARGET_DEVICE_TEMPLATE_FILENAME = "etc/log_config_target_device_template.json"

def open_logging(
	module_name, reload = False, p_document_directory = ".",
	p_running_on_target_device=False):

	global logger
	
	if reload:
		logging_filename = os.path.join(p_document_directory, LOGGING_FILENAME)
		
		if p_running_on_target_device:
			template_filename = LOGGING_TARGET_DEVICE_TEMPLATE_FILENAME
			
		else:
			template_filename = LOGGING_TEMPLATE_FILENAME
			
		copy_template = os.path.exists(template_filename) and not os.path.exists(logging_filename)
		
		if copy_template:
			util.check_directory(p_filename=logging_filename)
			shutil.copyfile(template_filename, logging_filename)
		
		logging_config_json_file = open(logging_filename)
		parsed_logging_data = json.load(logging_config_json_file)
		log_file = os.path.join(p_document_directory, parsed_logging_data["handlers"]["file"]["filename"])
		parsed_logging_data["handlers"]["file"]["filename"] = log_file
		util.check_directory(p_filename=log_file)
		logging_config_json_file.close()
		logging.config.dictConfig(parsed_logging_data)
		
		logger = logging.getLogger('log')
		
		if copy_template:
			logger.info("Copied logging configuration template %s" % LOGGING_TEMPLATE_FILENAME)
		
		logger.info("Loaded logging configuration from %s" % logging_filename)
		logger.info("Starting logging")
		
	return logging.getLogger(module_name)
	
def test():

	logger = open_logging('test', True)
	logger.error("This is an error")
	logger.warning("This is a warning")
	
if __name__ == '__main__':
	test()

