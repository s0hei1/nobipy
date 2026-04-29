from __future__ import annotations
from dataclasses import dataclass
from dataclasses import asdict
from src.data.abstracts import DataclassMappings


@dataclass
class GenerateWalletAddressRequest(DataclassMappings):
    currency : str | None
    wallet_id : str | None
    network : str | None = None

    def __post_init__(self):
        if self.currency is None and self.wallet_id is None:
            raise ValueError("Currency and Wallet ID cannot be None at same time")


