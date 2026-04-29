from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Literal

OrderSide = Literal['sell', 'buy']

@dataclass
class OrderEntry:

    type: OrderSide
    execution: str
    tradeType: str
    srcCurrency: str
    dstCurrency: str
    price: str
    amount: str
    totalPrice: str
    totalOrderPrice: str
    matchedAmount: str
    unmatchedAmount: str
    clientOrderId: str | None = None
    id: int | None = None
    status: str | None = None
    fee: str | None = None
    created_at : datetime | None = None
    averagePrice: str | None = None
    market: str | None = None
    partial: bool | None = None

    @staticmethod
    def from_dict(data: dict) -> OrderEntry:
        return OrderEntry(
            type=data["type"],
            execution=data["execution"],
            tradeType=data["tradeType"],
            srcCurrency=data["srcCurrency"],
            dstCurrency=data["dstCurrency"],
            price=data["price"],
            amount=data["amount"],
            totalPrice=data["totalPrice"],
            totalOrderPrice=data["totalOrderPrice"],
            matchedAmount=data["matchedAmount"],
            unmatchedAmount=data["unmatchedAmount"],
            clientOrderId=data.get("clientOrderId"),
            id=data["id"] if "id" in data else None,
            status=data["status"] if "status" in data else None,
            fee=data["fee"] if "fee" in data else None,
            created_at=datetime.fromisoformat(data["created_at"].replace('Z', '+00:00')) if "created_at" in data else None,
            averagePrice=data["averagePrice"] if "averagePrice" in data else None,
            market=data["market"] if "market" in data else None,
            partial=data["partial"] if "partial" in data else None,
        )

@dataclass
class GetOrdersResponse:
    status: str
    orders: list[OrderEntry]

    @staticmethod
    def from_dict(data: dict):
        return GetOrdersResponse(
            status=data["status"],
            orders=[OrderEntry.from_dict(o) for o in data.get("orders", [])],
        )
