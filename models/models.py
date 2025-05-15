# -*- coding: utf-8 -*-

from odoo import models, fields 


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    state_property_ids = fields.One2many(
        'bidcom_state_property',
        'partner_id',
    )
