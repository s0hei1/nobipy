from dataclasses import dataclass,asdict
from src.data.abstracts import DataclassMappings


@dataclass
class GetBalanceRequest(DataclassMappings):
    currency : str
