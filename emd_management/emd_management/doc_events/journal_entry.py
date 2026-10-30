import frappe
from frappe import _


def on_cancel(self, method):
    if not self.is_emd_entry:
        return

    emd = None
    if self.cheque_no:
        emd = frappe.db.get_value(
            "EMD",
            {"reference_num": self.cheque_no},
            ["name", "return_journal_entry", "return_forfeited_entry"],
            as_dict=True,
        )

    if not emd:
        frappe.msgprint(
            _("Is EMD Entry? is checked, but no connected EMD was found for Cheque No {0}.").format(
                self.cheque_no or "-"
            ),
            indicator="orange",
            alert=True,
        )
        return

    if emd.return_journal_entry or emd.return_forfeited_entry:
        frappe.db.set_value("EMD", emd.name, "journal_entry", None)
