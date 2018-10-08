# -*- coding: utf-8 -*-
{
    'name': "Account Payment By Employee",

    'summary': """
        Allows you to record vendor bill payments done by Employees.""",

    'description': """
    """,

    'author': "JT Moniker",
    'website': "https://www.jtmoniker.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '11.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'hr', 'payment'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
}