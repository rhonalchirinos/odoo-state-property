# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from odoo.tools.float_utils import float_compare, float_is_zero


class BidcomStateProperty(models.Model):
    _name = 'bidcom_state_property'
    _description = 'State Property'
    _order = "id desc"

    name = fields.Char(string='State', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Date Availability')
    expected_price = fields.Float(string='Expected Price')
    selling_price = fields.Float(string='Selling Price')
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Float(string='Living Area')
    facades = fields.Integer(string='Facades')

    has_garden = fields.Boolean(string='Has Garden')
    garage = fields.Integer(string='Garage')
    garden_area = fields.Float(string='Garden Area')
    garden_orientation = fields.Selection(
        [
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West'),
        ],
        string='Garden Orientation'
    )

    state = fields.Selection(
        [
            ('new', 'New'),
            ('offer received', 'Offer Received'),
            ('offer accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('cancelled', 'Cancelled'),
        ],
        string='Status', default='new'
    )

    active = fields.Boolean(string='Active', default=True)

    best_offer = fields.Float(
        compute="_compute_best_offer",
        string='Best Offer Price'
    )

    total_area = fields.Float(
        compute="_compute_total_area",
        string='Total Area'
    )

    # Related fields

    property_type_id = fields.Many2one(
        "bidcom_state_property_type",
        string="Property Type"
    )

    user_id = fields.Many2one(
        'res.users',
        string='Salesperson',
        index=True,
        tracking=True,
        default=lambda self: self.env.user
    )

    partner_id = fields.Many2one(
        "res.partner",
        string="Buyer"
    )

    tax_ids = fields.Many2many(
        "account.tax",
        string="Taxes"
    )

    tag_ids = fields.Many2many(
        "bidcom_state_property_tag",
        string="Tags"
    )

    offer_ids = fields.One2many(
        "bidcom_state_property_offer",
        "property_id",
        string="Offers"
    )

    # Constraints

    _sql_constraints = [
        ('positive_expected_price', 'CHECK(expected_price > 0)', ''),
        ('positive_selling_price', 'CHECK(selling_price > 0)', ''),
    ]

    # Private methods

    @api.depends("offer_ids")
    def _compute_best_offer(self):
        for record in self:
            max_price = 0
            for offer in record.offer_ids:
                if offer.price > max_price:
                    max_price = offer.price
            record.best_offer = max_price

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.onchange("has_garden")
    def _onchange_has_garden(self):
        if not self.has_garden:
            self.garden_area = 0

    @api.constrains('expected_price', 'selling_price')
    def _check_selling_price(self):
        for property_record in self:
            if float_is_zero(property_record.expected_price, precision_digits=2):
                continue

            lower_limit = property_record.expected_price * 0.9
            if float_compare(property_record.selling_price, lower_limit, precision_digits=2) == -1:
                raise exceptions.ValidationError(
                    "Selling price cannot be lower than 90% of the expected price."
                )

    # Actions
    def button_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise exceptions.UserError(
                    "A sold property cannot be calceled.")
            record.write({'state': 'cancelled'})

    def button_sold(self):
        for record in self:
            if record.state == 'canceled':
                raise exceptions.UserError(
                    "A canceled property cannot be sold."
                )
            record.write({'state': 'sold'})
