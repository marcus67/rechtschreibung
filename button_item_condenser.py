# coding: utf-8
# This file is part of https://github.com/marcus67/rechtschreibung

import ui
from objc_util import *

DEFAULT_X_SPACING = 8
DEFAULT_HEIGHT = 44

class ButtonItemAction (object):

	def __init__(self, buttonItem):
		'''
		:type buttonItem: ui.ButtonItem
		'''
		self.buttonItem = buttonItem
		
	def handle_action(self, sender):
		'''
		:type sender: ui.ButtonItem
		'''
		self.buttonItem.action(self.buttonItem)
		
class ButtonItemCondenser (object):

	def __init__(self, button_item_list, x_spacing=DEFAULT_X_SPACING):
	
		self.button_item_list = button_item_list
		self.x_spacing = x_spacing
		self.condensed_list = None
		self.buttons = []
		self.btn_container = None
		
	def get_condensed_list(self):
	
		if self.condensed_list:
			return self.condensed_list
			
		i = 0
		x = 0
		self.btn_container = ui.View(name='button container view')
		
		for button_item in self.button_item_list:
			btn = ui.Button(image=button_item.image)
			self.buttons.append(btn)
			btn.action = ButtonItemAction(button_item).handle_action
			width = button_item.image.size[0]
			btn.frame = (x, 0, width, DEFAULT_HEIGHT)
			x = x + width + self.x_spacing
			self.btn_container.add_subview(btn)
			i = i + 1
			
		x = x - self.x_spacing
		self.btn_container.frame = (0, 0, x , DEFAULT_HEIGHT)
		btn_item = ui.ButtonItem()
		
		# The followinf ObjCInstance calls allow access to the container view of the ButtonItem.
		# It will be replaced by the view containing the Buttons instead.
		# See https://forum.omz-software.com/topic/2724/spacing-of-buttonitem-s
		btn_item_objc = ObjCInstance(btn_item)
		custom_view = ObjCInstance(self.btn_container)
		btn_item_objc.customView = custom_view
		
		self.condensed_list = [btn_item]
		return self.condensed_list
		
def test_handle_action(sender):
	print ("sender=%s" % str(sender))
	print ("sender.title=%s" % sender.title)
	
def test():
	icon_names = [ 'iob:beaker_32', 'iob:beer_32', 'iob:bag_32' ]
	button_item_list = map(lambda name : ui.ButtonItem(image=ui.Image.named(name), action=test_handle_action, title=name), icon_names)
	condenser = ButtonItemCondenser(button_item_list)
	v = ui.View(frame=(0, 0, 400, 400), name='Demo')
	v.background_color = 'white'
	condensed_list = condenser.get_condensed_list()
	v.right_button_items = condensed_list
	
	# The following assignment prevents the instance of ButtonItemCondenser to be garbage collected.
	# See https://forum.omz-software.com/topic/2724/spacing-of-buttonitem-s
	v.condenser = condenser
	
	v.present('sheet')
	
if __name__ == '__main__':
	test()

