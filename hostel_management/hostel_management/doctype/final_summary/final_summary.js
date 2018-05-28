// Copyright (c) 2018, Awais and contributors
// For license information, please see license.txt

frappe.ui.form.on('Final Summary', {
	refresh: function(frm) {

	},
	hostel : function(frm, cdt, cdn){
		var hostel=frappe.model.get_doc(cdt,cdn);
		frm.call({
				method:"hostel_management.hostel_management.doctype.final_summary.final_summary.infilate_data",
				args: { hostel: hostel.hostel},
				callback : function(r)
				{
					frappe.model.set_value(cdt,cdn,"total_strength",r.message['totalstrength'])
					frappe.model.set_value(cdt,cdn,"allocated_rooms",r.message['Allocated_rooms'])
					frappe.model.set_value(cdt,cdn,"students_residing",r.message['Students_Residing'])
					frappe.model.set_value(cdt,cdn,"total_fee_collected",r.message['fee_collected'])
					frappe.model.set_value(cdt,cdn,"total_employees",r.message['Total_Employees'])
					frappe.model.set_value(cdt,cdn,"total_salary_paid",r.message['salary_paid'])
				}
			});
	}
});
