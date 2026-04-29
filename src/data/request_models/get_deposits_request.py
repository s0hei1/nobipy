from dataclasses import dataclass
from apps.nobipy.data.abstracts import DataclassMappings


@dataclass
class GetDepositsRequest(DataclassMappings):
    wallet : str = 'all'