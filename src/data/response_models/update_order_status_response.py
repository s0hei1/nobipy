from __future__ import annotations
from dataclasses import dataclass
from src.data.response_models.get_spot_orders_response import OrderEntry


@dataclass
class UpdateOrderStatusResponse:
    status: str
    order: OrderEntry

    @staticmethod
    def from_dict(data: dict) -> UpdateOrderStatusResponse:
        return UpdateOrderStatusResponse(
            status=data["status"],
            order=OrderEntry.from_dict(data["order"]),
        )
