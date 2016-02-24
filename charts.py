# coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import matplotlib.pyplot as plot
import matplotlib.figure as figure
import console

import log
import defaults
import rulesets
import spelling_mode
import sample_text
import statistics

reload(log)
reload(defaults)
reload(rulesets)
reload(spelling_mode)
reload(sample_text)
reload(statistics)

TMP_PLOT_FILE = 'doc/plot.png'

DEFAULT_REPLACEMENTS = { ' ':'Leerz.', '.':'Punkt', ',':'Komma', ':':'Doppelp.' }
DEFAULT_COLORS = ( defaults.COLOR_LIGHT_GREEN, defaults.COLOR_LIGHT_PURPLE, defaults.COLOR_LIGHT_YELLOW, defaults.COLOR_LIGHT_YELLOW_2, defaults.COLOR_LIGHT_ORANGE, defaults.COLOR_LIGHT_PINK, defaults.COLOR_LIGHT_BLUE, defaults.COLOR_LIGHT_YELLOW_GREEN )

def plot_letter_histogram(plot_file, histogram, width, height):
  '''
  :type fig: figure.Figure
  '''
  values = map(lambda x:x[1], histogram)
  labels = map(lambda x:x[0], histogram)
  fig = plot.gcf()
  fig.clear()
  plot.pie(x=values, labels=labels, colors=DEFAULT_COLORS )
  fig.set_size_inches(6,6)
  fig.savefig(plot_file, bbox_inches='tight', pad_inches=0.0)
  
def test():
  default_mode = spelling_mode.spelling_mode()
  rulesets.set_default_mode(default_mode.combination)
  text = rulesets.to_upper(unicode(sample_text.get_sample_text()))
  histogram = statistics.map_labels(statistics.get_letter_histogram(text), DEFAULT_REPLACEMENTS)
  histogram2 = statistics.keep_n_largest(histogram, 20)
  print histogram2
  print histogram2[:][1]
  plot_letter_histogram(TMP_PLOT_FILE, histogram2, 200, 200)
  console.show_image(TMP_PLOT_FILE)
  
if __name__ == '__main__':
  test()
  
  