# coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import matplotlib.pyplot as plot
import matplotlib.figure as figure
import numpy as np
import console
import six

import log
import defaults
import rulesets
import spelling_mode
import sample_text
import statistics

if six.PY3:
	from importlib import reload
	
reload(log)
reload(defaults)
reload(rulesets)
reload(spelling_mode)
reload(sample_text)
reload(statistics)

TMP_PLOT_FILE = 'doc/plot.png'
PIXELS_PER_INCH = 200

DEFAULT_REPLACEMENTS = { ' ':'Leerz.', '.':'Punkt', ',':'Komma', ':':'Doppelp.' }
DEFAULT_COLORS = ( defaults.COLOR_LIGHT_GREEN, defaults.COLOR_LIGHT_PURPLE, defaults.COLOR_LIGHT_YELLOW, defaults.COLOR_LIGHT_YELLOW_2, defaults.COLOR_LIGHT_ORANGE, defaults.COLOR_LIGHT_PINK, defaults.COLOR_LIGHT_BLUE, defaults.COLOR_LIGHT_YELLOW_GREEN )

def plot_letter_histogram(plot_file, histogram, width, height):
	'''
	:type fig: figure.Figure
	'''
	#values = map(lambda x:x[1], histogram)
	values = [ x[1] for x in histogram ]
	#labels = map(lambda x:x[0], histogram)
	labels = [ x[0] for x in histogram ]
	fig = plot.gcf()
	fig.clear()
	plot.pie(x=values, labels=labels, colors=DEFAULT_COLORS )
	fig.set_size_inches(6.0 * width / PIXELS_PER_INCH, 6.0 * height / PIXELS_PER_INCH)
	fig.savefig(plot_file, bbox_inches='tight', pad_inches=0.0)
	
	
def plot_frequency_change_bars(plot_file, changes, width, height, legend=None):
	x = np.arange(len(changes))
	bar_width = 0.7
	y = [ 100.0 * entry[1] for entry in changes ]
	min_y = min(y)
	max_y = max(y)
	axis_min_y = -100
	axis_max_y = 100
	if min_y < -100:
		axis_min_y = 50 * int(1.0 / 50.0 * min_y - 1.0)
	if max_y > 100:
		axis_max_y = 50 * int(1.0 / 50.0 * max_y + 1.0)
		
	labels = [ entry[0] for entry in changes]
	colors = [ defaults.COLOR_LIGHT_RED if entry[1] > 0 else defaults.COLOR_LIGHT_GREEN for entry in changes]
	fig = plot.gcf()
	fig.clear()
	bar_plot = plot.bar(left=x, height=y, width=bar_width, color=colors)
	plot.hlines((0,), 0, len(changes) )
	
	plot.ylabel(u'Änderung [%]')
	plot.title(u'Relative Änderung der Buchstabenhäufigkeit')
	plot.xticks(x + bar_width / 2.0, labels )
	plot.yticks(np.arange(axis_min_y, axis_max_y + 1, 50))
	if legend:
		plot.legend((bar_plot[0],), (legend,), loc=2)
	fig.set_size_inches(3.0 * width / PIXELS_PER_INCH, 3.0 * height / PIXELS_PER_INCH)
	fig.savefig(plot_file, bbox_inches='tight', pad_inches=0.0)
	
def test():
	default_mode = spelling_mode.spelling_mode()
	rulesets.set_default_mode(default_mode.combination)
	text = rulesets.to_upper(sample_text.get_sample_text())
	histogram = statistics.map_labels(statistics.get_letter_histogram(text), DEFAULT_REPLACEMENTS)
	histogram2 = statistics.keep_n_largest(histogram, 20)
	print (histogram2)
	print (histogram2[:][1])
	plot_letter_histogram(TMP_PLOT_FILE, histogram2, 200, 200)
	console.show_image(TMP_PLOT_FILE)
	
	new_text = text[100:] + 'XXÖÖÜßßßßxxxxp'
	histogram = statistics.get_letter_histogram(text)
	histogram2 = statistics.get_letter_histogram(new_text)
	
	changes = statistics.compute_changes(histogram, histogram2)
	summary_small_changes = statistics.summarize_small_changes(changes, 0.05)
	actual_changes = statistics.keep_actual_changes(changes,0.05)
	
	plot_frequency_change_bars(TMP_PLOT_FILE, actual_changes, 600, 200, summary_small_changes)
	console.show_image(TMP_PLOT_FILE)
	
if __name__ == '__main__':
	test()

