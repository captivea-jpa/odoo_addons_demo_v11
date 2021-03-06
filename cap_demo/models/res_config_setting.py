# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging
from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ResConfiguration(models.TransientModel):
    _inherit = 'res.config.settings'
    
    # SALE
    group_product_variant = fields.Boolean(default=1)
    group_uom = fields.Boolean(default=1)
    multi_sales_price_method = fields.Selection(default='formula')
    group_sale_layout = fields.Boolean(default=1)
    group_route_so_lines = fields.Boolean(default=1)
    
    group_discount_per_so_line = fields.Boolean(default=1)
    portal_confirmation = fields.Boolean(default=1)
    portal_confirmation_options = fields.Selection(default='sign')
    module_sale_payment = fields.Boolean(default=1)

    # STOCK
    group_stock_packaging = fields.Boolean(default=1)    
    module_stock_barcode = fields.Boolean(default=1)
    module_stock_picking_batch = fields.Boolean(default=1)

    # INVOICE
    module_account_sepa = fields.Boolean(default=1)
    module_account_sepa_direct_debit = fields.Boolean(default=1)
    module_account_payment = fields.Boolean(default=1)
    

    # WEBSITE
    language_ids = fields.Many2many(default=lambda self: self.env['res.lang'].search([('code','=','fr_FR')]))
