from sqlalchemy import Column, String, Float, Integer, CheckConstraint
from app.database.database import Base

class TradeData(Base):
    """
    SQLAlchemy model for the `epex_12_20_12_13` table, representing trade data.

    Attributes:
        id (str): The primary key, unique identifier for each trade.
        quantity (int): The quantity of the asset being traded.
        price (float): The price at which the trade was executed.
        side (str): The side of the trade, either 'buy' or 'sell'.
        strategy (str): The strategy identifier associated with the trade.
    """
    __tablename__ = "epex_12_20_12_13"

    id = Column(String, primary_key=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    side = Column(String, nullable=False)
    strategy = Column(String, nullable=False)

    __table_args__ = (
        CheckConstraint("side IN ('buy', 'sell')", name="side_check"),
    )
