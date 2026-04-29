from __future__ import annotations
from dataclasses import dataclass

@dataclass
class BankCard:
    number: str
    bank: str
    owner: str
    confirmed: bool
    status: str

    @staticmethod
    def from_dict(data: dict) -> BankCard:
        return BankCard(
            number=data["number"],
            bank=data["bank"],
            owner=data["owner"],
            confirmed=data["confirmed"],
            status=data["status"],
        )


@dataclass
class BankAccount:
    id: int
    number: str
    shaba: str
    bank: str
    owner: str
    confirmed: bool
    status: str

    @staticmethod
    def from_dict(data: dict) -> BankAccount:
        return BankAccount(
            id=data["id"],
            number=data["number"],
            shaba=data["shaba"],
            bank=data["bank"],
            owner=data["owner"],
            confirmed=data["confirmed"],
            status=data["status"],
        )


@dataclass
class Verifications:
    email: bool
    phone: bool
    mobile: bool
    identity: bool
    selfie: bool
    bankAccount: bool
    bankCard: bool
    address: bool
    city: bool
    nationalSerialNumber: bool

    @staticmethod
    def from_dict(data: dict) -> "Verifications":
        return Verifications(
            email=data["email"],
            phone=data["phone"],
            mobile=data["mobile"],
            identity=data["identity"],
            selfie=data["selfie"],
            bankAccount=data["bankAccount"],
            bankCard=data["bankCard"],
            address=data["address"],
            city=data["city"],
            nationalSerialNumber=data["nationalSerialNumber"],
        )


@dataclass
class PendingVerifications:
    email: bool
    phone: bool
    mobile: bool
    identity: bool
    selfie: bool
    bankAccount: bool
    bankCard: bool

    @staticmethod
    def from_dict(data: dict) -> PendingVerifications:
        return PendingVerifications(
            email=data["email"],
            phone=data["phone"],
            mobile=data["mobile"],
            identity=data["identity"],
            selfie=data["selfie"],
            bankAccount=data["bankAccount"],
            bankCard=data["bankCard"],
        )


@dataclass
class Options:
    fee: str
    feeUsdt: str
    isManualFee: bool
    tfa: bool
    socialLoginEnabled: bool

    @staticmethod
    def from_dict(data: dict) -> Options:
        return Options(
            fee=data["fee"],
            feeUsdt=data["feeUsdt"],
            isManualFee=data["isManualFee"],
            tfa=data["tfa"],
            socialLoginEnabled=data["socialLoginEnabled"],
        )


@dataclass
class Profile:
    firstName: str
    lastName: str
    nationalCode: str
    email: str
    username: str
    phone: str
    mobile: str
    city: str
    bankCards: list[BankCard]
    bankAccounts: list[BankAccount]
    verifications: Verifications
    pendingVerifications: PendingVerifications
    options: Options
    withdrawEligible: bool

    @staticmethod
    def from_dict(data: dict) -> Profile:
        return Profile(
            firstName=data["firstName"],
            lastName=data["lastName"],
            nationalCode=data["nationalCode"],
            email=data["email"],
            username=data["username"],
            phone=data["phone"],
            mobile=data["mobile"],
            city=data["city"],
            bankCards=[BankCard.from_dict(x) for x in data["bankCards"]],
            bankAccounts=[BankAccount.from_dict(x) for x in data["bankAccounts"]],
            verifications=Verifications.from_dict(data["verifications"]),
            pendingVerifications=PendingVerifications.from_dict(data["pendingVerifications"]),
            options=Options.from_dict(data["options"]),
            withdrawEligible=data["withdrawEligible"],
        )

@dataclass
class TradeStats:
    monthTradesTotal: str
    monthTradesCount: int

    @staticmethod
    def from_dict(data: dict) -> TradeStats:
        return TradeStats(
            monthTradesTotal=data["monthTradesTotal"],
            monthTradesCount=data["monthTradesCount"],
        )

@dataclass
class GetProfileResponse:
    status: str
    profile: Profile
    tradeStats: TradeStats
    websocketAuthParam: str

    @staticmethod
    def from_dict(data: dict) -> GetProfileResponse:
        return GetProfileResponse(
            status=data["status"],
            profile=Profile.from_dict(data["profile"]),
            tradeStats=TradeStats.from_dict(data["tradeStats"]),
            websocketAuthParam=data["we_id"],
        )