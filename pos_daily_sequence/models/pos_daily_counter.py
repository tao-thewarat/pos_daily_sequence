from odoo import api, fields, models
from datetime import timedelta
import pytz


class PosDailyCounter(models.Model):
    _name = "pos.daily.counter"
    _description = "POS Daily Counter"
    _rec_name = "period_start"
    _order = "period_start desc"

    _sql_constraints = [
        (
            "unique_period_pos",
            "unique(period_start, pos_config_id)",
            "Counter already exists for this POS and period.",
        )
    ]

    period_start = fields.Datetime(
        required=True,
        index=True,
    )
    number = fields.Integer(
        required=True,
        default=0,
    )
    pos_config_id = fields.Many2one(
        comodel_name="pos.config",
        required=True,
        ondelete="cascade",
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        required=True,
        default=lambda self: self.env.company,
    )

    @api.model
    def _get_period_start(self, pos):
        now_utc = fields.Datetime.now()
        tz = pytz.timezone(pos.tz or "UTC")
        now_local = pytz.utc.localize(now_utc).astimezone(tz)
        try:
            hour, minute = map(int, pos.reset_time.split(":"))
        except Exception:
            hour, minute = 0, 0
        reset_today = now_local.replace(
            hour=hour,
            minute=minute,
            second=0,
            microsecond=0,
        )

        if now_local >= reset_today:
            period_local = reset_today
        else:
            period_local = reset_today - timedelta(days=1)
        period_utc = period_local.astimezone(pytz.utc).replace(tzinfo=None)
        return period_utc

    @api.model
    def get_next_number(self, pos):
        period_start = self._get_period_start(pos)

        counter = self.search([
            ("pos_config_id", "=", pos.id),
            ("period_start", "=", period_start),
        ], limit=1)

        if not counter:
            counter = self.create({
                "period_start": period_start,
                "pos_config_id": pos.id,
                "company_id": pos.company_id.id,
                "number": 0,
            })

        counter.number += 1
        return counter.number
