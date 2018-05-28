# -*- coding: utf-8 -*-
# Copyright (c) 2018, Awais and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class RoomAllocation(Document):
	def validate(self):
		self.page_name = self.name.lower()
		self.validate_allotment()

	def validate_allotment(self):
		found = []
		room=self.room
		room_obj = frappe.db.sql(''' select COUNT(*) from `tabRoom Allocation` 
						where room=%(room)s''', {
						"room": room
						}, as_dict=True)
		room_capacity=frappe.db.sql(''' select room_strength from `tabHostel Room`
					    where name=%(room)s''', {
						"room": room
						}, as_dict=True)
		allocated_rooms=room_obj[0]['COUNT(*)']
		room_strength=room_capacity[0]['room_strength']
		if not allocated_rooms<=room_strength-1:
			frappe.throw(_("This room is full"))
