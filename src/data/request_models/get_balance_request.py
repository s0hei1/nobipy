from dataclasses import dataclass,asdict
from apps.nobipy.data.abstracts import DataclassMappings


@dataclass
class GetBalanceRequest(DataclassMappings):
    currency : str
