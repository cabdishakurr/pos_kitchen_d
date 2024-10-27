{
    'name': 'POS Kitchen D',
    'version': '1.0',
    'category': 'Point of Sale',
    'summary': 'Kitchen D System for POS orders',
    'description': """
        This module adds a kitchen d system for managing POS orders in the kitchen.
    """,
    'depends': ['point_of_sale', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/pos_kitchen_d_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'pos_kitchen_d/static/src/js/KitchenD.js',
            'pos_kitchen_d/static/src/xml/kitchen_d.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
