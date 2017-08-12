# coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import six

import log
import rulesets

if six.PY3:
	from importlib import reload
	
reload(log)
reload(rulesets)

global logger

logger = log.open_logging(__name__)


def get_letter_histogram(text):
	histogram = {}
	
	for l in text:
		if l in histogram:
			counter = histogram[l] + 1
		else:
			counter = 1
		histogram[l] = counter
		
	return histogram.items()
	
def map_labels(histogram, replacements):
	return map(lambda x:(replacements[x[0]] if x[0] in replacements else x[0], x[1]), histogram)
	
def keep_n_largest(histogram, n, title_other="other"):

	sorted_histogram = sorted(histogram, key=lambda x:x[1], reverse=True)
	new_histogram = sorted_histogram[0:n]
	if len(sorted_histogram) > n:
		sum_count = sum(map(lambda x:x[1], sorted_histogram[n:]))
		new_histogram.append((title_other, sum_count))
	return new_histogram
	
def compute_changes(histogram1, histogram2):
	changes = {}
	
	for entry in histogram1:
		changes[entry[0]] = (entry[1], 0)
		
	for entry in histogram2:
		if entry[0] in changes:
			changes[entry[0]] = (changes[entry[0]][0], entry[1])
		else:
			changes[entry[0]] = (0, entry[1])
			
#	new_map = map(lambda x:(x[0], 1.0*(x[1][1]-x[1][0])/x[1][0] if x[1][0] > 0 else 1.0), changes.items())
	
	new_map = { (x[0], 1.0*(x[1][1]-x[1][0])/x[1][0] if x[1][0] > 0 else 1.0 ) for x in changes.items()}		
	return new_map
	
def keep_actual_changes(changes, threshold = 0.0):

	filtered = [entry for entry in changes if abs(entry[1]) >= threshold]
	return sorted(filtered, key=lambda x:x[1])
	
def summarize_small_changes(changes, threshold):

	change_list = ",".join("'%s'" % entry[0] for entry in changes if abs(entry[1]) < threshold and entry[1] != 0.0)
	if change_list:
		return u"Delta<%2.0f%% in %s" % ( 100.0 * threshold, change_list )
	else:
		return u"Alle Änderungen im Graphen sichtbar"
		
def test():
	histogram = get_letter_histogram(rulesets.to_upper('Dies ist ein Test!'))
	print (histogram)
	histogram2 = map_labels(histogram, { ' ' : 'space'})
	print (histogram2)
	histogram3 = keep_n_largest(histogram2, 5, "andere")
	print (histogram3)
	histogram4 = get_letter_histogram(rulesets.to_upper('Das ist noch ein Test!'))
	
	changes = compute_changes(histogram, histogram4)
	print (changes)
	summary = summarize_small_changes(changes, 0.5)
	actual_changes = keep_actual_changes(changes, 0.5)
	print (actual_changes)
	print (summary)
	
if __name__ == '__main__':
	test()

