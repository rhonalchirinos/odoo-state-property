# -*- coding: utf-8 -*-
from odoo import http


class Regionalizacion(http.Controller):
    @http.route('/regionalizacion/regionalizacion', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/regionalizacion/regionalizacion/objects', auth='public')
    def list(self, **kw):
        return http.request.render('regionalizacion.listing', {
            'root': '/regionalizacion/regionalizacion',
            'objects': http.request.env['regionalizacion.regionalizacion'].search([]),
        })

    @http.route('/regionalizacion/regionalizacion/objects/<model("regionalizacion.regionalizacion"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('regionalizacion.object', {
            'object': obj
        })
