from __future__ import annotations
from dataclasses import dataclass
from apps.nobipy.data.abstracts import DataclassMappings
from typing import Literal

OrderType = Literal['buy', 'sell']
ExecutionType = Literal['limit', 'market','stop_limit', 'stop_market']

@dataclass(frozen=True)
class AddOrderRequest(DataclassMappings):
    type: OrderType
    srcCurrency: str
    dstCurrency: str
    amount: float
    price: float | None
    execution: ExecutionType = 'limit'
    stopPrice: float | None = None
    clientOrderId: str | None = None

    def __post_init__(self):
        if self.execution in ('stop_limit', 'stop_market') and self.stopPrice is None:
            raise ValueError('stopPrice can not be None at [stop_limit , stop_market] execution types')
