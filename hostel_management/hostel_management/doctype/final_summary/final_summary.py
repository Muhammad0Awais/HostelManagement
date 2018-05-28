# -*- coding: utf-8 -*-
# Copyright (c) 2018, Awais and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class FinalSummary(Document):
	pass


@frappe.whitelist()
def infilate_data(hostel):
	totalstrength=0
	fee_collected=0
	salary_paid=0
	strength=frappe.db.sql(''' select room_strength from `tabHostel Room`
				    where building=%(hostel)s''', {
					"hostel": hostel
					}, as_dict=True)
	for r in strength:
		totalstrength+=r['room_strength']
	
	Allocated_rooms=frappe.db.sql(''' select COUNT(DISTINCT room) from `tabRoom Allocation`
				    where room in (select room from `tabHostel Room` 
					where building=%(hostel)s)''', {
					"hostel": hostel
					}, as_dict=True)
	
	Students_Residing=frappe.db.sql(''' select COUNT(*) from `tabRoom Allocation`
				    where room in (select room from `tabHostel Room` 
					where building=%(hostel)s)''', {
					"hostel": hostel
					}, as_dict=True)
	
	Total_Fee=frappe.db.sql(''' select fee from `tabFee Collection`
				    where room in (select room from `tabHostel Room` 
					where building=%(hostel)s)''', {
					"hostel": hostel
					}, as_dict=True)
	
	for r in Total_Fee:
		fee_collected+=int(r['fee'])
	
	Total_Employees=frappe.db.sql(''' select COUNT(*) from `tabEmployee`
				    where building=%(hostel)s''', {
					"hostel": hostel
					}, as_dict=True)
	
	Total_Salary=frappe.db.sql(''' select salary from `tabSalary Payment`
				    where employee in (select employee from `tabEmployee` 
					where building=%(hostel)s)''', {
					"hostel": hostel
					}, as_dict=True)
	
	for r in Total_Salary:
		salary_paid+=int(r['salary'])
	
	return {"totalstrength" :totalstrength, "Allocated_rooms":Allocated_rooms[0]['COUNT(DISTINCT room)'],"Students_Residing":Students_Residing[0]['COUNT(*)'],"fee_collected":fee_collected,"Total_Employees":Total_Employees[0]['COUNT(*)'],"salary_paid":salary_paid}
	
	
