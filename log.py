# coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import logging
import logging.handlers
import logging.config
import sys
import os
import shutil
import json

import log_stat

LOGGING_FILENAME = "etc/log_config.json"
LOGGING_TEMPLATE_FILENAME = "etc/log_config_template.json"

def open_logging(module_name, reload = False, p_document_directory = "."):

	global logger
	
	if reload or not log_stat.get_log_started():
	
		log_stat.set_log_started(True)
		logging_filename = os.path.join(p_document_directory, LOGGING_FILENAME)
		copy_template = os.path.exists(LOGGING_TEMPLATE_FILENAME) and not os.path.exists(logging_filename)
		if copy_template:
			directory = os.path.dirname(logging_filename)
			if not os.path.exists(directory):
				os.makedirs(directory)
			shutil.copyfile(LOGGING_TEMPLATE_FILENAME, logging_filename)
		logging_config_json_file = open(logging_filename)
		parsed_logging_data = json.load(logging_config_json_file)
		log_dir = os.path.join(p_document_directory, parsed_logging_data["handlers"]["file"]["filename"])
		parsed_logging_data["handlers"]["file"]["filename"] = log_dir
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

