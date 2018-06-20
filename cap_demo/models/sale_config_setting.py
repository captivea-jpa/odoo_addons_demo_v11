# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class SaleConfiguration(models.TransientModel):
    _inherit = 'sale.config.settings'
    
    # Inherit field
    group_product_variant = fields.Selection(default=1)
    group_uom = fields.Selection(default=1)
    sale_pricelist_setting = fields.Selection(default='formula')
    group_sale_layout = fields.Selection(default=1)
    group_route_so_lines = fields.Selection(default=1)
    
#     @api.model
#     def set_default_demo_values(self):
#         print "set_default_demo_value"
#         print self
#         obj_id = self.create({})
#         obj_id.update({'group_sale_layout':1})
#         print obj_id.group_sale_layout
#         
#         
#         IrValues = self.env['ir.values']
#         IrValues.set_default('sales.config.settings', 'group_product_variant', 1)
#         IrValues.set_default('sales.config.settings', 'group_uom', 1)
#         IrValues.set_default('sales.config.settings', 'sale_pricelist_setting', "formula")
#         IrValues.set_default('sales.config.settings', 'module_sale_margin', 1)
#         IrValues.set_default('sales.config.settings', 'module_website_quote', 1)
#         IrValues.set_default('sales.config.settings', 'module_website_sign', True)
#         IrValues.set_default('sales.config.settings', 'group_sale_layout', 1)
#         IrValues.set_default('sales.config.settings', 'group_route_so_lines', 1)
