from app.services.pnl_service import PnLService
from app.mappers.pnl_mapper import PnLMapper
from app.models.volume_model import VolumeData
from app.models.pnl_model import PnLData

class PnLAdapter:
    """
    Adapter for handling and transforming PnL related data for response.
    """

    def __init__(self):
        self.service = PnLService()
        self.mapper = PnLMapper()

    def compute_total_buy_volume(self) -> VolumeData:
        """
        Computes the total buy volume and maps it to VolumeData.

        Returns:
            VolumeData: An object containing the total buy volume.
        """
        return self.mapper.from_quantity_to_volume(
            self.service.compute_total_buy_volume()
        )
    
    def compute_total_sell_volume(self) -> VolumeData:
        """
        Computes the total sell volume and maps it to VolumeData.

        Returns:
            VolumeData: An object containing the total sell volume.
        """
        return self.mapper.from_quantity_to_volume(
            self.service.compute_total_sell_volume()
        )
    
    def get_pnl_by_strategy_id(self, strategy_id: str) -> PnLData:
        """
        Retrieves the PnL data for a specific strategy ID.

        Args:
            strategy_id (str): The identifier of the strategy for which PnL data is retrieved.

        Returns:
            PnLData: An object containing the strategy's PnL data, including strategy ID,
            PnL value, currency unit, and capture timestamp.
        """
        pnl_value, timestamp = self.service.get_pnl_by_strategy_id_with_timestamp(strategy_id=strategy_id)
        return self.mapper.to_pnl_data(
            strategy_id,
            pnl_value,
            "EUR",
            timestamp
        )
