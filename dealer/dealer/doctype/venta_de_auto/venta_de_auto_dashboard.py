from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'fieldname': 'vehiculo',
		'transactions': [
			{
				'label': _('Pagos Realizados'),
				'items': ['Payment Entry']
			}
		]
	}