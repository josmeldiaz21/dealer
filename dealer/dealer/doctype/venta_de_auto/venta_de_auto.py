# -*- coding: utf-8 -*-
# Copyright (c) 2020, Josmel Diaz and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document


class VentadeAuto(Document):
	def before_insert(self):
		porc = frappe.db.get_single_value("Configuracion de Dealer", "porcentaje_por_defecto")
		frappe.throw(_("Percentaje: {0}").format(porc))
