from odoo import api, fields, models


class PosOrder(models.Model):
    _inherit = "pos.order"

    daily_order_number = fields.Integer(
        index=True,
        readonly=True,
    )

    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        for rec in res:
            if not rec.daily_order_number and rec.config_id.enable_daily_reset:
                rec.daily_order_number = self.env["pos.daily.counter"].get_next_number(
                    rec.config_id
                )
        return res
