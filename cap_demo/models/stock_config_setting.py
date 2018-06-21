# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class StockSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    
    # Inherit field
    group_stock_packaging = fields.Boolean(default=1)