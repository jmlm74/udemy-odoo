# -*- coding: utf-8 -*-
{
    'name': "Car",
    'sequence': 1,
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '14.0.1.0.0',
    'category': 'Extra Tools',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/car_wizard.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/parking.xml',
        'views/sequence.xml',
        'views/partner_inherit.xml',
        'data/car_template_mail.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
