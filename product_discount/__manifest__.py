# -*- coding: utf-8 -*-
{
    'name': "product_discount",

    'summary': """
        Module helps to add discount(%) on product, on webshop shows original and discounted price on product page """,

    'description': """
        Module helps to add discount(%) on product, on webshop shows original and discounted price on product page """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '16.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'demo/demo.xml',
        'views/product_views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'pre_init_hook': 'pre_init_hook',
}
