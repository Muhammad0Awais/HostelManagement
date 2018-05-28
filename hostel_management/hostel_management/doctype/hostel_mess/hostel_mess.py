# -*- coding: utf-8 -*-
# Copyright (c) 2018, Awais and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class HostelMess(Document):
	def validate(self):
		self.validate_mess()

	def validate_mess(self):
		found = []
		for mess in self.mess_menu:
			if mess.day in found:
				frappe.throw(_("Day {0} entered twice").format(mess.day))
			found.append(mess.day)
		if(len(found)!=7):
			frappe.throw(_("Please enter menu for whole week"))
