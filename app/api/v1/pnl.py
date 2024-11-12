from fastapi import APIRouter, Path
from app.adapters.pnl_adapter import PnLAdapter
from app.schemas.pnl_data import PnLData
from app.schemas.volume_data import VolumeData

router = APIRouter()


@router.get("/pnl/{strategy_id}")
def get_pnl(strategy_id: str = Path(..., description="Identifier of the strategy")) -> PnLData:
    """
    Retrieves the PnL data for a specified strategy.

    Args:
        strategy_id (str): The unique identifier of the strategy.

    Returns:
        PnLData: An object containing PnL information such as strategy name, value, unit, and capture time.
    """
    return PnLAdapter().get_pnl_by_strategy_id(strategy_id)


@router.get("/pnl/total_volume/buy")
def get_total_volume_buy() -> VolumeData:
    """
    Computes the total buy volume for all trades.

    Returns:
        VolumeData: An object containing the total buy volume.
    """
    return PnLAdapter().compute_total_buy_volume()


@router.get("/pnl/total_volume/sell")
def get_total_volume_sell() -> VolumeData:
    """
    Computes the total sell volume for all trades.

    Returns:
        VolumeData: An object containing the total sell volume.
    """
    return PnLAdapter().compute_total_sell_volume()
