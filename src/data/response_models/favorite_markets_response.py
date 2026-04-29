from __future__ import annotations
from dataclasses import dataclass

@dataclass
class FavoriteMarketsResponse:
    status: str
    favoriteMarkets: list[str]

    @staticmethod
    def from_dict(data: dict) -> "FavoriteMarketsResponse":
        return FavoriteMarketsResponse(
            status=data["status"],
            favoriteMarkets=data["favoriteMarkets"],
        )

