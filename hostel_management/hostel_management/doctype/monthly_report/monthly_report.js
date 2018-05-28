// Copyright (c) 2018, Awais and contributors
// For license information, please see license.txt

frappe.ui.form.on('Monthly Report', {
	refresh: function(frm) {

	},
	month : function(frm, cdt,cdn){
		var hostel=frappe.model.get_doc(cdt,cdn);
		frm.call({
			method:"hostel_management.hostel_management.doctype.monthly_report.monthly_report.infilate_data",
			args: {
				month:frm.doc.month,
				hostel:hostel.hostel				
			},
			callback : function(r)
			{
				frappe.model.set_value(cdt,cdn,"fee_collected",r.message['fee_collected'])
				frappe.model.set_value(cdt,cdn,"salary_paid",r.message['salary_paid'])
			}
		});
	}
});
