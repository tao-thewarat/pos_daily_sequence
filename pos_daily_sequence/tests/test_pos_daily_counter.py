from datetime import datetime
from unittest.mock import patch
from odoo.tests.common import TransactionCase


class TestPosDailyCounter(TransactionCase):

    def setUp(self):
        super().setUp()

        self.company = self.env.company

        self.pos_config = self.env["pos.config"].create(
            {
                "name": "Test POS",
                "enable_daily_reset": True,
                "reset_time": "16:00",
                "tz": "UTC",
                "company_id": self.company.id,
            }
        )
        self.pos_config2 = self.env["pos.config"].create(
            {
                "name": "Test POS",
                "enable_daily_reset": True,
                "reset_time": "16-00",
                "tz": "UTC",
                "company_id": self.company.id,
            }
        )
        self.session = self.env["pos.session"].create(
            {
                "config_id": self.pos_config.id,
            }
        )
        self.session2 = self.env["pos.session"].create(
            {
                "config_id": self.pos_config2.id,
            }
        )
        self.session.action_pos_session_open()
        self.session2.action_pos_session_open()
        self.order_model = self.env["pos.order"]
        self.counter_model = self.env["pos.daily.counter"].create({
            "pos_config_id": self.pos_config.id,
            "period_start": datetime(2026, 3, 3, 15, 0, 0),
            "number": 0,
        })

    def test_increment_before_reset(self):
        with patch("odoo.fields.Datetime.now") as mock_now:
            mock_now.return_value = datetime(2026, 3, 3, 15, 0, 0)

            order1 = self.order_model.create(
                {
                    "config_id": self.pos_config.id,
                    "session_id": self.session.id,
                    "amount_total": 0,
                    "amount_paid": 0,
                    "amount_return": 0,
                    "amount_tax": 0,
                }
            )

            order2 = self.order_model.create(
                {
                    "config_id": self.pos_config.id,
                    "session_id": self.session.id,
                    "amount_total": 0,
                    "amount_paid": 0,
                    "amount_return": 0,
                    "amount_tax": 0,
                }
            )

            self.assertEqual(order1.daily_order_number, 1)
            self.assertEqual(order2.daily_order_number, 2)

    def test_increment_after_reset(self):
        with patch("odoo.fields.Datetime.now") as mock_now:
            mock_now.return_value = datetime(2026, 3, 3, 15, 0, 0)
            order1 = self.order_model.create(
                {
                    "config_id": self.pos_config.id,
                    "session_id": self.session.id,
                    "amount_total": 0,
                    "amount_paid": 0,
                    "amount_return": 0,
                    "amount_tax": 0,
                }
            )

            order2 = self.order_model.create(
                {
                    "config_id": self.pos_config.id,
                    "session_id": self.session.id,
                    "amount_total": 0,
                    "amount_paid": 0,
                    "amount_return": 0,
                    "amount_tax": 0,
                }
            )
            self.assertEqual(order1.daily_order_number, 1)
            self.assertEqual(order2.daily_order_number, 2)
            mock_now.return_value = datetime(2026, 3, 3, 16, 5, 0)
            order_after_reset = self.order_model.create(
                {
                    "config_id": self.pos_config.id,
                    "session_id": self.session.id,
                    "amount_total": 0,
                    "amount_paid": 0,
                    "amount_return": 0,
                    "amount_tax": 0,
                }
            )
            self.assertEqual(order_after_reset.daily_order_number, 1)

    def test_get_period_start_fallback_to_zero(self):
        self.pos_config.reset_time = "invalid"
        with patch("odoo.fields.Datetime.now") as mock_now:
            mock_now.return_value = datetime(2026, 3, 3, 10, 0, 0)
            period = self.counter_model._get_period_start(self.pos_config)
            expected = datetime(2026, 3, 3, 0, 0, 0)
            self.assertEqual(period, expected)
