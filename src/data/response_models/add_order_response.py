from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Order:
    type: str
    srcCurrency: str
    dstCurrency: str
    price: str
    amount: str
    totalPrice: str
    matchedAmount: float
    unmatchedAmount: str
    id: int
    status: str
    partial: bool
    fee: float
    created_at: str
    clientOrderId: str | None

    @staticmethod
    def from_dict(data: dict) -> "Order":
        return Order(
            type=data["type"],
            srcCurrency=data["srcCurrency"],
            dstCurrency=data["dstCurrency"],
            price=data["price"],
            amount=data["amount"],
            totalPrice=data["totalPrice"],
            matchedAmount=data["matchedAmount"],
            unmatchedAmount=data["unmatchedAmount"],
            id=data["id"],
            status=data["status"],
            partial=data["partial"],
            fee=data["fee"],
            created_at=data["created_at"],
            clientOrderId=data.get("clientOrderId"),
        )


@dataclass
class AddOrderResponse:
    status: str
    order: Order

    @staticmethod
    def from_dict(data: dict) -> AddOrderResponse:
        return AddOrderResponse(
            status=data["status"],
            order=Order.from_dict(data["order"]),
        )
