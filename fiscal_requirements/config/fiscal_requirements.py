from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Num Lines Invoice"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Num Lines Invoice",
					"description": _("Num Lines Invoice.")
				}
            ]
        }
    ]