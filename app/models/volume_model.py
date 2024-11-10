from pydantic import BaseModel

class VolumeData(BaseModel):
    """
    Data model representing the volume of trades.

    Attributes:
        volume (int): The total volume of trades, typically representing the sum of quantities.
    """
    volume: int