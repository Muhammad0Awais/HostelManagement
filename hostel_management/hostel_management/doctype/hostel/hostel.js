// Copyright (c) 2018, Awais and contributors
// For license information, please see license.txt

frappe.ui.form.on('Hostel', {
	refresh: function(frm) {
		
	},
	validate_rooms: function(frm,cdt,cdn) {
		frappe.call({
				method: "hostel_management.hostel_management.doctype.hostel.hostel.check_rooms",
				args :{
					rooms: frm.doc.rooms
				}
			});
		/*var rooms=parseInt(frm.doc.rooms);
		console.log((rooms));
		var 1_bed=parseInt(frm.doc.1_bed);
		console.log((1_bed));
		var total_rooms=frm.doc.1_bed+frm.doc.2_bed+frm.doc.3_bed+frm.doc.4_bed+frm.doc.5_bed;
		if(rooms<total)
		{
			frappe.throw(_("There are less rooms"));
		}
		else if(rooms>total)
		{
			frappe.throw(_("There are unallocated rooms"));
		}*/
	},
	find_strength: function(frm) {
			frm.call({
				method:"hostel_management.hostel_management.doctype.hostel.hostel.find_strength",
				args: { doc: frm.doc},
				callback : function(r)
				{
					frappe.model.set_value("total_strength",r.message);
				}
			});
			//var total_space=frm.doc.1_bed+(frm.doc.2_bed*2)+(frm.doc.3_bed*3)+(frm.doc.4_bed*4)+(frm.doc.5_bed*5)
			//frappe.model.set_value("total_strength",total_space);
		}
});

frappe.ui.form.on('Hostel Room',{
	validate_rooms: function(frm,cdt,cdn) {
			var rooms=frappe.model.get_doc(cdt,cdn);
			if (rooms.room)
			{
				frm.call({
					method: "hostel_management.hostel_management.doctype.hostel.hostel.check_rooms",
					args: { attendee: attendee.attendee},
					callback : function(r)
					{
						frappe.model.set_value(cdt,cdn,"full_name",r.message);
					}
				});
			} else{
				frappe.model.set_value(cdt,cdn, "full_name", null);
			}
	}
});


