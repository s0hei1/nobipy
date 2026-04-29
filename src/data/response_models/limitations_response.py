from __future__ import annotations
from dataclasses import dataclass

@dataclass
class LimitEntry:
    used: str
    limit: str

    @staticmethod
    def from_dict(data: dict) -> LimitEntry:
        return LimitEntry(
            used=data["used"],
            limit=data["limit"],
        )


@dataclass
class Features:
    crypto_trade: bool
    rial_trade: bool
    coin_deposit: bool
    rial_deposit: bool
    coin_withdrawal: bool
    rial_withdrawal: bool

    @staticmethod
    def from_dict(data: dict) -> Features:
        return Features(
            crypto_trade=data["crypto_trade"],
            rial_trade=data["rial_trade"],
            coin_deposit=data["coin_deposit"],
            rial_deposit=data["rial_deposit"],
            coin_withdrawal=data["coin_withdrawal"],
            rial_withdrawal=data["rial_withdrawal"],
        )


@dataclass
class Limits:
    withdrawRialDaily: LimitEntry
    withdrawCoinDaily: LimitEntry
    withdrawTotalDaily: LimitEntry
    withdrawTotalMonthly: LimitEntry

    @staticmethod
    def from_dict(data: dict) -> Limits:
        return Limits(
            withdrawRialDaily=LimitEntry.from_dict(data["withdrawRialDaily"]),
            withdrawCoinDaily=LimitEntry.from_dict(data["withdrawCoinDaily"]),
            withdrawTotalDaily=LimitEntry.from_dict(data["withdrawTotalDaily"]),
            withdrawTotalMonthly=LimitEntry.from_dict(data["withdrawTotalMonthly"]),
        )


@dataclass
class Limitations:
    userLevel: str
    features: Features
    limits: Limits

    @staticmethod
    def from_dict(data: dict) -> Limitations:
        return Limitations(
            userLevel=data["userLevel"],
            features=Features.from_dict(data["features"]),
            limits=Limits.from_dict(data["limits"]),
        )


@dataclass
class LimitationsResponse:
    status: str
    limitations: Limitations

    @staticmethod
    def from_dict(data: dict) -> LimitationsResponse:
        return LimitationsResponse(
            status=data["status"],
            limitations=Limitations.from_dict(data["limitations"]),
        )
