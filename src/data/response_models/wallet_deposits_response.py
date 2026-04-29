from __future__ import annotations
from dataclasses import dataclass

@dataclass
class DepositTransaction:
    id: int
    amount: str
    currency: str
    description: str
    created_at: str
    calculatedFee: str

    @staticmethod
    def from_dict(data: dict) -> DepositTransaction:
        return DepositTransaction(
            id=data["id"],
            amount=data["amount"],
            currency=data["currency"],
            description=data["description"],
            created_at=data["created_at"],
            calculatedFee=data["calculatedFee"],
        )


@dataclass
class Deposit:
    txHash: str
    address: str
    confirmed: bool
    transaction: DepositTransaction
    currency: str
    blockchainUrl: str
    confirmations: int
    requiredConfirmations: int
    amount: str

    @staticmethod
    def from_dict(data: dict) -> Deposit:
        return Deposit(
            txHash=data["txHash"],
            address=data["address"],
            confirmed=data["confirmed"],
            transaction=DepositTransaction.from_dict(data["transaction"]),
            currency=data["currency"],
            blockchainUrl=data["blockchainUrl"],
            confirmations=data["confirmations"],
            requiredConfirmations=data["requiredConfirmations"],
            amount=data["amount"],
        )


@dataclass
class WalletDepositsResponse:
    status: str
    deposits: list[Deposit]
    hasNext: bool

    @staticmethod
    def from_dict(data: dict) -> WalletDepositsResponse:
        return WalletDepositsResponse(
            status=data["status"],
            deposits=[Deposit.from_dict(d) for d in data["deposits"]],
            hasNext=data["hasNext"],
        )
