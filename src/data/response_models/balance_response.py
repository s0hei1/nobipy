from __future__ import annotations
from dataclasses import dataclass


@dataclass
class BalanceResponse:
    balance: str
    status: str

    @staticmethod
    def from_dict(data: dict) -> BalanceResponse:
        return BalanceResponse(
            balance=data["balance"],
            status=data["status"],
        )

