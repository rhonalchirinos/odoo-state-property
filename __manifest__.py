# -*- coding: utf-8 -*-
{
    'name': "regionalizacion",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': """
        Long description of module's purpose
    """,
    'author': "Bidcom",
    'website': "https://bidcom.com.ar",
    'category': 'Extra Tools',
    'version': '0.1',
    'depends': ['base', 'web'],
    'data': [
        'views/state_property.xml',
        'views/partner_inherit.xml',
        'views/regionalization.xml',
        'views/my_custom.xml',
        'views/menus.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'regionalizacion/static/src/js/my_custom_template.js',
            'regionalizacion/static/src/xml/my_custom_template.xml',
            'regionalizacion/static/src/scss/my_custom_template.scss',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
