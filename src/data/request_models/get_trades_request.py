from dataclasses import dataclass
from apps.nobipy.data.abstracts import DataclassMappings

@dataclass
class GetTradesRequest(DataclassMappings):
    srcCurrency: str | None = None
    dstCurrency: str | None = None
    fromId: int | None = None