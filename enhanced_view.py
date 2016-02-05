# coding: utf-8
import ui
import scene

STATUS_ROW_HEIGHT = 20

def get_absolute_y(view):
  """
  :type view: ui.View
  """
  if view.superview:
    return get_absolute_y(view.superview) + view.frame[1]
  else:
    return view.frame[1]
      
class EnhancedTextFieldDelegate (object):
  
  def __init__(self, extended_view):
    self.extended_view = extended_view
    
  def textfield_should_begin_editing(self, text_field):
    return True
    
  def textfield_did_begin_editing(self, text_field):
    self.extended_view.did_begin_editing(text_field)
    
  def textfield_did_end_editing(self, text_field):
    self.extended_view.did_end_editing()
    
  def textfield_should_return(self, text_field):
    text_field.end_editing()
    return True
    
  def textfield_should_change(self, text_field, range, replacement):
    return True
    
  def textfield_did_change(self, text_field):
    pass
    
class EnhancedTextViewDelegate (object):
  
  def __init__(self, extended_view):
    self.extended_view = extended_view
      
  def textview_did_begin_editing(self, text_view):
    self.extended_view.did_begin_editing(text_view)
  
  def textview_did_end_editing(self, text_view):
    self.extended_view.did_end_editing()
    
  def textview_should_change(self, text_view, range, replacement):
      return True
      
  def textview_did_change(self, text_view):
      pass
      
  def textview_did_change_selection(self, text_view):
      pass                
      
class EnhancedView(ui.View):
  
  def __init__(self):
    
    self.subviews_enhanced = False
    self.current_text_element = None
    
  def did_begin_editing(self, text_element):
    self.current_text_element = text_element

  def did_end_editing(self):
    if self.current_text_element:
      self.current_text_element = None
    
  def enhance_subviews(self):
    if self.subviews_enhanced:
      return
    self.enhance_subviews_recursively(self)
    self.subviews_enhanced = True
    
  def enhance_subviews_recursively(self, view):
    """
    :type view: ui.View
    """
    if type(view).__name__ == 'TextField':
      view.delegate = EnhancedTextFieldDelegate(self)
      
    elif type(view).__name__ == 'TextView':
      view.delegate = EnhancedTextViewDelegate(self)
      
    else:
      for subview in view.subviews:
        self.enhance_subviews_recursively(subview)
        
  
  def keyboard_frame_did_change(self, frame):
    
    self.enhance_subviews()    
    kb_y = frame[1]
    kb_height = frame[3]
    
    if kb_y == 0 or not self.current_text_element:
      # keyboard inactive
        self.bounds = scene.Rect(self.bounds[0], 0, self.bounds[2], self.bounds[3])    
    else:
      # keyboard active
      top_y = get_absolute_y(self.current_text_element) + STATUS_ROW_HEIGHT
      lower_y = top_y + self.current_text_element.frame[3]
      delta_y = lower_y - kb_y
      if delta_y > 0:
        self.bounds = scene.Rect(self.bounds[0], delta_y, self.bounds[2], self.bounds[3])    
        