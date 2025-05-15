# -*- coding: utf-8 -*-

from odoo import models, fields, api

from datetime import timedelta


class BidcomStatePropertyOffer(models.Model):
    _name = 'bidcom_state_property_offer'
    _description = 'State Property Offer'
    _order = "price desc"

    price = fields.Float(string='Price')
    status = fields.Selection(
        [
            ('accepted', 'Accepted'),
            ('refused', 'Refused'),
        ],
        string='Status'
    )
    partner_id = fields.Many2one(
        "res.partner", string="Buyer"
    )
    property_id = fields.Many2one(
        "bidcom_state_property",
        string="Property",
        required=True
    )
    validity = fields.Integer(
        string='Validity (days)',
        default=7,
        help="Number of days the offer is valid for. If not set, the offer is valid indefinitely."
    )

    # Computes
    date_deadline = fields.Date(
        compute="_compute_date_deadline",
        string='Valid Until'
    )

    is_offer_accepted = fields.Boolean(
        compute="_is_offer_accepted"
    )

    # Privates
    def _compute_date_deadline(self):
        for record in self:
            validate = record.validity if record.validity else 0
            record.date_deadline = fields.Date.context_today(
                self) + timedelta(days=record.validity)

    @api.depends('property_id.state')
    def _is_offer_accepted(self):
        for record in self:
            record.is_offer_accepted = record.property_id.state in (
                'offer acceptei',
                'sold'
            )

    # Actions
    def action_do_something(self):
        for record in self:
            record.name = "Something"
        return True

    def action_accepted(self):
        for offer in self:
            offer.write({'status': 'accepted'})
            offer.property_id.selling_price = offer.property_id.best_offer
            offer.property_id.partner_id = offer.partner_id
            offer.property_id.write({'state': 'offer accepted'})

    def action_refused(self):
        for offer in self:
            offer.write({'status': 'refused'})
