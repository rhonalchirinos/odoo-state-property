# -*- coding: utf-8 -*-

from odoo import models, fields


class BidcomStatePropertyType(models.Model):
    _name = 'bidcom_state_property_type'
    _description = 'State Property Type'
    _order = "name desc"

    name = fields.Char(string='Type', required=True)
    description = fields.Text(string='Description')
