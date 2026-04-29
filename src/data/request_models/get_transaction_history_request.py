from dataclasses import dataclass, asdict
from src.data.abstracts import DataclassMappings
from typing import Literal
from datetime import datetime

TransactionType = Literal[
    'deposit',
    'withdraw',
    'buy',
    'sell',
    'manual',
    'referral',
    'transfer',
    'pnl',
    'delegate',
    'staking',
    'yield_farming',
    'discount',
]


@dataclass
class GetTransactionsHistoryRequest(DataclassMappings):
    currency: str | None = None
    tp: TransactionType | None = None
    from_: datetime | None = None
    to: datetime | None = None
    from_id: datetime | None = None


    def to_dict(self) -> dict:
        d = asdict(self)
        d['from'] = d.pop('from_')
        keys = list(d.keys())
        for k in keys:
            if d[k] is None:
                d.pop(k)

        return d
