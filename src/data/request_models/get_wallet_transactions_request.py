from dataclasses import dataclass
from src.data.abstracts import DataclassMappings


@dataclass
class GetWalletTransactionsRequest(DataclassMappings):
    wallet_id : int