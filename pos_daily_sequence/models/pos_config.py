from odoo import models, fields
from odoo.addons.base.models.res_partner import _tz_get


class PosConfig(models.Model):
    _inherit = "pos.config"

    enable_daily_reset = fields.Boolean(
        string="Enable Daily Counter Reset",
        default=False,
    )
    reset_time = fields.Char(
        default="00:00",
        help="Hour in 24h format. Example: 0.0 = 00:00, 6.5 = 06:30",
    )
    tz = fields.Selection(
        selection=_tz_get,
        default=lambda self: self.env.context.get('tz') or self.env.user.tz,
    )
