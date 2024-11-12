import unittest
from unittest.mock import MagicMock
from datetime import datetime
from app.services.pnl_service import PnLService
from app.models.trade_data import TradeData


class TestPnLService(unittest.TestCase):
    def setUp(self):
        self.service = PnLService()
        self.service.repository = MagicMock()

    def test_compute_total_buy_volume_empty(self):
        # Given
        self.service.repository.get_all_by_side.return_value = []

        # When
        result = self.service.compute_total_buy_volume()

        # Then
        self.assertEqual(result, 0)

    def test_compute_total_sell_volume_empty(self):
        # Given
        self.service.repository.get_all_by_side.return_value = []

        # When
        result = self.service.compute_total_sell_volume()

        # Then
        self.assertEqual(result, 0)

    def test_get_pnl_by_strategy_id_with_timestamp_empty(self):
        # Given
        timestamp = datetime.now()
        self.service.repository.get_all_by_strategy_id_with_timestamp.return_value = ([], timestamp)

        # When
        result, result_timestamp = self.service.get_pnl_by_strategy_id_with_timestamp("strategy1")

        # Then
        self.assertEqual(result, 0)
        self.assertEqual(result_timestamp, timestamp)

    def test_compute_total_buy_volume(self):
        # Given
        trades = [
            TradeData(quantity=10, price=5.0, side="buy", strategy="strategy1"),
            TradeData(quantity=15, price=4.0, side="buy", strategy="strategy1"),
        ]
        self.service.repository.get_all_by_side.return_value = trades

        # When
        result = self.service.compute_total_buy_volume()

        # Then
        self.assertEqual(result, 25)

    def test_compute_total_sell_volume(self):
        # Given
        trades = [
            TradeData(quantity=10, price=5.0, side="sell", strategy="strategy1"),
            TradeData(quantity=20, price=3.0, side="sell", strategy="strategy1"),
        ]
        self.service.repository.get_all_by_side.return_value = trades

        # When
        result = self.service.compute_total_sell_volume()

        # Then
        self.assertEqual(result, 30)

    def test_get_pnl_by_strategy_id_with_timestamp(self):
        # Given
        trades = [
            TradeData(quantity=10, price=5.0, side="buy", strategy="strategy1"),
            TradeData(quantity=20, price=3.0, side="sell", strategy="strategy1"),
        ]
        timestamp = datetime.now()
        self.service.repository.get_all_by_strategy_id_with_timestamp.return_value = (trades, timestamp)

        # When
        result, result_timestamp = self.service.get_pnl_by_strategy_id_with_timestamp("strategy1")

        # Then
        expected_pnl = (-10 * 5.0) + (20 * 3.0)
        self.assertEqual(result, expected_pnl)
        self.assertEqual(result_timestamp, timestamp)


if __name__ == "__main__":
    unittest.main()
