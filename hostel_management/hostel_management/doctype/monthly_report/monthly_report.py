# -*- coding: utf-8 -*-
# Copyright (c) 2018, Awais and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class MonthlyReport(Document):
	pass

@frappe.whitelist()
def infilate_data(hostel,month):
	fee_collected=0
	salary_paid=0
	fee=frappe.db.sql(''' select fee from `tabFee Collection`
				    where room in (select room from `tabHostel Room` 
					where building=%(hostel)s) and month=%(month)s''', {
					"hostel": hostel,
					"month":month
					}, as_dict=True)
	
	for fees in fee:
		fee_collected+=int(fees['fee'])
	#frappe.msgprint(_(fee_collected))

	salary=frappe.db.sql('''  select salary from `tabSalary Payment`
				    where employee in (select employee from `tabEmployee` 
					where building=%(hostel)s) and month=%(month)s''', {
					"hostel": hostel,
					"month":month
					}, as_dict=True)
	
	for sal in salary:
		salary_paid+=int(sal['salary'])
	#frappe.msgprint(_(salary_paid))

	return {"fee_collected":fee_collected,"salary_paid":salary_paid}
