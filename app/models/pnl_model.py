from pydantic import BaseModel
from datetime import datetime

class PnLData(BaseModel):
    """
    Data model representing PnL data.

    Attributes:
        strategy (str): The identifier of the strategy.
        value (float): The PnL value.
        unit (str): The unit of the PnL value, such as 'EUR'.
        capture_time (datetime): The timestamp when the PnL data was captured.
    """
    strategy: str
    value: float
    unit: str
    capture_time: datetime

    class Config:
        schema_extra = {
            "example": {
                "strategy": "strategy_1",
                "value": 100.0,
                "unit": "EUR",
                "capture_time": "2023-01-01T01:23:45Z"
            }
        }
