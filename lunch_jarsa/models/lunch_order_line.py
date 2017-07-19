# -*- coding: utf-8 -*-
# Copyright 2017, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from openerp import api, fields, models


class LunchOrderLine(models.Model):
    _inherit = 'lunch.order.line'

    quantity = fields.Float(
        string='Quantity',
        default=1.0,
    )
    total = fields.Float(
        string='Total',
        compute='compute_total',
    )

    @api.depends('price', 'quantity')
    def compute_total(self):
        for rec in self:
            rec.total = rec.price * rec.quantity
