from dataclasses import dataclass
from apps.nobipy.data.abstracts import DataclassMappings


@dataclass
class GetWalletTransactionsRequest(DataclassMappings):
    wallet_id : int