# POS Daily Order Number Reset (Odoo 19)

This module resets the POS order number every day in Odoo 19.

By default, Odoo uses a continuous sequence for POS orders. In many businesses, especially retail and restaurants, it is more practical to start the order numbering from 1 at the beginning of each day. This module provides that behavior without changing the standard POS workflow.

## What it does

- Resets POS order numbering automatically each day
- Works per POS configuration
- Keeps accounting entries untouched
- Does not interfere with invoicing or journal entries
- Fully compatible with Odoo 19

## Why use this module

Continuous order sequences can become very long and harder to reconcile on a daily basis. For businesses that close and report sales daily (for example, using Z-reports), restarting the order number each day makes tracking and internal reporting clearer.

Example:

| Date       | Order Number |
|------------|--------------|
| 2025-03-01 | 0001         |
| 2025-03-01 | 0002         |
| 2025-03-02 | 0001         |
| 2025-03-02 | 0002         |

Each day starts again from 1.

## Installation

1. Copy the module into your Odoo addons directory.
2. Restart the Odoo server.
3. Update the Apps list.
4. Install the module from the Apps menu.

## Technical Information

- Technical name: `pos_daily_sequence`
- Version: 19.0
- License: LGPL-3
- Dependency: `point_of_sale`

## Notes

This module is designed to be simple and safe for production environments. It does not alter accounting logic or posted documents. It only controls how POS order numbers are generated.

## License

LGPL-3
