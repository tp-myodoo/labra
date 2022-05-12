# -*- coding: utf-8 -*-

{
    'name': 'Partner check in GUS and VIES',
    'summary': 'Using GUS and VIES webservice, vat, name and address information will be checked and updated',
    'description': """
Partner check in GUS, VIES and on the White List
=========================
* Checks Partner's VAT in GUS and VIES
* Prevent Invoice Validation for Partners with invalid VAT
* Checks Partner's bank accounts on the White List
""",
    'version': '15.0.1.0.00',
    'category': 'Customer Relationship Management',
    'author': 'OpenGLOBE.pl',
    'website': 'http://openglobe.pl',
    'application': False,
    'installable': True,
    'external_dependencies': {
        'python': ['stdnum', 'suds','xmltodict'],
    },
    'depends': [
        'base_vat',
        'account',
        'auth_oauth'
        ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/partner_gus_wizard_view.xml',
        'views/res_partner_view.xml',
        'views/res_config_settings_views.xml',
    ],
    'images': [],
    'auto_install': False,
}
