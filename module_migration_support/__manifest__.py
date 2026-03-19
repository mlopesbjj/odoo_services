{
    "name": "Module Migration Support",
    "version": "16.0.1.0.0",
    "summary": "Export and compare installed modules between Odoo versions",
    "category": "Tools",
    "author": "Marcio Lopes",
    "website": "https://github.com/mlopesbjj/odoo_services",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/module_migration_report_views.xml",
    ],
    "installable": True,
    "application": True,
}
