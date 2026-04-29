from __future__ import annotations
from dataclasses import dataclass

@dataclass
class DepositInfoEntry:
    address: str | None
    tag: str | None

    @staticmethod
    def from_dict(data: dict) -> DepositInfoEntry:
        return DepositInfoEntry(
            address=data.get("address"),
            tag=data.get("tag"),
        )


@dataclass
class Wallet:
    depositAddress: str | None
    depositTag: str | None
    depositInfo: dict[str, DepositInfoEntry]
    id: int
    currency: str
    balance: str
    blockedBalance: str
    activeBalance: str
    rialBalance: int
    rialBalanceSell: int

    @staticmethod
    def from_dict(data: dict) -> Wallet:
        return Wallet(
            depositAddress=data.get("depositAddress"),
            depositTag=data.get("depositTag"),
            depositInfo={
                key: DepositInfoEntry.from_dict(value)
                for key, value in data.get("depositInfo", {}).items()
            },
            id=data["id"],
            currency=data["currency"],
            balance=data["balance"],
            blockedBalance=data["blockedBalance"],
            activeBalance=data["activeBalance"],
            rialBalance=data["rialBalance"],
            rialBalanceSell=data["rialBalanceSell"],
        )


@dataclass
class GetWalletsListResponse:
    status: str
    wallets: list[Wallet]

    @staticmethod
    def from_dict(data: dict) -> GetWalletsListResponse:
        return GetWalletsListResponse(
            status=data["status"],
            wallets=[Wallet.from_dict(w) for w in data["wallets"]],
        )

@dataclass
class WalletEntry:
    id: int
    balance: str
    blocked: str

    @staticmethod
    def from_dict(data: dict) -> WalletEntry:
        return WalletEntry(
            id=data["id"],
            balance=data["balance"],
            blocked=data["blocked"],
        )


@dataclass
class GetWalletsV2Response:
    status: str
    wallets: dict[str, WalletEntry]

    @staticmethod
    def from_dict(data: dict) -> GetWalletsV2Response:
        return GetWalletsV2Response(
            status=data["status"],
            wallets={
                currency: WalletEntry.from_dict(info)
                for currency, info in data["wallets"].items()
            },
        )

