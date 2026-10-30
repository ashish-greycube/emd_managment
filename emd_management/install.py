from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def after_install():
	make_custom_fields()


def after_migrate():
	make_custom_fields()


def make_custom_fields():
	create_custom_fields(
		{
			"Journal Entry": [
				{
					"fieldname": "is_emd_entry",
					"label": "Is EMD Entry?",
					"fieldtype": "Check",
					"insert_after": "voucher_type",
				}
			]
		},
		update=True,
	)
