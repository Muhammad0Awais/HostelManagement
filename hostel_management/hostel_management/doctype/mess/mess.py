# -*- coding: utf-8 -*-
# Copyright (c) 2018, Awais and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _
from frappe.website.website_generator import WebsiteGenerator

class Mess(WebsiteGenerator):
	website = frappe._dict(
		template = "templates/generators/mess.html"
	)
	
	def validate(self):
		self.page_name = self.name.lower()
		#self.validate_mess()

	def validate_mess(self):
		found = []
		for mess in self.mess_menu:
			if mess.day in found:
				frappe.throw(_("Day {0} entered twice").format(mess.day))
			found.append(mess.day)
