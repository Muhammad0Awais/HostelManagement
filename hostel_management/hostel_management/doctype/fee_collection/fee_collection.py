# -*- coding: utf-8 -*-
# Copyright (c) 2018, Awais and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class FeeCollection(Document):
	def validate(self):
		self.validate_fee()

	def validate_fee(self):
		found = []
		sal_obj = frappe.db.sql(''' select resident, month from `tabFee Collection` ''')
		#frappe.msgprint(_(sal_obj))
		for sal in sal_obj:
			#frappe.throw(_(sal[0]))
			if sal[0]==self.resident and sal[1]==self.month:
				frappe.throw(_("Fee for this month is already paid"))

@frappe.whitelist()
def get_fee(resident):
	mess_required=frappe.db.sql(''' select need_mess from `tabRoom Allocation`
				    where name=%(resident)s''', {
					"resident": resident
					}, as_dict=True)
	mess=mess_required[0]['need_mess']
	if mess==0:
		return (12000)
	else:
		return (12000+5000)
	
