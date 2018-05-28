// Copyright (c) 2018, Awais and contributors
// For license information, please see license.txt

frappe.ui.form.on('Hostel Room', {
	refresh: function(frm) {

	},
	building : function(frm, cdt, cdn){
		var building=frappe.model.get_doc(cdt,cdn);
		frm.call({
				method:"hostel_management.hostel_management.doctype.hostel_room.hostel_room.validate_floors",
				args: { building: building.building},
				callback : function(r)
				{
					var arr=Array.apply(null, {length: r.message}).map(Function.call,Number);
					var arr1=[1,2,3,4];
					//frappe.model.set_value(cdt,cdn,"floor",r.object);
					frm.set_df_property('floor', 'options', arr);
					frm.refresh_field('floor');
				}
			});
	}
});
