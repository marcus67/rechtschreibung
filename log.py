import logging
import logging.handlers
import sys

global logger 

def open_logging():
  
  global logger
  
  if 'logger' in globals():
    return logger

  # create logger
  logger = logging.getLogger('rechtschreibung')
  logger.handlers = []
  logger.setLevel(logging.DEBUG)
  
  # create console handler and set level to debug
#  fh = logging.handlers.RotatingFileHandler('log/rechtschreibung.log', mode='a', maxBytes=10000, backupCount=9)
  fh = logging.FileHandler('log/rechtschreibung.log', mode='w')
  fh.setLevel(logging.DEBUG)

  # create console handler and set level to debug
  ch = logging.StreamHandler()
  ch.setLevel(logging.INFO)

  # create formatter
  formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

  # add formatter to ch
  ch.setFormatter(formatter)
  fh.setFormatter(formatter)

  # add ch to logger
  logger.addHandler(ch)
  logger.addHandler(fh)
  
  logger.info("Starte Logging")
  return logger

def test():
  
  logger = open_logging()
  logger.error("Dies ist ein Fehler")
  logger.warning("Dies ist eine Warnung")  
    
if __name__ == '__main__':
  test()

