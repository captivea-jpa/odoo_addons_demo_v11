# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging
from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class SaleConfiguration(models.Model):
    _inherit = 'res.partner'
    
    @api.model
    def force_lang(self,lang='fr_FR'):
        for partner in self.env['res.partner'].search([]):
            partner.lang = lang
        