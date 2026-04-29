from dataclasses import dataclass
from src.data.abstracts import DataclassMappings

@dataclass
class GetTradesRequest(DataclassMappings):
    srcCurrency: str | None = None
    dstCurrency: str | None = None
    fromId: int | None = None