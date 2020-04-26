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
		}),
		frappe.call({
			type: "GET",
			method: "dealer.dealer.doctype.venta_de_auto.venta_de_auto.set_valores_por_defecto",
			callback: function(r) {
				// alert("josmel")
				if (!this.frm.doc.porcentaje) {
					frm.set_value("porcentaje", r.message.p);
					alert(r.exc);
				}
			}
		})
	},
	refresh: function(frm){
		// frm.fields_dict['tab_datasheet'].grid.add_custom_button('label', () => {console.log("custom button press");})
		frm.trigger('mostrar_progreso_de_pagos');
	},
	mostrar_progreso_de_pagos: function(frm) {
		let bars = [];
		let message = '';
		let added_min = false;

		// completed sessions
		let title = __('2 payments');

		title += __(' de 10');

		bars.push({
			'title': title,
			'width': '10%',
			'progress_class': 'progress-bar-success',
		});
		if (bars[0].width == '0%') {
			bars[0].width = '0.5%';
			added_min = 0.5;
		}
		message = title;
		frm.dashboard.add_progress(__('Status'), bars, message);
	},

	vehiculo: function(frm, cdt, cdn) {
		frappe.call({
			type: "GET",
			method: "dealer.dealer.doctype.venta_de_auto.venta_de_auto.precio_vehiculo",
			args: {"item_code": frm.doc.vehiculo},
			callback: function(r) {
				if (frm.doc.vehiculo) {
					frm.set_value("precio", r.message);
				}
			}
		})
	}

});
frappe.ui.form.on('Cuotas de Pago', {
	cantidad: function(frm) {
		let total = 0;
		$.each(frm.doc.cuotas_de_pago, function(_i, e) {
			total += e.cantidad;
		});
		frm.set_value('total_a_pagar', total);
		refresh_field('total_a_pagar');
	}
});


