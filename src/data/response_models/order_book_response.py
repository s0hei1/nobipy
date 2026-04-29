from __future__ import annotations
from dataclasses import dataclass

@dataclass
class OrderBookEntry:
    price: str
    amount: str

@dataclass
class GetOrderBookResponse:
    status: str
    lastUpdate: int
    lastTradePrice: str
    asks: list[OrderBookEntry]
    bids: list[OrderBookEntry]

    @staticmethod
    def from_dict(data: dict) -> GetOrderBookResponse:
        return GetOrderBookResponse(
            status=data["status"],
            lastUpdate=data["lastUpdate"],
            lastTradePrice=data["lastTradePrice"],
            asks=[OrderBookEntry(price=a[0], amount=a[1]) for a in data["asks"]],
            bids=[OrderBookEntry(price=b[0], amount=b[1]) for b in data["bids"]],
        )

@dataclass
class GetOrderBookAllEntry:
    lastUpdate: int
    asks: list[OrderBookEntry]
    bids: list[OrderBookEntry]


@dataclass
class GetOrderBookAllResponse:
    status: str
    all: dict[str, GetOrderBookAllEntry]

    @staticmethod
    def from_dict(data: dict) -> GetOrderBookAllResponse:
        return GetOrderBookAllResponse(
            status=data.pop("status"),
            all={
                d: GetOrderBookAllEntry(
                    lastUpdate=data[d]["lastUpdate"],
                    asks=[OrderBookEntry(price=a[0], amount=a[1]) for a in data.get(d)["asks"]],
                    bids=[OrderBookEntry(price=b[0], amount=b[1]) for b in data.get(d)["bids"]],
                ) for d in data},
        )


@dataclass
class GetDepthResponse:
    status: str
    lastUpdate: int
    lastTradePrice: str
    asks: List[OrderBookEntry]
    bids: List[OrderBookEntry]

    @staticmethod
    def from_dict(data: dict) -> GetDepthResponse:
        return GetDepthResponse(
            status=data["status"],
            lastUpdate=data["lastUpdate"],
            lastTradePrice=data["lastTradePrice"],
            asks=[OrderBookEntry(price=a[0], amount=a[1]) for a in data["asks"]],
            bids=[OrderBookEntry(price=b[0], amount=b[1]) for b in data["bids"]],
        )
