# -*- coding: utf-8 -*-
# Copyright (c) 2020, Josmel Diaz and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class VentadeAuto(Document):
	def before_insert(self):
		pass
		#porc = frappe.db.get_single_value("Configuracion de Dealer", "porcentaje_por_defecto")
		#frappe.throw(_("Percentaje: {0}").format(porc))
	def validate(self):
		self.crear_tabla_cuotas()
		self.set_totales()
	def crear_tabla_cuotas(self):
		ac = 0
		meses = int(self.annos) * int(12)
		cuota = self.porcentaje * self.precio
		for c in range(meses):
			ac = ac + cuota
			
			self.append("cuotas_de_pago", {
				"nombre": "Cuota " + str(c+1),
				"cantidad": cuota,
				"acumulado": ac
				})
	def set_totales(self):
		total_cuotas = int("10")
		#self.db_set('cantidad_de_cuotas', total_cuotas)

@frappe.whitelist()
def set_valores_por_defecto():
	#frappe.msgprint("Prueba desde Funcion whitelist en venta_de_auto.py")
	porc = frappe.db.get_single_value("Configuracion de Dealer", "porcentaje_por_defecto")
	return porc
	# return {
	# 	"p": porc,
	# 	"cantidad": "2111",
	# }
@frappe.whitelist()
def precio_vehiculo(item_code):
	a = frappe.db.get_value("Item Price", {"item_code": item_code, "price_list": "Venta estándar"}, "price_list_rate")
	return a