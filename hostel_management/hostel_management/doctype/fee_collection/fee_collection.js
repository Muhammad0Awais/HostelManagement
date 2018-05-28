// Copyright (c) 2018, Awais and contributors
// For license information, please see license.txt

frappe.ui.form.on('Fee Collection', {
	refresh: function(frm) {
		
	},
	resident: function(frm, cdt, cdn){
		var resident=frappe.model.get_doc(cdt,cdn);
		if (resident.resident)
		{
			frm.call({
				method:"hostel_management.hostel_management.doctype.fee_collection.fee_collection.get_fee",
				args: { resident: resident.resident},
				callback : function(r)
				{
					frappe.model.set_value(cdt,cdn,"fee",r.message);
				}
			});
		} else{
			frappe.model.set_value(cdt,cdn, "fee", null);
		}
	},
});
