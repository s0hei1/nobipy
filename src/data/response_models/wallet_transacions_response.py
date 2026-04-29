from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Transaction:
    currency: str
    created_at: str
    calculatedFee: str
    id: int
    amount: str
    description: str

    @staticmethod
    def from_dict(data: dict) -> "Transaction":
        return Transaction(
            currency=data["currency"],
            created_at=data["created_at"],
            calculatedFee=data["calculatedFee"],
            id=data["id"],
            amount=data["amount"],
            description=data["description"],
        )


@dataclass
class WalletTransactionsResponse:
    status: str
    transactions: list[Transaction]
    hasNext: bool

    @staticmethod
    def from_dict(data: dict) -> "WalletTransactionsResponse":
        return WalletTransactionsResponse(
            status=data["status"],
            transactions=[Transaction.from_dict(t) for t in data["transactions"]],
            hasNext=data["hasNext"],
        )
