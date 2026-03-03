# POS Daily Order Number Reset (Odoo 19)

This module resets the POS order number every day in Odoo 19.

By default, Odoo uses a continuous sequence for POS orders. In many businesses, especially retail and restaurants, it is more practical to start the order numbering from 1 at the beginning of each day. This module provides that behavior without changing the standard POS workflow.

---

## Key Features

- Daily automatic reset of POS order numbering
- Custom reset time (not limited to midnight)
- Works per POS configuration
- Supports multiple POS in the same company
- Timezone-aware reset logic
- No impact on accounting entries or invoices
- Concurrency-safe counter logic
- Designed for production environments

---

## What it does

- Generates a separate counter per POS and per reset period
- Automatically starts numbering from 1 after the configured reset time
- Keeps historical order numbers unchanged
- Does not modify Odoo’s core POS sequence

---

## Why use this module

Continuous order sequences can become very long and harder to reconcile on a daily basis. For businesses that close and report sales daily (for example, using Z-reports), restarting the order number each day makes tracking and internal reporting clearer.

Example:

| Date       | Order Number |
|------------|--------------|
| 2025-03-01 | 0001         |
| 2025-03-01 | 0002         |
| 2025-03-02 | 0001         |
| 2025-03-02 | 0002         |

Each reset period starts again from 1.

---

## Configuration

1. Go to **Point of Sale → Configuration → Point of Sale**
2. Open your POS configuration
3. Enable **Daily Counter Reset**
4. Set the desired reset time (HH:MM format)
5. Save

The system will automatically handle numbering based on your configuration.

---

## Installation

1. Copy the module into your Odoo addons directory.
2. Restart the Odoo server.
3. Update the Apps list.
4. Install the module from the Apps menu.

---

## Technical Information

- Technical name: `pos_daily_sequence`
- Version: 19.0
- License: LGPL-3
- Dependency: `point_of_sale`
- Model added: `pos.daily.counter`
- Field added: `daily_order_number` on `pos.order`

---

## Notes

This module is designed to be simple and safe for production environments.

- It does not alter accounting logic.
- It does not modify posted invoices.
- It does not interfere with POS sessions.
- It only controls how the daily order number is generated.

---

## License

LGPL-3
