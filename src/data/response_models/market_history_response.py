from __future__ import annotations
from dataclasses import dataclass

@dataclass
class MarketHistoryResponse:
    s: str
    t: list[int]
    o: list[int]
    h: list[int]
    l: list[int]
    c: list[int]
    v: list[float]

    @staticmethod
    def from_dict(data: dict) -> MarketHistoryResponse:
        return MarketHistoryResponse(
                s=data["s"],
                t=data["t"],
                o=data["o"],
                h=data["h"],
                l=data["l"],
                c=data["c"],
                v=data["v"],
            )
