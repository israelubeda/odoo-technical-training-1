# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academia',
    
    'summary': """App de prueba Academia""",

    'description': """
        mODULOS DE PRUEBAS:
        - Cursos
        - Sesiones
        - Attendees
        """,
    
    'author': 'Israel Ubeda Bravo',
    
    'website': 'https://israelubeda.github.io/',
    
    'category': 'Training',
    'version': '15.0.1',
    
    'depends': ['sale'],
    
    'data': [
        'security/seguridad.xml',
        'security/ir.model.access.csv',
        'views/academia_menuitem.xml',
        'views/curso_vista.xml',
        'views/libro_menuitem.xml',
        'views/voluntarios_menuitem.xml',
        'views/nave_menuitem.xml',
        'views/nave_vista.xml',
        'views/libro_vista.xml',
        #'views/session_views.xml',
        #'views/sales_views_inherit.xml',
        #'views/product_views_inherit.xml',
        #'views/academy_web_templates.xml',
        #'wizard/sale_wizard_view.xml',
        #'report/session_report_templates.xml',
    ],
    'demo': [
        'demo/demo_isra.xml',
    ],
    #Add license to remove License Warning
    'license': 'OPL-1'
}
