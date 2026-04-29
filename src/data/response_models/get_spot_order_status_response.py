from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Literal

from src.data.abstracts import DataclassMappings

OrderSide = Literal['sell', 'buy']
OrderStatus = Literal['Active', 'Done', 'Inactive', 'Canceled']


@dataclass
class OrderStatusEntry(DataclassMappings):
    id: int
    type: OrderSide
    status: OrderStatus
    srcCurrency: str
    dstCurrency: str
    amount: str
    price: str
    totalPrice: str
    matchedAmount: str
    unmatchedAmount: str
    fee: str
    partial: bool
    created_at: datetime
    clientOrderId: str | None = None

    @staticmethod
    def from_dict(data: dict) -> OrderStatusEntry:
        return OrderStatusEntry(
            id=data["id"],
            type=data["type"],
            status=data["status"],
            srcCurrency=data["srcCurrency"],
            dstCurrency=data["dstCurrency"],
            amount=data["amount"],
            price=data["price"],
            totalPrice=data["totalPrice"],
            matchedAmount=data["matchedAmount"],
            unmatchedAmount=data["unmatchedAmount"],
            fee=data["fee"],
            partial=data["partial"],
            # Handling the ISO 8601 string conversion
            created_at=datetime.fromisoformat(data["created_at"].replace('Z', '+00:00')),
            clientOrderId=data.get("clientOrderId")
        )

@dataclass
class GetOrderStatusResponse:
    status: str
    order: OrderStatusEntry

    @staticmethod
    def from_dict(data: dict):
        return GetOrderStatusResponse(
            status=data["status"],
            order=OrderStatusEntry.from_dict(data["order"]),
        )
