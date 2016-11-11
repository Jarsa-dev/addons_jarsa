# -*- coding: utf-8 -*-
# <2016> <Jarsa Sistemas, S.A. de C.V.>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Report Sale',
    'version': '9.0.1.0.0',
    'author': (
        'Jarsa Sistemas, S.A de C.V., Odoo Community Association (OCA)'),
    'description': 'This module is to report sale',
    'website': 'https://www.jarsa.com.mx',
    'category': 'Purchase',
    'license': 'AGPL-3',
    'depends': [
        'purchase',
    ],
    'data': [
        "wizard/wizard_purchase_report_view.xml",
        "report/report.xml",
    ],
    'installable': True,
    'active': True,
}
