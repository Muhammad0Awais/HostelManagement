# -*- coding: utf-8 -*-
# Copyright (c) 2018, Awais and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class Hostel(Document):
	def validate(self):
		pass


@frappe.whitelist()
def check_rooms(rooms):
	t_rooms=rooms
	tt=12
	frappe.throw(_(tt))
	if not t_rooms==tt:
		frappe.throw(_("Not validated"))

@frappe.whitelist()
def find_strength(doc):
	'''t_strength=doc.1_bed+(doc.2_bed*2)+(doc.3_bed*3)+(doc.4_bed*4)+(doc.5_bed*5)
	return t_strength'''
