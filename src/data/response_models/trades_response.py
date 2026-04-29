from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Trade:
    time: int
    price: str
    volume: str
    type: str


@dataclass
class TradesResponse:
    status: str
    trades: list[Trade]

    @staticmethod
    def from_dict(data: dict) -> TradesResponse:
        return TradesResponse(
            status=data["status"],
            trades=[
                Trade(
                    time=item["time"],
                    price=item["price"],
                    volume=item["volume"],
                    type=item["type"],
                )
                for item in data["trades"]
            ],
        )
