
import ui

view = ui.load_view('view_harmonization')    
subview = view['scrollview_harmonization']['segmented_control_harmonization_elongation']
print subview.name
print type(subview).__name__
print "%d subviews" % len(subview.subviews)
for subsubview in subview.subviews:
  print subsubview.name

