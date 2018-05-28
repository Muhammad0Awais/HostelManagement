# -*- coding: utf-8 -*-
# Copyright (c) 2018, Awais and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class HostelRoom(Document):
	def validate(self):
		self.validate_rooms()

	def validate_rooms(self):
		building=self.building
		room_obj = frappe.db.sql(''' select COUNT(*) from `tabHostel Room` 
						where building=%(building)s''', {
						"building": building
						}, as_dict=True)
		number_of_rooms=frappe.db.sql(''' select number_of_rooms from `tabBuilding`
					    where name=%(building)s''', {
						"building": building
						}, as_dict=True)
		developed_rooms=room_obj[0]['COUNT(*)']
		total_rooms=number_of_rooms[0]['number_of_rooms']
		if not developed_rooms<=total_rooms-1:
			frappe.throw(_("Limit of rooms has been exceeded"))

@frappe.whitelist()
def validate_floors(building):
	#total_floors = frappe.db.sql(''' select COUNT(*) from `tabFloor` ''')
	available_floors=frappe.db.sql(''' select number_of_floors from `tabBuilding`
				    where name=%(building)s''', {
					"building": building
					}, as_dict=True)
	#total_floors=total_floors[0]['COUNT(*)']
	available_floors=available_floors[0]['number_of_floors']
	frappe.msgprint(_(available_floors))
	return available_floors
