# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Fiscal Requirements",
			"category": "Modules",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Fiscal Requirements"),
			"description": "Fiscal Requirements for Company"
		}
	]
