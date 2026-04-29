from dataclasses import dataclass
from apps.nobipy.data.abstracts import DataclassMappings
from typing import Literal

OrderStatus = Literal['all', 'open', 'close', 'done']
OrderSide = Literal['sell', 'buy']
ExecutionType = Literal['limit', 'market','stop_limit', 'stop_market']
TradeType = Literal['margin', 'spot']
OrderingType = Literal['id', '-id-', 'created_at', 'created_at-', 'price', 'price-']


@dataclass
class GetSpotOrdersRequest(DataclassMappings):
    status : OrderStatus = 'open'
    type: OrderSide | None = None
    execution: ExecutionType | None = None
    tradeType: TradeType | None = None
    srcCurrency: str | None = None
    dstCurrency: str | None = None
    details: int = 1
    fromId: int = 1
    order: OrderingType | None = None