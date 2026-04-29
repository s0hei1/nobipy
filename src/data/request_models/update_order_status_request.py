from dataclasses import dataclass
from apps.nobipy.data.abstracts import DataclassMappings
from typing import Literal

OrderStatus = Literal['new','active','inactive','canceled']

@dataclass
class UpdateOrderStatusRequest(DataclassMappings):
    status: OrderStatus
    order: int | None = None
    clientOrderId: str | None = None
