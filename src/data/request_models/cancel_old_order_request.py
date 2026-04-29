from dataclasses import dataclass
from typing import Literal
from apps.nobipy.data.abstracts import DataclassMappings

ExecutionType = Literal['limit', 'market','stop_limit', 'stop_market']
TradeType = Literal['margin', 'spot']

@dataclass(frozen=True)
class CancelOrdersRequest(DataclassMappings):
    hours: float | None = None
    execution: ExecutionType | None = None
    tradeType: TradeType | None = None
    srcCurrency: str | None = None
    dstCurrency: str | None = None
