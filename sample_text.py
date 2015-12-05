import spelling_mode
import rulesets
import sentences

reload(spelling_mode)
reload(rulesets)
reload(sentences)

from sentences import *
from rulesets import *

def get_sample_text():
  return sentence001() + space() + sentence002() + space()+ sentence003() + space()+ sentence004() + space()+ sentence005() + para() + sentence006() + space() + sentence007() + space() + sentence008() + space() + sentence009() + space() + sentence010() + space() + sentence011() + space() + para() + sentence012() + space() + sentence013() + para() + para() + sentence1() + sentence2() + sentence3() + para() + sentence4() + para() + sentence5() 
  
def test():
  rulesets.set_default_mode(rulesets.spelling_mode())
  print get_sample_text()
  
if __name__ == '__main__':
  test()

