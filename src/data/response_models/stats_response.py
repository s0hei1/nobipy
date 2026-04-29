from __future__ import annotations
from dataclasses import dataclass

@dataclass
class MarketStat:
    isClosed: bool
    bestSell: str
    bestBuy: str
    volumeSrc: str
    volumeDst: str
    latest: str
    mark: str
    dayLow: str
    dayHigh: str
    dayOpen: str
    dayClose: str
    dayChange: str


@dataclass
class StatsResponse:
    status: str
    stats: dict[str, MarketStat]

    @staticmethod
    def from_dict(data: dict) -> StatsResponse:
        stats = {
            symbol: MarketStat(**values)
            for symbol, values in data["stats"].items()
        }

        return StatsResponse(
            status=data["status"],
            stats=stats
        )
