# -*- coding: utf-8 -*-
{
    'name': "Indian GST Number Validation",

    'summary': """
        Checks the GST Number ( GSTIN ) for accuracy""",

    'description': """
        Performs the following checks when you enter a GSTIN number :
			1. Length
            2. Format 
            3. Checksum
		
		It will give you a simple warning if it finds a wrong entry.
    """,

    'author': "Aditya Agarwal",
    'website': "http://www.qilinlab.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
}