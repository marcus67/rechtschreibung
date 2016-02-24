# coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import ui

import defaults
import ui_util
import rulesets
import statistics
import charts

reload(defaults)
reload(ui_util)
reload(rulesets)
reload(statistics)
reload(charts)

from rulesets import *

DEFAULT_TITLE = 'Statistik'

PLOT1_FILENAME = 'doc/plot1.png'
PLOT2_FILENAME = 'doc/plot2.png'

class StatisticsViewController ( ui_util.ViewController ) :

  def __init__(self, parent_vc=None):
    super(StatisticsViewController, self).__init__(parent_vc)
    if ui_util.is_iphone():
      self.load('statistics_view_iphone')
    else:
      self.load('statistics_view')
    self.imageview_plot1 = self.find_subview_by_name('imageview_plot1')
    self.imageview_plot2 = self.find_subview_by_name('imageview_plot2')
    
  def handle_action(self, sender):
    if sender.name == 'button_close':
      self.view.close()
      
    else:
      print "WARNING: action '%s' not handled!" % sender.name
      
    return 0
    
  def prepare_image_view(self, text, plot_file):
    normalized_text = rulesets.to_upper(unicode(text))
    histogram = statistics.map_labels(statistics.get_letter_histogram(normalized_text), charts.DEFAULT_REPLACEMENTS)
    histogram2 = statistics.keep_n_largest(histogram, 20, 'andere')
    charts.plot_letter_histogram(plot_file, histogram2, 200, 200)    
    
  def present(self, reference_text, working_text, style='sheet'):
    self.prepare_image_view(reference_text, PLOT1_FILENAME)
    self.imageview_plot1.image = ui.Image.named(PLOT1_FILENAME).with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
    self.prepare_image_view(working_text, PLOT2_FILENAME)
    self.imageview_plot2.image = ui.Image.named(PLOT2_FILENAME).with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)    
    super(StatisticsViewController, self).present(style)
    
def test():  
  popup_vc = StatisticsViewController()
  popup_vc.present("Hallo!", "Das ist ein anderer Text")    
    
if __name__ == '__main__':
  test()