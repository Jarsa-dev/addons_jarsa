# -*- coding: utf-8 -*-
# Copyright <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import datetime
from openerp import api, fields, models


class WizardPurchaseReport(models.TransientModel):
    _name = 'wizard.purchase.report'

    date_start = fields.Datetime('Date Start', default=fields.Datetime.now)
    date_end = fields.Datetime('Date End', default=fields.Datetime.now)

    @api.multi
    def print_report_purchase(self):
        for rec in self:
            date_start = datetime.datetime.strftime(
                datetime.datetime.strptime(
                    rec.date_start, "%Y-%m-%d %H:%M:%S"), "%Y-%m-%d 00:00:01")
            date_end = datetime.datetime.strftime(
                datetime.datetime.strptime(
                    rec.date_end, "%Y-%m-%d %H:%M:%S"), "%Y-%m-%d 00:59:59")
            purchase_ids = rec.env['purchase.order'].search(
                [('date_order', '<', date_end),
                 ('date_order', '>=', date_start)])

            context = dict(
                self.env.context or {},
                active_ids=[x.id for x in purchase_ids],
                active_model='purchase.order')
            return {
                'type': 'ir.actions.report.xml',
                'report_name': 'report_print.report_purchase',
                'context': context,
                'docs': [x.id for x in purchase_ids]
            }
