from typing import List, Tuple
from sqlalchemy.orm import Session
from app.models.trade_data import TradeData
from app.database.database import SessionLocal
from datetime import datetime, timezone


class TradeRepository:
    """
    Repository for handling trades data operations on the `epex_12_20_12_13` table.
    """

    def __init__(self):
        self.db: Session = SessionLocal()

    def get_all_by_strategy_id(self, strategy_id: str) -> List[TradeData]:
        """
        Retrieves all trade records for a given strategy ID.

        Args:
            strategy_id (str): The ID of the strategy to filter trades by.

        Returns:
            List[TradeData]: A list of TradeData instances matching the specified strategy ID.
        """
        try:
            # Query the PnLData table by the specified strategy_id
            results = self.db.query(TradeData).filter(TradeData.strategy == strategy_id).all()
            return results
        finally:
            self.db.close()

    def get_all_by_strategy_id_with_timestamp(self, strategy_id: str) -> Tuple[List[TradeData], datetime]:
        """
        Retrieves all trade records for a given strategy ID with a timestamp.

        Args:
            strategy_id (str): The ID of the strategy to filter trades by.

        Returns:
            Tuple[List[TradeData], datetime]: A list of TradeData instances matching the specified strategy ID
            with a timestamp that is captured right before the db call.
        """
        timestamp = datetime.now(timezone.utc)
        return (self.get_all_by_strategy_id(strategy_id=strategy_id), timestamp)

    def get_all_by_side(self, side: str) -> List[TradeData]:
        """
        Retrieves all trade records for a given side (e.g., 'buy' or 'sell').

        Args:
            side (str): The side of the trade to filter by. Must be 'buy' or 'sell'.

        Returns:
            List[TradeData]: A list of TradeData instances matching the specified side.
        """
        try:
            results = self.db.query(TradeData).filter(TradeData.side == side).all()
            return results
        finally:
            self.db.close()
