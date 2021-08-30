# Copyright (c) 2021, Dharshini and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import date
from frappe.utils import date_diff

class TenantDetails(Document):
	def validate(self):
		fromdate=self.dateofin
		todate=self.dateofout
		tot=date_diff(fromdate, todate)
		self.totaldays=abs(int(tot))
		self.amountpaid_upto_dateout=abs(int(tot))*self.monthly_rent
	pass
	
