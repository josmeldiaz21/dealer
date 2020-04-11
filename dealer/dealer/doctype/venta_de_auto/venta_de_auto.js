// Copyright (c) 2020, Josmel Diaz and contributors
// For license information, please see license.txt

frappe.ui.form.on('Venta de Auto', {
	onload: function(frm) {
	 	frm.set_query("vehiculo", function() {
			return {
				"filters": {
					"item_group": "Vehiculo",
				}
			};
		});
	},
});

/*
frappe.ui.form.on('Venta de Auto', {
	 refresh: function(frm) {

	 }
});
*/