# -*- coding: utf-8 -*-

from odoo import models, fields

from random import randint


class BidcomStatePropertyTag(models.Model):
    _name = 'bidcom_state_property_tag'
    _description = 'State Property Tag'
    _order = "name desc"

    name = fields.Char(string='Type', required=True)
    color = fields.Char(string='Color', required=False)

    def _default_color(self):
        return randint(1, 11)

    color = fields.Integer(
        string='Color Index', default=lambda self: self._default_color(),
        help='Tag color. No color means no display in kanban or front-end, to distinguish internal tags from public categorization tags.')

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'The tag name already created'),
    ]
