# -*- coding: utf-8 -*-
# Copyright (c) 2018, Awais and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class SalaryPayment(Document):
	def validate(self):
		self.validate_salary()

	def validate_salary(self):
		found = []
		sal_obj = frappe.db.sql(''' select employee_name, month from `tabSalary Payment` ''')
		#frappe.msgprint(_(sal_obj))
		for sal in sal_obj:
			#frappe.throw(_(sal[0]))
			if sal[0]==self.employee_name and sal[1]==self.month:
				frappe.throw(_("Salary for this month is already paid"))
