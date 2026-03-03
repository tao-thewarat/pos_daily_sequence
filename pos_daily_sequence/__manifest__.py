{
    "name": "POS Daily Order Number Reset",
    "summary": "Automatically reset POS order sequence every day",
    "version": "19.0.1.0.0",
    "author": "Lorddoor",
    "category": "Point of Sale",
    "license": "LGPL-3",
    "depends": [
        "point_of_sale",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/pos_config_views.xml",
        "views/pos_order_views.xml",
        "views/pos_daily_counter_views.xml",
        "views/menuitems.xml",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_daily_sequence/static/src/xml/receipt_header.xml",
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
    "price": "29.9",
    "currency": "USD",
}
