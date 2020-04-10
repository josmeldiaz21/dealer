from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("Dealer"),
        "icon": "octicon octicon-briefcase",
        "items": [
            {
              "type": "doctype",
              "name": "Venta de Auto",
              "label": _("Venta de Auto"),
              "description": _("Vehicles sold")
            }
          ]
      },
      {
        "label":_("Configuracion"),
        "icon": "octicon octicon-briefcase",
        "items": [
            {
              "type": "doctype",
              "name": "Configuracion de Dealer",
              "label": _("Configuracion de Dealer"),
              "description": _("Config")
            }
          ]
      }

  ]