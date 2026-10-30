# Copyright (c) 2026, Greycube Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class EMDSettings(Document):
	pass


def get_emd_voucher_type():
	return frappe.db.get_single_value("EMD Settings", "voucher_type") or "Journal Entry"
