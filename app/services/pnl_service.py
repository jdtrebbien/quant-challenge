from typing import List, Tuple
from datetime import datetime
from app.models.trade_data import TradeData
from app.repositories.trade_repository import TradeRepository


class PnLService:
    """
    Service layer for handling PnL related operations.
    """

    def __init__(self):
        self.repository = TradeRepository()

    def get_pnl_by_strategy_id_with_timestamp(self, strategy_id: str) -> Tuple[float, datetime]:
        """
        Calculates the PnL associated with a given strategy ID for all trades.

        Args:
            strategy_id (str): The ID of the strategy to filter the trades by.

        Returns:
            Tuple[float, datetime]: The pnl of the strategy with the corresponding timestamp when the data was
            captured from the db.
        """
        trades, timestamp = self.repository.get_all_by_strategy_id_with_timestamp(strategy_id=strategy_id)
        return (self._compute_pnl(trades), timestamp)

    @staticmethod
    def _compute_pnl(trades: List[TradeData]) -> float:
        """
        Computes the total PnL from a list of trades.

        Args:
            trades (List[TradeData]): A list of trades from which to calculate PnL.

        Returns:
        float: The computed PnL value.
        """
        total_pnl = 0.0

        for trade in trades:
            if trade.side == "sell":
                total_pnl += trade.quantity * trade.price
            elif trade.side == "buy":
                total_pnl -= trade.quantity * trade.price

        return total_pnl

    def compute_total_buy_volume(self) -> float:
        """
        Computes the total volume for all buy trades.

        Returns:
            float: The total buy volume.
        """
        trades = self.repository.get_all_by_side("buy")
        return self._get_quantity_sum(trades)

    def compute_total_sell_volume(self) -> float:
        """
        Computes the total volume for all sell trades.

        Returns:
            float: The total sell volume.
        """
        trades = self.repository.get_all_by_side("sell")
        return self._get_quantity_sum(trades)

    @staticmethod
    def _get_quantity_sum(trades: List[TradeData]) -> float:
        """
        Calculates the sum of quantities from a list of trades.

        Args:
            trades (List[TradeData]): A list of trades to sum the quantities of.

        Returns:
            float: The sum of all trade quantities.
        """
        return sum(trade.quantity for trade in trades)
