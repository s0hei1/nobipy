from __future__ import annotations
from dataclasses import dataclass

@dataclass
class GenerateWalletAddressResponse:
    status: str
    address: str

    @staticmethod
    def from_dict(data: dict) -> GenerateWalletAddressResponse:
        return GenerateWalletAddressResponse(
            status=data["status"],
            address=data["address"],
        )
