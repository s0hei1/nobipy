from __future__ import annotations
from dataclasses import dataclass
from src.data.abstracts import DataclassMappings

@dataclass
class AddFavoriteMarketsRequest(DataclassMappings):
    market : list[str]

    def to_dict(self) -> dict:
        return {
            "market": ','.join(self.market),
        }