{
    'name'              :"Training Odoo",
    'summary'           :""" Modul untuk latihan technical Odoo """,
    'description'       :""""
    |   Modul ini berfungsi untuk menjalankan technical documentation pada
    website resmi odoo.com. Bahan yang dipelajari:
        - ORM
        - Berbagai View
        - Report
        - Wizard
        - Dll
    """,
    'author'            :"Kevin Benaya Sava Nugraha",
    'category'          :"Uncategorized",
    'version'           :"1.0",
    # any module neccesary for this one to work correctly
    "depends"           : [
        "base",
    ],
    # always loaded
    'data'              : [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    "demo"              : [
        'demo/demo.xml',
    ],
    
    'application'       : True,
}