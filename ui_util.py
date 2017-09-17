# coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import six
import ui
import logging
import gc
import objc_util
import os

import log
import util
import spelling_mode
import defaults
import enhanced_view
import button_item_condenser

if six.PY3:
	from importlib import reload
	
reload(log)
reload(util)
reload(spelling_mode)
reload(defaults)
reload(enhanced_view)
reload(button_item_condenser)

SWITCH_PREFIX = "switch_"
BITSWITCH_PREFIX = "bitswitch_"
SEGMENTED_CONTROL_PREFIX = "segmented_control_"
SPLIT_CHAR = "|"
MAX_BITS = 8
NAVIGATION_VIEW_TITLE_HEIGHT = 64
PORTRAIT_SMALL_VIEW_HEIGHT = 480

global logger

logger = log.open_logging(__name__)

def is_iphone():
	return ui.get_screen_size().width < 768
	#return True
	
# see https://forum.omz-software.com/topic/2371/sub-views-of-navigationview-are-not-accessible
def get_navigationview_root(nv):
	return None
	o=[v for v in gc.get_objects() if hasattr(v,'navigation_view') and v.navigation_view==nv and not v.superview]
	print ("view %s has %d subviews" % (nv.name, len(o)))
	return o[0] if len(o) > 0 else None
	
def get_navigationview_subviews(nv):
	return None
	o=[v for v in gc.get_objects() if hasattr(v,'superview') and v.superview==nv]
	print ("view %s has %d subviews" % (nv.name, len(o)))
	return o
	
def store_in_model(sender, model):
	switch_name = sender.name
	
	if switch_name.startswith(SWITCH_PREFIX):
		util.set_container_value(model, switch_name, sender.value)
		
	elif switch_name.startswith(BITSWITCH_PREFIX):
		(switch_name, bit_value) = switch_name.split(SPLIT_CHAR)
		old_value = int(getattr(model, switch_name, None))
		util.set_container_value(model, switch_name, util.compute_bit_value(sender.value, old_value, int(bit_value)))
		
	elif switch_name.startswith(SEGMENTED_CONTROL_PREFIX):
		util.set_container_value(model, switch_name, sender.selected_index)
		
	else:
		return 0
		
	return 1
	
class ButtonItemAction(object):

	def __init__(self, view_controller, button_item):
		self.view_controller = view_controller
		self.button_item = button_item
		
	def handle_action(self, sender):
		self.view_controller.handle_action(self.button_item)
		
		
class TextFieldDelegate (object):

	def __init__(self, vc, name):
		self.vc = vc
		self.name = name
		
	def textfield_did_change(self, textfield):
		self.action = 'textfield_did_change'
		self.textfield = textfield
		self.vc.handle_action(self)
		
		
class ViewController (object):

	def __init__(self, parent_vc=None):
	
		self.parent_vc = parent_vc
		self.model = None
		self.child_controllers = {}
		self.view = None
		self.subview_map = {}
		self.warningWorkaroundIssued = False
		self.orientations = None
		self.button_items= {}
		
	def add_child_controller(self, view_name, child_controller):
	
		self.child_controllers[view_name] = child_controller
		view = child_controller.get_view()
		self.subview_map[view_name] = child_controller.get_view()
		
	def add_subview(self, parent_view_name, subview):
	
		global logger
		
		container_view = self.find_subview_by_name(parent_view_name)
		
		if not container_view:
			logger.warning("add_subview: cannot find parent view '%s'" % parent_view_name)
			return
			
		container_view.add_subview(subview)
		subview.width = container_view.width
		subview.height = container_view.height
		if type(subview).__name__ == 'NavigationView':
			subview.height = subview.height - NAVIGATION_VIEW_TITLE_HEIGHT
			
		container_view.add_subview(subview)
		
	def add_left_button_item(self, view_name, name, button_item):
	
		global logger
		
		view = self.find_subview_by_name(view_name)
		if view == None:
			logger.warning("add_left_button_item: cannot find view %s" % view_name)
			return
			
		button_item.action = ButtonItemAction(self, button_item).handle_action
		self.button_items[str(button_item)] = name
		
		if view.left_button_items == None:
			view.left_button_items = [ button_item ]
		else:
			new_list = list(view.left_button_items)
			new_list.append(button_item)
			view.left_button_items = new_list
			
			
	def add_right_button_item(self, view_name, name, button_item):
		global logger
		
		view = self.find_subview_by_name(view_name)
		if view == None:
			logger.warning("add_right_button_item: cannot find view %s" % view_name)
			return
			
		button_item.action = ButtonItemAction(self, button_item).handle_action
		self.button_items[str(button_item)] = name
		if view.right_button_items == None:
			view.right_button_items = [ button_item ]
		else:
			new_list = list(view.right_button_items)
			new_list.append(button_item)
			view.right_button_items = new_list
			
	def set_right_button_item_list(self, view_name, button_item_list):
		global logger
		
		view = self.find_subview_by_name(view_name)
		if view == None:
			logger.warning("add_right_button_item: cannot find view %s" % view_name)
			return
			
		self.condenser = button_item_condenser.ButtonItemCondenser(button_item_list,x_spacing=0)
		view.right_button_items = self.condenser.get_condensed_list()
		
	def load(self, view_name):
		self.view = ui.load_view(view_name)
		if self.parent_vc:
			self.parent_vc.add_child_controller(view_name, self)
			
	def get_view(self):
		return self.view
		
	def find_subview_by_name(self, name, first_level = True):
		global logger
		
		if name in self.subview_map:
			logger.debug("find_subview_by_name: found '%s' in cache" % name)
			return self.subview_map[name]
			
		if self.view is not None:
			logger.debug("find_subview_by_name: find %s in vc of view %s" % (name, self.view.name))
			descendant_view = self.find_subview_by_name2(self.view, name)
			if descendant_view is not None:
				self.subview_map[name] = descendant_view
				return descendant_view
				
		for child in self.child_controllers.values():
			descendant_view = child.find_subview_by_name(name, first_level = False)
			if descendant_view is not None:
				self.subview_map[name] = descendant_view
				return descendant_view
		
		if first_level:		
			logger.warn("find_subview_by_name: view '%s' not found!" % name)
			
		return None
		
	def find_subview_by_name2(self, view, name):
		if view is not None:
			#if "label" in view.name:
			#	print (view.name)
			if view.name == name:
				return view
			else:
				if type(view).__name__ == 'SegmentedControl':
					if not self.warningWorkaroundIssued:
						logger.warning("find_subview_by_name2: WORKAROUND: skipping iteration over subviews of SegmentedControl '%s'" % view.name)
						self.warningWorkaroundIssued = True
				else:
					if type(view).__name__ == 'NavigationView':
						subviews = get_navigationview_subviews(view)
					else:
						subviews = view.subviews
					if subviews:
						for subview in subviews:
							#if not name:
							#	continue
							descendent_view = self.find_subview_by_name2(subview, name)
							if descendent_view is not None:
								return descendent_view
		return None
		
		
	def handle_action(self, sender):
		global logger
		
		if type(sender).__name__ == 'ListDataSource':
			fmt = "handle_action: ListDataSource: %s"
			logger.debug(fmt % str(sender))
			return self.handle_list_data_source_action(sender)
			
		elif type(sender).__name__ == 'Button':
			fmt = "handle_action: Button: %s"
			logger.debug(fmt % sender.name)
			return self.handle_button_action(sender.name, sender)
			
		elif type(sender).__name__ == 'Switch':
			fmt = "handle_action: Switch: %s"
			logger.debug(fmt % sender.name)
			return self.handle_switch_action(sender)
			
		elif type(sender).__name__ == 'SegmentedControl':
			fmt = "handle_action: SegmentedControl: %s"
			logger.debug(fmt % sender.name)
			return self.handle_segmented_control_action(sender)
			
		elif type(sender).__name__ == 'TextFieldDelegate':
			fmt = "handle_action: TextFieldDelegate: %s"
			logger.debug(fmt % sender.name)
			return self.handle_textfield_action(sender)
			
		elif type(sender).__name__ == 'ButtonItem':
			if str(sender) in self.button_items:
				fmt = "handle_action: ButtonItem: %s"
				name = self.button_items[str(sender)]
				logger.debug(fmt % name)
				return self.handle_button_action(name, sender)
				
			elif sender.title:
				fmt = "handle_action: ButtonItem: %s"
				name = sender.title
				logger.debug(fmt % name)
				return self.handle_button_action(name, sender)
				
			else:
				fmt = "handle_action: ButtonItem: unknown class instance '%s'"
				logger.warning(fmt % str(sender))
				
		else:
			fmt = "handle_action: unknown class '%s'"
			logger.warning(fmt % type(sender).__name__)
			
		return 0
		
	def handle_named_action(self, name):
	
		if self.parent_vc:
			return self.parent_vc.handle_named_action(name)
			
		fmt = "handle_named_action: action '%s' not handled"
		logger.warning(fmt % name)
		
	def handle_button_action(self, name, sender):
		global logger
		
		if self.parent_vc:
			return self.parent_vc.handle_button_action(name, sender)
			
		fmt = "handle_button_action: button '%s' not handled"
		logger.warning(fmt % name)
		
	def handle_switch_action(self, sender):
		global logger
		
		if self.parent_vc:
			return self.parent_vc.handle_switch_action(sender)
			
		fmt = "handle_switch_action: switch '%s' not handled"
		logger.warning(fmt % sender.name)
		
	def handle_segmented_control_action(self, sender):
		global logger
		
		if self.parent_vc:
			return self.parent_vc.handle_segmented_control_action(sender)
			
		fmt = "handle_segmented_control_action: control '%s' not handled"
		logger.warning(fmt % sender.name)
		
	def handle_list_data_source_action(self, sender):
	
		if self.parent_vc:
			return self.parent_vc.handle_list_data_source_action(sender)
			
		fmt = "handle_list_data_source_action: not handled"
		logger.warning(fmt)
		
	def handle_textfield_action(self, sender):
	
		if self.parent_vc:
			return self.parent_vc.handle_textfield_action(sender)
			
		fmt = "handle_textfield_action: not handled"
		logger.warning(fmt)
		
	def present(self, style='popover', title=None, orientations=None, title_bar_color=None):
		global logger
		
		self.view.present(style=style, title_bar_color=title_bar_color, orientations=orientations if orientations else self.orientations)
		
		try:
			self.view.wait_modal()
			
		except Exception as e:
			logger.error("Exception '%s' caught" % str(e))
			self.view.close()
			
	def retrieve_from_model(self, p_model = None):
		global logger
		
		if p_model is not None:
			model = p_model
		
		else:
			model = self.model

		for att in model.__dict__:
			
			if att.startswith(SWITCH_PREFIX):
				view = self.find_subview_by_name(att)
				if view:
					view.value = getattr(model, att)

				else:
					logger.warning("retrieve_from_model: no view found for switch attribute '%s'" % att)
					
			elif att.startswith(BITSWITCH_PREFIX):
				bit = 1
				found = False
				for i in range(0, MAX_BITS):
					viewname = "%s|%d" % (att, bit)
					view = self.find_subview_by_name(viewname)
					if view != None:
						view.value = bool(getattr(model, att) & bit)
						found = True
					bit = bit * 2
				if not found:
					logger.warning("retrieve_from_model: no view found for BIT switch attribute '%s'" % att)
					
			elif att.startswith(SEGMENTED_CONTROL_PREFIX):
				view = self.find_subview_by_name(att)
				if view != None:
					view.selected_index = getattr(model, att)
				else:
					logger.warning("retrieve_from_model: no view found for segmented control attribute '%s'" % att)
					
			else:
				logger.debug("retrieve_from_model: unsupported attribute prefix in attribute '%s'" % att)
				
				
	def set_model(self, model, retrieve=True):
	
		self.model = model
		if retrieve:
			self.retrieve_from_model()
			
class NavigationViewController(ViewController):

	def __init__(self, parent_vc):
	
		super(NavigationViewController, self).__init__(parent_vc)
		
def get_document_directory():
	
	f = objc_util.ObjCClass('NSFileManager').defaultManager()
	return str(f.URLsForDirectory_inDomains_(9,1)[0].path())
		
def test():

	print(os.getcwd())
	print(get_document_directory())
	model = spelling_mode.spelling_mode()
	vc = ViewController()
	vc.set_model(model)
	
if __name__ == '__main__':
	test()

