from app.models.volume_model import VolumeData
from app.models.pnl_model import PnLData
from datetime import datetime


class PnLMapper:
    """
    Mapper for transforming raw data into structured data transfer objects (DTOs)
    for PnL and volume data.
    """
    @staticmethod
    def from_quantity_to_volume(quantity: float) -> VolumeData:
        """
        Converts a quantity value into a VolumeData object.

        Args:
            quantity (float): The quantity to be converted into volume.

        Returns:
            VolumeData: An object containing the specified volume.
        """
        return VolumeData(volume=quantity)
    
    @staticmethod
    def to_pnl_data(strategy: str, value: float, unit: str, capture_time: datetime) -> PnLData:
        """
        Maps the provided values into a PnLData object.

        Args:
            strategy (str): The strategy identifier.
            value (float): The PnL value.
            unit (str): The unit of the PnL value, such as 'EUR'.
            capture_time (datetime): The timestamp when the PnL data was captured.

        Returns:
            PnLData: An object containing structured PnL information.
        """
        return PnLData(
            strategy=strategy,
            value=value,
            unit=unit,
            capture_time=capture_time
        )