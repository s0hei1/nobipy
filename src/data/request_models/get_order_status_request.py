from dataclasses import dataclass,asdict
from typing import Any

from apps.nobipy.data.abstracts import DataclassMappings

@dataclass
class GetOrderStatusRequest(DataclassMappings):
    id: int | None = None
    clientOrderId: str | None = None

    def __post_init__(self):
        if self.id is None and self.clientOrderId is None:
            raise ValueError("Either id or clientOrderId must be provided")

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)

        if self.id is None:
            d.pop('id')
        if self.clientOrderId is None:
            d.pop('clientOrderId')

        return d