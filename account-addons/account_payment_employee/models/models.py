# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountPayment(models.Model):

	_inherit = "account.payment"

	paid_by_employee = fields.Boolean('Paid By Employee?', default=False)
	paid_by_employee_id = fields.Many2one('hr.employee', string="Paid By")
	employee_reimbursed = fields.Boolean('Employee Reimbursed?', default=False)

	@api.multi
	def reimburse_employee(self):
		self.employee_reimbursed = True
		return False

class EmployeePay(models.TransientModel):
	_name = "account.payment.employee"

	employee_id = fields.Many2one('hr.employee', string="Select Employee")

	@api.multi
	def load_employee_payments(self):
		return {
			'type': 'ir.actions.act_window',
			'res_model': 'account.payment',
			'view_type': 'form',
			'view_mode': 'tree,kanban,form,graph',
			'target': 'current',
			'domain': [
			('paid_by_employee_id','=',self.employee_id.id),
			('employee_reimbursed','=',False),
			],
		}