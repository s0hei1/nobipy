from dataclasses import dataclass

@dataclass
class SpotTrade:
    id: int
    orderId: int
    srcCurrency: str
    dstCurrency: str
    market: str
    timestamp: str
    type: str
    price: str
    amount: str
    total: str
    fee: str

    @staticmethod
    def from_dict(data: dict):
        return SpotTrade(
            id=data["id"],
            orderId=data["orderId"],
            srcCurrency=data["srcCurrency"],
            dstCurrency=data["dstCurrency"],
            market=data["market"],
            timestamp=data["timestamp"],
            type=data["type"],
            price=data["price"],
            amount=data["amount"],
            total=data["total"],
            fee=data["fee"],
        )


@dataclass
class SpotTradesResponse:
    status: str
    trades: list[SpotTrade]
    hasNext: bool

    @staticmethod
    def from_dict(data: dict):
        return SpotTradesResponse(
            status=data["status"],
            trades=[SpotTrade.from_dict(t) for t in data.get("trades", [])],
            hasNext=data.get("hasNext", False),
        )