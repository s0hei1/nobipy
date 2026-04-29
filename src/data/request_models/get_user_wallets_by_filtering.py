from dataclasses import dataclass
from apps.nobipy.data.abstracts import DataclassMappings
from typing import Literal

WalletType = Literal['margin', 'spot']

@dataclass
class GetUserWalletsByFilteringResponse(DataclassMappings):
    currencies : list[str] | None = None
    type_ : WalletType = 'spot'

    def to_dict(self):
        return {
            'currencies': ', '.join(self.currencies),
            'type': self.type_,
        }