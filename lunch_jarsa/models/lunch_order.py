# -*- coding: utf-8 -*-
# Copyright 2016, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from openerp import api, fields, models


class LunchOrder(models.Model):
    _inherit = 'lunch.order'

    @api.one
    @api.depends('order_line_ids')
    def _compute_total(self):
        self.total = sum(
            orderline.total for orderline in self.order_line_ids)
