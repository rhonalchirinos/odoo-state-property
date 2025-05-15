# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BidcomRegionalization(models.Model):
    _name = 'bidcom_regionalization'
    _description = 'Regionalizacion for bidcom... :-)'

    name = fields.Char()
    value = fields.Integer()
    description = fields.Text()
