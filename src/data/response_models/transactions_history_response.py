from __future__ import annotations
from dataclasses import dataclass

@dataclass
class HistoryTransaction:
    id: int
    amount: str
    description: str
    created_at: str
    balance: str
    tp: str
    calculatedFee: str | None
    type: str
    currency: str

    @staticmethod
    def from_dict(data: dict) -> "HistoryTransaction":
        return HistoryTransaction(
            id=data["id"],
            amount=data["amount"],
            description=data["description"],
            created_at=data["created_at"],
            balance=data["balance"],
            tp=data["tp"],
            calculatedFee=data.get("calculatedFee"),
            type=data["type"],
            currency=data["currency"],
        )


@dataclass
class TransactionsHistoryResponse:
    status: str
    transactions: list[HistoryTransaction]
    hasNext: bool

    @staticmethod
    def from_dict(data: dict) -> "TransactionsHistoryResponse":
        return TransactionsHistoryResponse(
            status=data["status"],
            transactions=[HistoryTransaction.from_dict(t) for t in data["transactions"]],
            hasNext=data["hasNext"],
        )
