# -*- coding: utf-8 -*-
{
    'name': "Mapeo de contacto Clases",

    'summary': """
        Mapeo en contacto clasess""",

    'description': """
        Mapeo en contacto clasess
    """,

    'author': "Clup Alpha",
    'website': "http://www.cludalpha.mx",

    'category': 'Contacto',
    'version': '0.1',

    'depends': ['base','contacts'],

    'data': [
        'security/ir.model.access.csv',
        'views/views_res_partner.xml',
        'views/views_clases.xml',
    ],
    
}
